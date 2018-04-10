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

organizeViewsButton = Button(menuFrame, text="Organize Views")
organizeViewsButton.pack(side=LEFT, padx=5, pady=5, fill=X, expand=1)

openPcapButton = Button(menuFrame, text="Open PCAP")
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
randomButton = Button(paletteConstructFrame, text="Field", command=openFieldWindow)
randomButton.grid(row=0, column=0, sticky="ew")
randomButton2 = Button(paletteConstructFrame, text="Field", command=openFieldWindow)
randomButton2.grid(row=0, column=1, sticky="ew")

paletteFieldFrame = Frame(paletteFrame)
paletteFieldFrame.grid(row=0, column=0, sticky="nsew")
paletteFieldFrame.grid_columnconfigure(0, weight=1)
paletteFieldFrame.grid_columnconfigure(1, weight=1)
startFieldButton = Button(paletteFieldFrame, text="Start Field", command=openStartField)
startFieldButton.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
field1ByteButton = Button(paletteFieldFrame, text="Field(1 byte)", command=openFieldWindow)
field1ByteButton.grid(row=0, column=1, sticky="ew", padx=5, pady=10)
field2ByteButton = Button(paletteFieldFrame, text="Field(2 byte)", command=openFieldWindow)
field2ByteButton.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
field4ByteButton = Button(paletteFieldFrame, text="Field(4 byte)", command=openFieldWindow)
field4ByteButton.grid(row=1, column=1, sticky="ew", padx=5, pady=10)
field8ByteButton = Button(paletteFieldFrame, text="Field(8 byte)", command=openFieldWindow)
field8ByteButton.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
field16ByteButton = Button(paletteFieldFrame, text="Field(16 byte)", command=openFieldWindow)
field16ByteButton.grid(row=2, column=1, sticky="ew", padx=5, pady=10)
fieldvarSizeButton = Button(paletteFieldFrame, text="Field(Var Size)", command=openFieldWindow)
fieldvarSizeButton.grid(row=3, column=0, sticky="ew", padx=5, pady=10)
endFieldButton = Button(paletteFieldFrame, text="End Field", command=openEndField)
endFieldButton.grid(row=3, column=1, sticky="ew", padx=5, pady=10)
referenceListButton = Button(paletteFieldFrame, text="Reference List", command=openReferenceList)
referenceListButton.grid(row=4, column=0, sticky="ew", padx=5, pady=10)
packetInfoButton = Button(paletteFieldFrame, text="Packet Info", command=openPacketInfo)
packetInfoButton.grid(row=4, column=1, sticky="ew", padx=5, pady=10)

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