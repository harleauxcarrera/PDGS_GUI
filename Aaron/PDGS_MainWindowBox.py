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

class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Protocol Dissector Generator System")

		# Main Box
		box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
		self.add(box)

		#LabelBox
		labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		labelBox.set_homogeneous(False)

		#ButtonsBox
		buttonBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		buttonBox.set_homogeneous(False)

		box.pack_start(labelBox, True, True, 5)
		box.pack_start(buttonBox, True, True, 5)

		# Label
		PDGSLabel = Gtk.Label()
		PDGSLabel.set_markup("<span color = 'orange'><b><big>Protocol Dissector Generator System</big></b></span>")
		PDGSLabel.set_justify(Gtk.Justification.LEFT)
		labelBox.pack_start(PDGSLabel, True, True, 0)

		#Create Project Button
		CreateProjectButton = Gtk.Button(label="Create Project")
		CreateProjectButton.connect("clicked", self.CreateProjectButton_clicked)
		buttonBox.pack_start(CreateProjectButton, True, True, 5)

		#Save Project Button
		SaveProjectButton = Gtk.Button(label="Save Project")
		SaveProjectButton.connect("clicked", self.SaveProjectButton_clicked)
		buttonBox.pack_start(SaveProjectButton, True, True, 0)

		#Close Project Button
		CloseProjectButton = Gtk.Button(label="Close Project")
		CloseProjectButton.connect("clicked", self.CloseProjectButton_clicked)
		buttonBox.pack_start(CloseProjectButton, True, True, 0)

		#Switch Workspace Button
		SwitchWorkspaceButton = Gtk.Button(label="Switch Workspace")
		SwitchWorkspaceButton.connect("clicked", self.SwitchWorkspaceButton_clicked)
		buttonBox.pack_start(SwitchWorkspaceButton, True, True, 0)

		#Import Project Button
		ImportProjectButton = Gtk.Button(label="Import Project")
		ImportProjectButton.connect("clicked", self.ImportProjectButton_clicked)
		buttonBox.pack_start(ImportProjectButton, True, True, 0)

		#Export Project Button
		ExportProjectButton = Gtk.Button(label="Export Project")
		ExportProjectButton.connect("clicked", self.ExportProjectButton_clicked)
		buttonBox.pack_start(ExportProjectButton, True, True, 0)

		#Generate Dissector Script Button
		GenerateDissectorScriptButton = Gtk.Button(label="Generate Dissector Script")
		GenerateDissectorScriptButton.connect("clicked", self.GenerateDissectorScriptButton_clicked)
		buttonBox.pack_start(GenerateDissectorScriptButton, True, True, 0)

		#Organize Views Button
		OrganizeViewsButton = Gtk.Button(label="Organize Views")
		OrganizeViewsButton.connect("clicked", self.OrganizeViewsButton_clicked)
		buttonBox.pack_start(OrganizeViewsButton, True, True, 0)

		#Open PCAP Button
		OpenPCAPButton = Gtk.Button(label="Open PCAP")
		OpenPCAPButton.connect("clicked", self.OpenPCAPButton_clicked)
		buttonBox.pack_start(OpenPCAPButton, True, True, 0)


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
		win.show_all()
		Gtk.main()

	#User clicks ExportProjectButton
	def ExportProjectButton_clicked(self, button):
		print("Export Project")
		#button action
		win = exportProjectWindow.ExportProject()
		win.show_all()
		Gtk.main()

	#User clicks GenerateDissectorScriptButton
	def GenerateDissectorScriptButton_clicked(self, button):
		print("Generate Dissector Script")
		#button action
		win = generateDissectorScriptWindow.GenerateDissectorScript()
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