#!/anaconda/bin/python
import json
import asyncio
import websocket
import tornado.ioloop
import tornado.web
import tornado.websocket
import threading

class FeeNetModul():

    def info(self, mId, soda, nut, muesli, fruit, mut, total, tmp):
        self.send({'id': mId, 'total': total, 'soda': soda, 'muesli': muesli, 'nut': nut, 'fruit': fruit, 'mut': mut, 'tmp': tmp})

    def send(self, jsData):
        ws = websocket.create_connection("ws://localhost:8888/ws")
        ws.send(json.dumps(jsData))
        message = ws.recv()
        ws.close()


class AluUnit():

    quostats = dict()

    def cumulate(self, soda=0, fruit=0, nuts=0, muesli=0):
        cumulative = 0
        cumulative += soda * 2
        cumulative += fruit * 2
        cumulative += muesli * 1
        cumulative += nuts * 1
        return cumulative

    def verify(self, total, sodas, fruits, nut, muesli, mut, tmp):
        serviceCode = 0

        # leak: int('00000001',2)
        if total < self.cumulate(sodas, fruits, nut, muesli):
            serviceCode = serviceCode | 1

        # service interval: int('00000010',1)
        if total > 0 and mut % 40 == 0 or tmp > 20:
            serviceCode = serviceCode | 2

        # 1: leakage
        # 2: service
        # 3: leakage & service
        return serviceCode

    def enque(self, data):
        print('FeeNetServer enque()')
        code = self.verify(data['total'], data['soda'], data['fruit'], data['nut'], data['muesli'], data['mut'], data['tmp'])
        self.quostats[data['id']] = 0
        self.quostats[data['id']] = self.quostats[data['id']] & code
        
        if code > 0:
            usage = 'usage '+ data['id']+':'+' '+code
            print(usage)

    def getQuostats(self):
        return self.quostats
    
 
class FeeNetServer(tornado.websocket.WebSocketHandler):

    alu = None
    
    def setAlu(alu):
        self.alu = alu

    def on_message(self, msg):
        data = json.loads(msg)
        self.alu.enque(data)


if __name__ == '__main__':
    print('tornado server')
    app = tornado.web.Application([
        (r'/ws', FeeNetServer)
    ])
    app.listen(8888)

    tornado.ioloop.IOLoop.instance().start()
