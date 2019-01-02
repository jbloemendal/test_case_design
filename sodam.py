#!/anaconda/bin/python

from feenet import FeeNetModul

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

    mId = 1

    total = 0
    tmp = 0

    sodas = 0
    fruits = 0
    mueslis = 0
    nuts = 0

    mut = 0

    serviceModul = None

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


    def inventory(self, withDraw=False, soda=True, muesli=False, nuts=False, fruits=False):
        if soda and self.sodas >= 40 or muesli and self.mueslis >= 40 or nuts and self.nuts >= 40 or fruits and self.fruits >= 40:
            return False

        if withDraw:
            self.sodas += soda and 1 or 0
            self.mueslis += muesli and 1 or 0
            self.nuts += nuts and 1 or 0
            self.fruits += fruits and 1 or 0

            self.mut += 1
            if self.serviceModul:
                self.serviceModul.info(self.mId, soda, nuts, fruits, muesli, self.mut, self.total, self.tmp)

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


    def setTotal(self, total):
        self.total = total


    def setCumulate(self, sodas, mueslis, nuts, fruits):
        self.sodas = sodas
        self.mueslis = mueslis
        self.nuts = nuts
        self.fruits = fruits


    def setMut(self, mut):
        self.mut = mut


    def setTmp(self, tmp):
        self.tmp = tmp


    def reset(self):
        self.sodas = self.mueslis = self.fruits = self.nuts = 0 
        self.total = 0
        self.tmp = 0


    def setServiceModul(self, service):
        self.serviceModul = service


if __name__ == '__main__':
    sodaM = SodaMachine()

    modul = FeeNetModul()
    sodaM.setServiceModul(modul)

    for i in range(1, 11):
        sodaM.add50c()
        sodaM.add50c()
        if not sodaM.draw():
            raise Exception('Drawing soda failed')

