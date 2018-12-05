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


if __name__ == '__main__':
    unittest.main()
