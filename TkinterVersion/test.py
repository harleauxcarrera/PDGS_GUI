from Tkinter import *
import endField as endField
import fieldWindow as fieldWindow

root = Tk()
root.title("Testing Window")
root.geometry("200x200")


def openEndField():
    winEndField = endField.endFieldWindow(root)

def openFieldWindow():
    winField = fieldWindow.fieldWindow(root)

mainFrame = Frame(root)
mainFrame.pack()
fieldButton = Button(mainFrame, text="Open Field Window", command=openFieldWindow)
fieldButton.pack()
endFieldButton = Button(mainFrame, text="Open End Field Window", command=openEndField)
endFieldButton.pack()

root.mainloop()