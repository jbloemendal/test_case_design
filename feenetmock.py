import json
from sodam import SodaMachine
from feenet import FeeNetModul

class FeeNetModulMock():

    data = [] 
    infoInv = 0
    sendInv = 0

    def info(self, mId, soda, nut, muesli, fruit, mut, total, tmp):
        self.send({'id': mId, 'total': total, 'soda': soda, 'muesli': muesli, 'nut': nut, 'fruit': fruit, 'mut': mut, 'tmp': tmp})
        self.infoInv += 1


    def send(self, jsData):
       self.sendInv += 1
       self.data.append(jsData)

    def getData(self): 
        return self.data

    def getInfoInv(self):
        return self.infoInv

    def getSendInv(self):
        return self.sendInv


class AluUnitMock():

    cumulateInvo = 0
    verifyInvo = 0
    enqueInfo = 0
    unit = None

    def cumulate(self, soda=0, fruit=0, nuts=0, muesli=0):
        self.cumulateInvo += 1
        return 0

    def verify(self, total, sodas, fruits, nut, muesli, mut, tmp):
        self.verifyInvo += 1
        return 0

    def enque(self, data):
        self.enqueInfo += 0
        if self.unit:
            self.unit.enque(data)

    def setUnit(self, unit):
        self.unit = unit

    def getVerifyInvo(self):
        return selfVerifyInfo

    def getCumulateInvo(self):
        return self.cumulateInvo


class FeeNetServerMock():

    alu = None

    def setAlu(self, alu):
        self.alu = alu

    def on_message(self, msg):
        data = json.loads(msg)
        self.alu.enque(data)
