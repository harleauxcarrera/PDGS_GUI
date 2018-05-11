from Tkinter import *
import tkFileDialog
import endField as endField
import fieldWindow as fieldWindow
import startField as startField
import packetInfo as packetInfo
import referenceList as referenceList
import projectNavigator as projectNavigator
import packetStreamArea as packetStreamArea
import dissectedStreamArea as dissectedStreamArea
import rawData as rawData
import consoleArea as consoleArea
import createProject as createProject
#import dndManager

class DragManager():

    def add_dragable(self, widget):
        self.draggedWidget = widget
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        button = Button(target, text="BUTTTTONNN", command=openFieldWindow)
        print("Dragged to x ",x," and y ",y)
        try:
            #target.create_rectangle(x-10-260, y-5-125, x+10-260, y+5-125, fill="blue")
            target.create_window(x-260, y-125, window=button)
            openFieldWindow()
        except:
            pass

root = Tk()
root.title("Protocol Dissector Generator System")
root.geometry("1000x800+0+0")

###############################################################
###System Functions###
###############################################################

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

def openCreateProject():
    winCreateProject = createProject.createProject(root)

def saveAsFile():
    saveName = tkFileDialog.asksaveasfilename(initialdir="/", title="Select Save Location",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

def openFile():
    openFileName = tkFileDialog.askdirectory()

def importProject():
    importFileName = tkFileDialog.askopenfilename(initialdir = "/",title = "Select File to Import",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

def exportProject():
    exportDirectory = tkFileDialog.askdirectory()

def raiseField():
    paletteFieldFrame.tkraise()

def raiseConstruct():
    paletteConstructFrame.tkraise()

def organizeViews():
    organizeWindow = Toplevel(root, width=200, height=200)
    organizeWindow.transient(root)
    organizeWindow.geometry("300x300")
    organizeWindow.title("Organize Views")
    organizeTitleFrame = Frame(organizeWindow)
    organizeTitleFrame.pack(side=TOP)
    organizeTitle = Label(organizeTitleFrame, text="Customize the views")
    organizeTitle.pack(fill=X)
    organizeViewsFrame = Frame(organizeWindow)
    organizeViewsFrame.pack(fill=X)
    organizeViewsFrame.grid_columnconfigure(0, weight=1)
    organizeViewsFrame.grid_columnconfigure(1, weight=1)
    organizeViewsFrame.grid_columnconfigure(2, weight=1)

    organizeViewsFrame.grid_rowconfigure(0, weight=1)
    projectNavRadioLabel = Label(organizeViewsFrame, text="Project Navigation")
    projectNavRadioLabel.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    projectNavRadioHideButton = Radiobutton(organizeViewsFrame, text="Hide", value=1, variable=1,
                                            command=navigatorWindow.withdraw)
    projectNavRadioHideButton.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    projectNavRadioShowButton = Radiobutton(organizeViewsFrame, text="Show", value=2, variable=1,
                                            command=navigatorWindow.deiconify)
    projectNavRadioShowButton.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

    organizeViewsFrame.grid_rowconfigure(1, weight=1)
    dissBuildAreaRadioLabel = Label(organizeViewsFrame, text="Dissector Building Area")
    dissBuildAreaRadioLabel.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    dissBuildAreaRadioHideButton = Radiobutton(organizeViewsFrame, text="Hide", value=1, variable=2,
                                               command=builderWindow.withdraw)
    dissBuildAreaRadioHideButton.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
    dissBuildAreaRadioShowButton = Radiobutton(organizeViewsFrame, text="Show", value=2, variable=2,
                                               command=builderWindow.deiconify)
    dissBuildAreaRadioShowButton.grid(row=1, column=2, sticky="ew", padx=5, pady=5)

    organizeViewsFrame.grid_rowconfigure(2, weight=1)
    paletteRadioLabel = Label(organizeViewsFrame, text="Palette")
    paletteRadioLabel.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    paletteRadioHideButton = Radiobutton(organizeViewsFrame, text="Hide", value=1, variable=3,
                                               command=paletteWindow.withdraw)
    paletteRadioHideButton.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
    paletteRadioShowButton = Radiobutton(organizeViewsFrame, text="Show", value=2, variable=3,
                                               command=paletteWindow.deiconify)
    paletteRadioShowButton.grid(row=2, column=2, sticky="ew", padx=5, pady=5)

    organizeViewsFrame.grid_rowconfigure(3, weight=1)
    packetStreamAreaRadioLabel = Label(organizeViewsFrame, text="Packet Stream Area")
    packetStreamAreaRadioLabel.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    packetStreamAreaRadioHideButton = Radiobutton(organizeViewsFrame, text="Hide", value=1, variable=4,
                                         command=packetStreamWindow.withdraw)
    packetStreamAreaRadioHideButton.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
    packetStreamAreaRadioShowButton = Radiobutton(organizeViewsFrame, text="Show", value=2, variable=4,
                                         command=packetStreamWindow.deiconify)
    packetStreamAreaRadioShowButton.grid(row=3, column=2, sticky="ew", padx=5, pady=5)

    organizeViewsFrame.grid_rowconfigure(4, weight=1)
    dissStreamAreaRadioLabel = Label(organizeViewsFrame, text="Dissected Stream Area")
    dissStreamAreaRadioLabel.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
    dissStreamAreaRadioHideButton = Radiobutton(organizeViewsFrame, text="Hide", value=1, variable=5,
                                                  command=dissectedStreamWindow.withdraw)
    dissStreamAreaRadioHideButton.grid(row=4, column=1, sticky="ew", padx=5, pady=5)
    dissStreamAreaRadioShowButton = Radiobutton(organizeViewsFrame, text="Show", value=2, variable=5,
                                                  command=dissectedStreamWindow.deiconify)
    dissStreamAreaRadioShowButton.grid(row=4, column=2, sticky="ew", padx=5, pady=5)

    organizeViewsFrame.grid_rowconfigure(5, weight=1)
    rawDataRadioLabel = Label(organizeViewsFrame, text="Raw Data Area")
    rawDataRadioLabel.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
    rawDataRadioHideButton = Radiobutton(organizeViewsFrame, text="Hide", value=1, variable=6,
                                                command=rawDataWindow.withdraw)
    rawDataRadioHideButton.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
    rawDataRadioShowButton = Radiobutton(organizeViewsFrame, text="Show", value=2, variable=6,
                                                command=rawDataWindow.deiconify)
    rawDataRadioShowButton.grid(row=5, column=2, sticky="ew", padx=5, pady=5)

    organizeViewsFrame.grid_rowconfigure(6, weight=1)
    consoleAreaRadioLabel = Label(organizeViewsFrame, text="Console Area")
    consoleAreaRadioLabel.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
    consoleAreaRadioHideButton = Radiobutton(organizeViewsFrame, text="Hide", value=1, variable=7,
                                         command=consoleWindow.withdraw)
    consoleAreaRadioHideButton.grid(row=6, column=1, sticky="ew", padx=5, pady=5)
    consoleAreaRadioShowButton = Radiobutton(organizeViewsFrame, text="Show", value=2, variable=7,
                                         command=consoleWindow.deiconify)
    consoleAreaRadioShowButton.grid(row=6, column=2, sticky="ew", padx=5, pady=5)

    organizeButtonFrame = Frame(organizeWindow)
    organizeButtonFrame.pack(fill=X)
    okButton = Button(organizeButtonFrame, text="Create", command=organizeWindow.withdraw)
    cancelButton = Button(organizeButtonFrame, text="Cancel", command=organizeWindow.destroy)
    cancelButton.pack(side=RIGHT)
    okButton.pack(side=RIGHT)

def openPcap():
    openPcapFile = tkFileDialog.askopenfilename(initialdir = "/",title = "Select PCAP to open",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

###############################################################
###Main Menu Button Area###
###############################################################

menuFrame = Frame(root)
menuFrame.pack(side=TOP, fill=X)

createProjectButton = Button(menuFrame, text="Create Project", command=openCreateProject)
createProjectButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

saveProjectButton = Button(menuFrame, text="Save Project", command=saveAsFile)
saveProjectButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

closeProjectButton = Button(menuFrame, text="Close Project", command=root.destroy)
closeProjectButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

switchWorkspaceButton = Button(menuFrame, text="Switch Workspace", command=openFile)
switchWorkspaceButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

importProjectButton = Button(menuFrame, text="Import Project", command=importProject)
importProjectButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

exportProjectButton = Button(menuFrame, text="Export Project", command=exportProject)
exportProjectButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

generateScriptButton = Button(menuFrame, text="Generate Dissector Script")
generateScriptButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

organizeViewsButton = Button(menuFrame, text="Organize Views", command=organizeViews)
organizeViewsButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

openPcapButton = Button(menuFrame, text="Open PCAP", command=openPcap)
openPcapButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

###############################################################
###Project Navigator Window###
###############################################################

navigatorWindow = projectNavigator.projectNavigator(root)
navigatorWindow.transient(root)
navigatorWindow.geometry("%dx%d+%d+%d" % (navigatorWindow.winfo_reqwidth(), navigatorWindow.winfo_reqheight(), root.winfo_x() + 20, root.winfo_y() +70))

###############################################################
###Dissector Builder Area Canvas###
###############################################################

builderWindow = Toplevel(width=750, height=500)
builderWindow.title("Dissector Builder Area")
builderWindow.transient(root)
builderWindow.geometry("%dx%d+%d+%d" % (builderWindow.winfo_reqwidth(), builderWindow.winfo_reqheight(), root.winfo_x() + 230, root.winfo_y() + 70))
builderFrame = Frame(builderWindow)
builderFrame.pack(padx=20, pady=20, side=LEFT)
builderCanvas = Canvas(builderFrame, width=500, height=450, bg="WHITE")
builderCanvas.pack()
dnd = DragManager()

###############################################################
###Dissector Builder Area Palette###
###############################################################

paletteWindow = Toplevel(width=200, height=450)
paletteWindow.title("Palette")
paletteWindow.transient(builderWindow)
paletteWindow.geometry("%dx%d+%d+%d" % (paletteWindow.winfo_reqwidth(), paletteWindow.winfo_reqheight(), root.winfo_x() + 770, root.winfo_y() + 110))
switchFrame = Frame(paletteWindow, bg="GRAY")
switchFrame.pack(side=TOP, fill=X)
fieldsButton = Button(switchFrame, text="Field", command=raiseField)
fieldsButton.pack(side=LEFT, fill=X, expand=1, pady=5, padx=5)
constructsButton = Button(switchFrame, text="Construct", command=raiseConstruct)
constructsButton.pack(side=LEFT, fill=X, expand=1, pady=5, padx=5)

paletteFrame = Frame(paletteWindow)
paletteFrame.pack(fill=BOTH, expand=1)
paletteFrame.grid_columnconfigure(0, weight=1)
paletteFrame.grid_rowconfigure(0, weight=1)

paletteConstructFrame = Frame(paletteFrame)
paletteConstructFrame.grid(row=0, column=0, sticky="nsew")
paletteConstructFrame.grid_columnconfigure(0, weight=1)
paletteConstructFrame.grid_columnconfigure(1, weight=1)

expressionButton = Button(paletteConstructFrame, text="Expression")
expressionButton.grid(row=0, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
dnd.add_dragable(expressionButton)
connectorButton = Button(paletteConstructFrame, text="Connector")
connectorButton.grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
dnd.add_dragable(connectorButton)

relationalFrame = Frame(paletteConstructFrame)
relationalFrame.grid(row=2, column=0, columnspan=2, sticky="ew")
relationalFrame.grid_columnconfigure(0, weight=1)
relationalFrame.grid_columnconfigure(1, weight=1)
relationalFrame.grid_columnconfigure(2, weight=1)
relationalFrame.grid_columnconfigure(3, weight=1)
relationalFrame.grid_columnconfigure(4, weight=1)
relationalFrame.grid_columnconfigure(5, weight=1)
lessThanButton = Button(relationalFrame, text="<")
lessThanButton.grid(row=0, column=0, sticky="ew", padx=1, pady=5)
dnd.add_dragable(lessThanButton)
greaterThanButton = Button(relationalFrame, text=">")
greaterThanButton.grid(row=0, column=1, sticky="ew", padx=1, pady=5)
dnd.add_dragable(greaterThanButton)
lessThanEqualButton = Button(relationalFrame, text="<=")
lessThanEqualButton.grid(row=0, column=2, sticky="ew", padx=1, pady=5)
dnd.add_dragable(lessThanEqualButton)
greaterThanEqualButton = Button(relationalFrame, text=">=")
greaterThanEqualButton.grid(row=0, column=3, sticky="ew", padx=1, pady=5)
dnd.add_dragable(greaterThanEqualButton)
equalButton = Button(relationalFrame, text="==")
equalButton.grid(row=0, column=4, sticky="ew", padx=1, pady=5)
dnd.add_dragable(equalButton)
notEqualButton = Button(relationalFrame, text="~=")
notEqualButton.grid(row=0, column=5, sticky="ew", padx=1, pady=5)
dnd.add_dragable(notEqualButton)

logicalFrame = Frame(paletteConstructFrame)
logicalFrame.grid(row=3, column=0, columnspan=2, sticky="ew")
logicalFrame.grid_columnconfigure(0, weight=1)
logicalFrame.grid_columnconfigure(1, weight=1)
logicalFrame.grid_columnconfigure(2, weight=1)
andButton = Button(logicalFrame, text="And")
andButton.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
dnd.add_dragable(andButton)
orButton = Button(logicalFrame, text="Or")
orButton.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
dnd.add_dragable(orButton)
notButton = Button(logicalFrame, text="Not")
notButton.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
dnd.add_dragable(notButton)
operandButton = Button(paletteConstructFrame, text="Operand")
operandButton.grid(row=4, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

paletteFieldFrame = Frame(paletteFrame)
paletteFieldFrame.grid(row=0, column=0, sticky="nsew")
paletteFieldFrame.grid_columnconfigure(0, weight=1)
paletteFieldFrame.grid_columnconfigure(1, weight=1)

startFieldButton = Button(paletteFieldFrame, text="Start Field", command=openStartField)
startFieldButton.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
dnd.add_dragable(startFieldButton)
field1ByteButton = Button(paletteFieldFrame, text="Field(1 byte)", command=openFieldWindow)
field1ByteButton.grid(row=0, column=1, sticky="ew", padx=5, pady=10)
dnd.add_dragable(field1ByteButton)
field2ByteButton = Button(paletteFieldFrame, text="Field(2 byte)", command=openFieldWindow)
field2ByteButton.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
dnd.add_dragable(field2ByteButton)
field4ByteButton = Button(paletteFieldFrame, text="Field(4 byte)", command=openFieldWindow)
field4ByteButton.grid(row=1, column=1, sticky="ew", padx=5, pady=10)
dnd.add_dragable(field4ByteButton)
field8ByteButton = Button(paletteFieldFrame, text="Field(8 byte)", command=openFieldWindow)
field8ByteButton.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
dnd.add_dragable(field8ByteButton)
field16ByteButton = Button(paletteFieldFrame, text="Field(16 byte)", command=openFieldWindow)
field16ByteButton.grid(row=2, column=1, sticky="ew", padx=5, pady=10)
dnd.add_dragable(field16ByteButton)
fieldvarSizeButton = Button(paletteFieldFrame, text="Field(Var Size)", command=openFieldWindow)
fieldvarSizeButton.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
dnd.add_dragable(fieldvarSizeButton)
endFieldButton = Button(paletteFieldFrame, text="End Field", command=openEndField)
endFieldButton.grid(row=3, column=1, sticky="ew", padx=5, pady=10)
dnd.add_dragable(endFieldButton)
referenceListButton = Button(paletteFieldFrame, text="Reference List", command=openReferenceList)
referenceListButton.grid(row=4, column=0, sticky="ew", padx=5, pady=10)
dnd.add_dragable(referenceListButton)
packetInfoButton = Button(paletteFieldFrame, text="Packet Info", command=openPacketInfo)
packetInfoButton.grid(row=4, column=1, sticky="ew", padx=5, pady=10)
dnd.add_dragable(packetInfoButton)

###############################################################
###Packet Stream Area###
###############################################################

packetStreamWindow = packetStreamArea.packetStreamArea(root)
packetStreamWindow.title("Packet Stream Area")
packetStreamWindow.transient(root)
packetStreamWindow.geometry("%dx%d+%d+%d" % (packetStreamWindow.winfo_reqwidth(), packetStreamWindow.winfo_reqheight(), root.winfo_x() + 230, root.winfo_y() + 610))

###############################################################
###Dissected Stream Area###
###############################################################

dissectedStreamWindow = dissectedStreamArea.dissectedStreamArea(root)
dissectedStreamWindow.title("Dissected Stream Area")
dissectedStreamWindow.transient(root)
dissectedStreamWindow.geometry("%dx%d+%d+%d" % (dissectedStreamWindow.winfo_reqwidth(), dissectedStreamWindow.winfo_reqheight(), root.winfo_x() + 420, root.winfo_y() + 610))

###############################################################
###Raw Data Area###
###############################################################

rawDataWindow = rawData.rawData(root)
rawDataWindow.title("Raw Data Area")
rawDataWindow.transient(root)
rawDataWindow.geometry("%dx%d+%d+%d" % (rawDataWindow.winfo_reqwidth(), rawDataWindow.winfo_reqheight(), root.winfo_x() + 610, root.winfo_y() + 610))

###############################################################
###Console Area###
###############################################################

consoleWindow = consoleArea.consoleArea(root)
consoleWindow.title("Console Area")
consoleWindow.transient(root)
consoleWindow.geometry("%dx%d+%d+%d" % (consoleWindow.winfo_reqwidth(), consoleWindow.winfo_reqheight(), root.winfo_x() + 800, root.winfo_y() + 610))



root.mainloop()