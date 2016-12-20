from tkinter import *
import CharacterCounterLogic as makePiechart

def buttonClicked():
    global numOfSlices
    makePiechart.drawPieChart('Words.txt', numOfSlices.get())

root = Tk()
root.wm_title("Character Counter v1.0")
numOfSlices = IntVar()

titleFrame = Frame (root)
lblWidget = Label (titleFrame, text = "Character Counter v1.0")
lblWidget.pack (side = TOP, fill = BOTH)
titleFrame.pack(fill = X, padx = 3)

numOfSlicesFrame = Frame (root)
lblSlicesNumber = Label (numOfSlicesFrame, text = "# of Slices:", width = 15, anchor = W)
lblSlicesNumber.pack (side = LEFT)
txtnumOfSlices = Entry(numOfSlicesFrame, width = 5, textvariable = numOfSlices).pack(side = LEFT)
lblSlicesInfo = Label(numOfSlicesFrame, text="Limit to 20", width = 15)
lblSlicesInfo.pack(side=LEFT)
numOfSlicesFrame.pack(fill = X, padx = 3)

executeButton = Button(root, text = "Execute", width = 10, command = buttonClicked)
executeButton.pack (side = RIGHT, anchor = SE, padx = 6)
root.mainloop()