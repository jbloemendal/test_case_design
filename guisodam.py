#!/anaconda/bin/python 1

from tkinter import *
from feenet import FeeNetModul
from sodam import *

'''
Copyright 2018 Jannis Bloemendal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

On Object State Testing (Adaptation in Python)
D.C. Kunk, N. Suchak, J. Gao, P. Hsia
https://pdfs.semanticscholar.org/c099/37b9d87cf8020fc897b882c412229f5a7c68.pdf
'''

class GuiSoda(Frame):

    forrader = None

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

    def setlui(self, lint):
        self.forrader = lint

    def add50c(self):
        self.forrader.add50c()
        if self.forrader.canWithDraw():
            self.pull.config(state='normal')

    def return50c(self):
        self.forrader.return50cs()
        if not self.forrader.canWithDraw():
            self.pull.config(state='disabled')
       
    def draw(self):
        self.forrader.draw()
        if not self.forrader.canWithDraw():
            self.pull.config(state='disabled')

    def createWidgets(self):
        self.fare = Button(self, padx='20', pady='20')
        self.fare["text"] = "add50c"
        self.fare["fg"]   = "red"
        self.fare["command"] =  self.add50c
        self.fare.grid(column=1,row=1)

        self.return50cs = Button(self, padx='20', pady='20')
        self.return50cs["text"] = "return"
        self.return50cs["fg"]   = "red"
        self.return50cs["command"] = self.return50cs
        self.return50cs.grid(column=2,row=1)

        self.pull = Button(self, text="draw", padx='20', pady='20')
        self.pull.config(state='disabled')
        self.pull["command"] =  self.draw
        self.pull.grid(column=2,row=3)

        self.fare.pack({"side": "left"})
        self.return50cs.pack({"side": "left"})
        self.pull.pack({"side": "right"})

if __name__ == '__main__':
    root = Tk()
    root.title("SodaMachine")
    root.geometry("600x500")

    gui = GuiSoda(master=root)
    sodam = SodaMachine()
    gui.setlui(sodam)
    gui.createWidgets()
    gui.mainloop() # start
