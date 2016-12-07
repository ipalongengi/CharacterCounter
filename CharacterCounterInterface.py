from tkinter import *

class FileFinder(Frame):
    def __init__ (self, parent):
        Frame.__init__(self, parent)
        lblFileFinder = Label (self, text = "File Name:", width = 12, anchor = W)
        lblFileFinder.pack (side = LEFT, fill = X)
        btnFileFinder = Button (self, text = "Browse", width = 10)
        btnFileFinder.pack (side = RIGHT)
        Entry(self).pack(side = RIGHT, fill = X, expand=True)

class WidgetLabel(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        lblWidget = Label (self, text = "CharacterCounter 1000")
        lblWidget.pack (side = TOP, fill = BOTH)

class SlicesNumber(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        lblSlicesNumber = Label (self, text = "# of Slices:", width = 12, anchor = W)
        lblSlicesNumber.pack (side = LEFT, fill = X)
        Entry(self).pack(side = RIGHT, fill = X, expand = True)

root = Tk()
title = WidgetLabel(root)
title.pack(padx = 3)
blah = FileFinder (root)
blah.pack(padx = 3)
zap = SlicesNumber (root)
zap.pack(fill = X, expand = True, padx = 3)
Button(root, text = "Execute", width = 8).pack (side = RIGHT, anchor = SE)
root.mainloop()