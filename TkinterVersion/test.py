from Tkinter import *
import endField as endField
import fieldWindow as fieldWindow
import startField as startField
import packetInfo as packetInfo
import referenceList as referenceList

root = Tk()
root.title("Testing Window")
root.geometry("400x400")


def openEndField():
    winEndField = endField.endFieldWindow(root)

def openFieldWindow():
    winField = fieldWindow.fieldWindow(root)

def openStartField():
    winStartField = startField.startFieldWindow(root)

def openPacketInfo():
    winPacketInfo = packetInfo.packetInfoWindow(root)

def openReferenceList():
    winReferenceList = referenceList.referenceListWindow(root)

mainFrame = Frame(root)
mainFrame.pack()
fieldButton = Button(mainFrame, text="Open Field Window", command=openFieldWindow)
fieldButton.pack()
startFieldButton = Button(mainFrame, text="Open Start Field Window", command=openStartField)
startFieldButton.pack()
endFieldButton = Button(mainFrame, text="Open End Field Window", command=openEndField)
endFieldButton.pack()
packetInfoButton = Button(mainFrame, text="Open Packet Info Window", command=openPacketInfo)
packetInfoButton.pack()
referenceListButton = Button(mainFrame, text="Open Reference List Window", command=openReferenceList)
referenceListButton.pack()

root.mainloop()