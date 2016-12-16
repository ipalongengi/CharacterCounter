from tkinter import *
from tkinter.filedialog import askopenfilename

class WidgetLabel(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        lblWidget = Label (self, text = "CharacterCounter v1.0")
        lblWidget.pack (side = TOP, fill = BOTH)

class FileFinder(Frame):
    def __init__ (self, parent):
        Frame.__init__(self, parent)
        self.dirname = ""
        self.lblFileFinder = Label (self, text = "File Name:", width = 15, anchor = W)
        self.lblFileFinder.pack (side = LEFT)
        Entry(self).pack(side = LEFT)
        self.btnFileFinder = Button (self, text = "Browse", width = 10, command = self.buttonClicked)
        self.btnFileFinder.pack (side = RIGHT, padx=3)

    def buttonClicked(self):
        self.dirname = askopenfilename(title="Select a text file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        print(self.dirname)

class SlicesNumber(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.lblSlicesNumber = Label (self, text = "# of Slices:", width = 15, anchor = W)
        self.lblSlicesNumber.pack (side = LEFT)
        Entry(self, width = 5).pack(side = LEFT)
        self.lblSlicesInfo = Label(self, text="Limit to 20", width = 15)
        self.lblSlicesInfo.pack(side=LEFT)


root = Tk()
root.wm_title("Character Counter v1.0")

title = WidgetLabel(root)
title.pack(fill = X, padx = 3)

blah = FileFinder (root)
blah.pack(fill = X, padx = 3)

zap = SlicesNumber (root)
zap.pack(fill = X, padx = 3)

Button(root, text = "Execute", width = 10).pack (side = RIGHT, anchor = SE, padx = 6)
root.mainloop()