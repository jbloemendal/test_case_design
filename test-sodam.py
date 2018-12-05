#!/anaconda/bin/python

'''
Copyright 2018 Jannis Bloemendal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

On Object State Testing (Adaptation Python)
D.C. Kunk, N. Suchak, J. Gao, P. Hsia
https://pdfs.semanticscholar.org/c099/37b9d87cf8020fc897b882c412229f5a7c68.pdf
'''

import unittest
from sodam import SodaMachine

class SodaMachineTest(unittest.TestCase):

    # test each methods
    def test_canWithDraw(self):
        sodaM = SodaMachine()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_add50c(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.canWithDraw())

    def test_return50cs(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.return50cs()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_draw_path1(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.draw()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_draw_path2(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.draw()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_reset(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.draw()
        sodaM.reset()
        self.assertEqual(False, sodaM.canWithDraw())

    '''
    total = 0 
    tmp = 0
    withDraw = False

    A) identify states:
    total: either 0 or !=0 (2)
    tmp: either 0, 0<tmp<2, tmp=2, tmp>2 (4)
    withDraw: true, false (2)

    B)
    "positive states"
    1) start        S1: total=0, tmp=0, withDraw=false
    2) add50c       S1->S2: total=0, tmp=1, withDraw=false
    3) add50c       S2->S3: total=0, tmp=2, withDraw=true

    (2*4*2)=16 states, total is neglectable
    => (4*2)=8 states
    => 5 negative states

    4) S4: tmp=0, withDraw=true
    5) S5: tmp=1, withDraw=true, unreachable
    6) S6: tmp=2, withDraw=false, unreachable
    7) S7: tmp=3, withDraw=true
    8) S8: tmp=3, withDraw=false, unreachable

    Are there transitions resulting in S4-S8?
    
    return50cs      S3->S4  soda free
    add50c          S3->S7  pay to much
   
    => two mistakes

    State Diagram:
    S1->S1            reset
    S1->S2            add50c
        S2->S1        return50cs
        S2->S3        add50c
        S3->S1        draw
        S3->S4        return50cs !!!
            S4->S1    draw       !!!
        S3->S7        add50c     !!!
            S7->S1    draw       !!!
            S7->S7    add50c
            S7->S1    return50cs
    '''

    def test_Return1E(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.return50cs()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_add150c(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.draw()
        sodaM.add50c()
        self.assertEqual(True, sodaM.canWithDraw())

    def test_add200c(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.draw()
        self.assertEqual(True, sodaM.canWithDraw())

if __name__ == '__main__':
    unittest.main()
