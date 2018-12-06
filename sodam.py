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

    def __init__(self):
        self.reset()

    def add50c(self):
        self.tmp = self.tmp + 1

    def return50cs(self):
        self.tmp = 0

    def reduce(self, soda=False, muesli=False, nuts=False, fruits=False):
        if (soda or fruits) and (muesli or nuts):
            return 1
        return 0

    def cumulate(self, soda=False, muesli=False, nuts=False, fruits=False):
        cumulative = 0 
        if soda:
            cumulative += 2
        if fruits:
            cumulative += 2
        if muesli:
            cumulative += 1
        if nuts:
            cumulative += 1
        return cumulative

    def canWithDraw(self, soda=True, muesli=False, nuts=False, fruits=False):
        return self.tmp > 0 and self.tmp >= self.cumulate(soda, muesli, nuts, fruits) - self.reduce(soda, muesli, nuts, fruits)

    def draw(self, soda=True, muesli=False, nuts=False, fruits=False):
        if self.canWithDraw(soda, muesli, nuts, fruits):
            cumulative = self.cumulate(soda, muesli, nuts, fruits) - self.reduce(soda, muesli, nuts, fruits)
            self.tmp -= cumulative 
            self.total += cumulative
            return True
        return False

    def reset(self):
        self.total = 0
        self.tmp = 0

if __name__ == '__main__':
    sodaM = SodaMachine()
    print(sodaM.canWithDraw())
    sodaM.add50c()
    sodaM.add50c()
    print(sodaM.canWithDraw())
    print(sodaM.draw())
    print(sodaM.canWithDraw())
