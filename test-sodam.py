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

    # test each method
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

    # Object state transitions tests
    def test_Return1E(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.return50cs()
        self.assertEqual(False, sodaM.canWithDraw())

    def test_add1E_d1E(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.draw()
        sodaM.add50c()
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

    # Combinatorial tests draw()
    def test_comb1(self):
        sodaM = SodaMachine()
        self.assertEqual(False, sodaM.draw(False, False, False, False))

    def test_comb2(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.draw(False, False, False, True))

    def test_comb3(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.draw(True, False, False, False))

    def test_comb4(self):
        sodaM = SodaMachine()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        sodaM.add50c()
        self.assertEqual(True, sodaM.draw(True, False, False, True))

    '''
    Elementary comparison tests service()
    T1: 1110 total=39, cumulate=40, mut=40, tmp=0  => code 3
    T2: 0110 total=40, cumulate=40, mut=40, tmp=0  => code 2
    T3: 1001 total=0, cumulate=38, mut=38, tmp=21 => code 3
    T4: 1101 total=38, cumulate=39, mut=39, tmp=21  => code 3
    T5: 1000 total=38,  cumulate=39, mut=39, tmp=0  => code 1
    '''
    def test_service_ect1(self):
        sodaM = SodaMachine()
        for i in range(0, 40):
            sodaM.add50c()
            sodaM.draw(False, True, False, False)
        sodaM.setTotal(39)
        self.assertEqual(3, sodaM.service())

    def test_service_ect2(self):
        sodaM = SodaMachine()
        for i in range(0, 40):
            sodaM.add50c()
            sodaM.draw(False, True, False, False)
        self.assertEqual(2, sodaM.service())

    def test_service_ect3(self):
        sodaM = SodaMachine()
        for i in range(0, 38):
            sodaM.add50c()
            sodaM.draw(False, True, False, False)
        sodaM.setTotal(0)
        sodaM.setTmp(21)
        self.assertEqual(3, sodaM.service())

    def test_service_ect4(self):
        sodaM = SodaMachine()
        for i in range(0, 39):
            sodaM.add50c()
            sodaM.draw(False, True, False, False)
        sodaM.setTotal(38)
        sodaM.setTmp(21)
        self.assertEqual(3, sodaM.service())

    def test_service_ect5(self):
        sodaM = SodaMachine()
        for i in range(0, 39):
            sodaM.add50c()
            sodaM.draw(False, True, False, False)
        sodaM.setTotal(0)
        self.assertEqual(1, sodaM.service())

if __name__ == '__main__':
    unittest.main()
