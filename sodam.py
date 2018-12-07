#!/anaconda/bin/python

'''
Copyright 2018 Jannis Bloemendal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

On Object State Testing (Adaptation in Python)
D.C. Kunk, N. Suchak, J. Gao, P. Hsia
https://pdfs.semanticscholar.org/c099/37b9d87cf8020fc897b882c412229f5a7c68.pdf
'''

class SodaMachine:

    total = 0
    tmp = 0

    sodas = 0
    fruits = 0
    mueslis = 0
    nuts = 0

    serviceCode = 0 
    mut = 0

    def __init__(self):
        self.reset()


    def add50c(self):
        self.tmp = self.tmp + 1


    def return50cs(self):
        self.tmp = 0


    def reduce(self, soda=False, muesli=False, nuts=False, fruits=False):
        if (soda or fruits) and (nuts or muesli):
            return 1
        return 0


    def cumulate(self, soda=0, muesli=0, nuts=0, fruits=0):
        cumulative = 0 
        cumulative += soda * 2
        cumulative += fruits * 2
        cumulative += muesli * 1
        cumulative += nuts * 1
        return cumulative


    def gross(self, soda, muesli, nuts, fruits):
        cumulative = self.cumulate(soda and 1 or 0, muesli and 1 or 0, nuts and 1 or 0, fruits and 1 or 0)
        cumulative = cumulative - self.reduce(soda, muesli, nuts, fruits)
        return cumulative


    def service(self):
        # refill: int('0000001',2)
        if  self.nuts > 40 or self.mueslis > 40 or self.soda > 40 or self.nuts > 40:
            self.serviceCode = self.serviceCode ^ 1

        # service interval: int('00000010',2)
        if self.mut % 160 == 0:
            self.serviceCode = self.serviceCode ** 2

        # leak: int('00000100',2)
        if self.total <= self.cumulate(self.sodas, self.mueslis, self.nuts, self.fruits):
            self.serviceCode = self.serviceCode & 4

        # 1: refill
        # 2: service
        # 4: leak
        # 7: refill, service, leak
        return self.serviceCode


    def inventory(self, withDraw=False, soda=True, muesli=False, nuts=False, fruits=False):
        # TODO simplify
        if soda and self.sodas >= 40:
            return False
        if muesli and self.mueslis >= 40:
            return False
        if nuts and self.nuts >= 40:
            return False
        if fruits and self.fruits >= 40:
            return False

        if withDraw:
            if soda:
                self.sodas += 1
            if muesli:
                self.mueslis += 1
            if nuts:
                self.nuts += 1
            if fruits:
                self.fruits += 1

            self.mut += 1
            self.service()

        return True


    def canWithDraw(self, soda=True, muesli=False, nuts=False, fruits=False):
        if not self.inventory(False, soda, muesli, nuts, fruits):
            return False
        if self.tmp <= 0:
            return False
        if self.tmp < self.gross(soda, muesli, nuts, fruits):
            return False
        return True


    def draw(self, soda=True, muesli=False, nuts=False, fruits=False):
        if self.canWithDraw(soda, muesli, nuts, fruits):
            gross = self.gross(soda, muesli, nuts, fruits)
            self.tmp -= gross
            self.total += gross
            return self.inventory(True, soda, muesli, nuts, fruits)
        return False


    def reset(self):
        self.total = 0
        self.tmp = 0

        self.aService = 0
        self.soda = self.mueslis = self.fruits = self.nuts = 0 

if __name__ == '__main__':
    sodaM = SodaMachine()
    print(sodaM.canWithDraw())
    sodaM.add50c()
    sodaM.add50c()
    print(sodaM.canWithDraw())
    print(sodaM.draw())
    print(sodaM.canWithDraw())
