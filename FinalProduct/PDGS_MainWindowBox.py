import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import createProject as createProjectWindow
import switchWorkspace as switchWorkspaceWindow
import importProject as importProjectWindow
import exportProject as exportProjectWindow
import generateDissectorScript as generateDissectorScriptWindow
import organizeViews as organizeViewsWindow
import openPCAP as openPCAPWindow
import BuilderAreaBox as BuilderAreaBox
import console as console

class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Protocol Dissector Generator System")
		self.set_default_size(1300, 700)

		# Main Box
		box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)
		self.add(box)

		#LabelBox
		labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0)
		labelBox.set_homogeneous(False)

		#ButtonsBox
		buttonBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0)
		buttonBox.set_homogeneous(False)

		#Project/Dissector Box
		#projectDissectorBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0)
		#projectDissectorBox.set_homogeneous(False)
		projectDissectorGrid = Gtk.Grid()
		

		#Project Navigator Box
		projectNavigatorBox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 0)
		projectNavigatorBox.set_size_request(200, 400)
		projectNavigatorBox.set_homogeneous(False)

		#Dissector Builder Area Box
		dissectorBuilderAreaBox = BuilderAreaBox.BuilderWindow()
		dissectorBuilderAreaBox.set_size_request(1100, 200)
		dissectorBuilderAreaBox.set_homogeneous(False)

		#projectDissectorBox.pack_start(projectNavigatorBox, True, True, 5)
		#projectDissectorBox.pack_start(dissectorBuilderAreaBox, True, True, 5)
		projectDissectorGrid.add(projectNavigatorBox)
		projectDissectorGrid.attach_next_to(dissectorBuilderAreaBox, projectNavigatorBox, Gtk.PositionType.RIGHT, 1, 1)

		#PacketPreviewAreaBox
		#packetPreviewAreaBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 0)
		packetPreviewAreaBox = console.ConsoleAreaWindow()
		packetPreviewAreaBox.set_size_request(1300, 100)
		packetPreviewAreaBox.set_homogeneous(True)

		box.pack_start(labelBox, True, False, 5)
		box.pack_start(buttonBox, True, False, 5)
		#box.pack_start(projectDissectorBox, True, True, 5)
		box.pack_start(projectDissectorGrid, True, True, 5)
		box.pack_start(packetPreviewAreaBox, True, True, 5)

		# Label
		PDGSLabel = Gtk.Label()
		PDGSLabel.set_markup("<span color = 'orange'><b><big>Protocol Dissector Generator System</big></b></span>")
		PDGSLabel.set_justify(Gtk.Justification.LEFT)
		labelBox.pack_start(PDGSLabel, True, True, 0)

		#Create Project Button
		CreateProjectButton = Gtk.Button(label = "Create Project")
		CreateProjectButton.connect("clicked", self.CreateProjectButton_clicked)
		buttonBox.pack_start(CreateProjectButton, True, True, 5)

		#Save Project Button
		SaveProjectButton = Gtk.Button(label = "Save Project")
		SaveProjectButton.connect("clicked", self.SaveProjectButton_clicked)
		buttonBox.pack_start(SaveProjectButton, True, True, 5)

		#Close Project Button
		CloseProjectButton = Gtk.Button(label = "Close Project")
		CloseProjectButton.connect("clicked", self.CloseProjectButton_clicked)
		buttonBox.pack_start(CloseProjectButton, True, True, 5)

		#Switch Workspace Button
		SwitchWorkspaceButton = Gtk.Button(label = "Switch Workspace")
		SwitchWorkspaceButton.connect("clicked", self.SwitchWorkspaceButton_clicked)
		buttonBox.pack_start(SwitchWorkspaceButton, True, True, 5)

		#Import Project Button
		ImportProjectButton = Gtk.Button(label = "Import Project")
		ImportProjectButton.connect("clicked", self.ImportProjectButton_clicked)
		buttonBox.pack_start(ImportProjectButton, True, True, 5)

		#Export Project Button
		ExportProjectButton = Gtk.Button(label = "Export Project")
		ExportProjectButton.connect("clicked", self.ExportProjectButton_clicked)
		buttonBox.pack_start(ExportProjectButton, True, True, 5)

		#Generate Dissector Script Button
		GenerateDissectorScriptButton = Gtk.Button(label="Generate Dissector Script")
		GenerateDissectorScriptButton.connect("clicked", self.GenerateDissectorScriptButton_clicked)
		buttonBox.pack_start(GenerateDissectorScriptButton, True, True, 5)

		#Organize Views Button
		OrganizeViewsButton = Gtk.Button(label="Organize Views")
		OrganizeViewsButton.connect("clicked", self.OrganizeViewsButton_clicked)
		buttonBox.pack_start(OrganizeViewsButton, True, True, 5)

		#Open PCAP Button
		OpenPCAPButton = Gtk.Button(label="Open PCAP")
		OpenPCAPButton.connect("clicked", self.OpenPCAPButton_clicked)
		buttonBox.pack_start(OpenPCAPButton, True, True, 5)


		#************************************************Project Navigator Area**************************************************
		store = Gtk.TreeStore(str)

		row1 = store.append(None, ['ProjectA'])
		store.append(row1, ['dissectorA1'])

		row2 = store.append(None, ['Project B'])
		store.append(row2, ['dissectorB1'])

		row2 = store.append(None, ['Project C'])
		store.append(row2, ['dissectorC1'])

		treeView = Gtk.TreeView(store)
		treeViewColumn = Gtk.TreeViewColumn('Project Navigator')
		treeView.append_column(treeViewColumn)

		cell = Gtk.CellRendererText()
		treeViewColumn.pack_start(cell, True)
		treeViewColumn.add_attribute(cell, 'text', 0)
		projectNavigatorBox.pack_start(treeView, True, True, 5)



		#***********************************************Dissector Builder Area**************************************************

		#dissectorBuilderAreaBox = BuilderAreaBox.BuilderWindow()

		#*************************************************Packet Preview Area***************************************************
		
		#previewAreas = Gtk.Notebook()
		#packetPreviewAreaBox.pack_start(previewAreas, True, True, 5)

		#packetStreamBox = Gtk.Box(spacing = 5)
		#packetStreamBox.set_homogeneous(False)
		#packetStreamBox.set_border_width(5)
		#packetStreamBox.add(Gtk.Label('Test'))
		#previewAreas.append_page(packetStreamBox, Gtk.Label('Packet Stream Area View'))

		#dissectedStreamBox = Gtk.Box(spacing = 5)
		#dissectedStreamBox.set_homogeneous(False)
		#dissectedStreamBox.set_border_width(5)
		#dissectedStreamBox.add(Gtk.Label('Test'))
		#previewAreas.append_page(dissectedStreamBox, Gtk.Label('Dissected Stream Area View'))

		#rawDataBox = Gtk.Box(spacing = 5)
		#rawDataBox.set_homogeneous(False)
		#rawDataBox.set_border_width(5)
		#rawDataBox.add(Gtk.Label('Test'))
		#previewAreas.append_page(rawDataBox, Gtk.Label('Raw Data Area'))

		#consoleBox = Gtk.Box(spacing = 5)
		#consoleBox.set_homogeneous(False)
		#consoleBox.set_border_width(5)
		#consoleBox.add(Gtk.Label('Test'))
		#previewAreas.append_page(consoleBox, Gtk.Label('Console Area'))


	#User clicks CreateProjectButton
	def CreateProjectButton_clicked(self, button):
		print("Create Project")
		#button action
		win = createProjectWindow.CreateProject()
		win.connect("destroy", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	#User clicks SaveProjectButton
	def SaveProjectButton_clicked(self, button):
		print("Save Project")

	#User clicks CloseProjectButton
	def CloseProjectButton_clicked(self, button):
		print("Close Project")

	#User clicks SwitchWorkspaceButton
	def SwitchWorkspaceButton_clicked(self, button):
		print("Switch Workspace")
		#button action
		win = switchWorkspaceWindow.SwitchWorkspace()
		win.connect("destroy", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	#User clicks ImportProjectButton
	def ImportProjectButton_clicked(self, button):
		print("Import Project")
		#button action
		win = importProjectWindow.ImportProject()
		win.connect("destroy", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	#User clicks ExportProjectButton
	def ExportProjectButton_clicked(self, button):
		print("Export Project")
		#button action
		win = exportProjectWindow.ExportProject()
		win.connect("destroy", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	#User clicks GenerateDissectorScriptButton
	def GenerateDissectorScriptButton_clicked(self, button):
		print("Generate Dissector Script")
		#button action
		win = generateDissectorScriptWindow.GenerateDissectorScript()
		win.connect("destroy", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	#User clicks Organize Views Button
	def OrganizeViewsButton_clicked(self, button):
		print("Organize Views")
		#button action
		win = organizeViewsWindow.OrganizeViews()
		win.connect("destroy", Gtk.main_quit)
		win.show_all()
		Gtk.main()

	#User clicks Organize Views Button
	def OpenPCAPButton_clicked(self, button):
		print("Open PCAP")
		#button action
		win = openPCAPWindow.OpenPCAP()
		win.connect("destroy", Gtk.main_quit)
		win.show_all()
		Gtk.main()

window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()