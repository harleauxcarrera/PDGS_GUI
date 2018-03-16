import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Protocol Dissector Generator System")

		# Box
		self.box = Gtk.Box(spacing = 5)
		PDGSLabel = Gtk.Box(spacing = 10)

		self.box.pack_start(PDGSLabel, True, True, 0)

		label = Gtk.Label()
		label.set_markup("<big>Protocol Dissector Generator System</big>")
		PDGSLabel.pack_start(label, True, True, 0)

		#Create Project Button
		self.CreateProjectButton = Gtk.Button(label="Create Project")
		self.CreateProjectButton.connect("clicked", self.CreateProjectButton_clicked)
		self.box.pack_start(self.CreateProjectButton, True, True, 0)

		#Save Project Button
		self.SaveProjectButton = Gtk.Button(label="Save Project")
		self.SaveProjectButton.connect("clicked", self.SaveProjectButton_clicked)
		self.box.pack_start(self.SaveProjectButton, True, True, 0)

		#Close Project Button
		self.CloseProjectButton = Gtk.Button(label="Close Project")
		self.CloseProjectButton.connect("clicked", self.CloseProjectButton_clicked)
		self.box.pack_start(self.CloseProjectButton, True, True, 0)

		#Switch Workspace Button
		self.SwitchWorkspaceButton = Gtk.Button(label="Switch Workspace")
		self.SwitchWorkspaceButton.connect("clicked", self.SwitchWorkspaceButton_clicked)
		self.box.pack_start(self.SwitchWorkspaceButton, True, True, 0)

		#Import Project Button
		self.ImportProjectButton = Gtk.Button(label="Import Project")
		self.ImportProjectButton.connect("clicked", self.ImportProjectButton_clicked)
		self.box.pack_start(self.ImportProjectButton, True, True, 0)

		#Export Project Button
		self.ExportProjectButton = Gtk.Button(label="Export Project")
		self.ExportProjectButton.connect("clicked", self.ExportProjectButton_clicked)
		self.box.pack_start(self.ExportProjectButton, True, True, 0)

		#Generate Dissector Script Button
		self.GenerateDissectorScriptButton = Gtk.Button(label="Generate Dissector Script")
		self.GenerateDissectorScriptButton.connect("clicked", self.GenerateDissectorScriptButton_clicked)
		self.box.pack_start(self.GenerateDissectorScriptButton, True, True, 0)

		#Organize Views Button
		self.OrganizeViewsButton = Gtk.Button(label="Organize Views")
		self.OrganizeViewsButton.connect("clicked", self.OrganizeViewsButton_clicked)
		self.box.pack_start(self.OrganizeViewsButton, True, True, 0)

		#Open PCAP Button
		self.OpenPCAPButton = Gtk.Button(label="Open PCAP")
		self.OrganizeViewsButton.connect("clicked", self.OpenPCAPButton_clicked)
		self.box.pack_start(self.OpenPCAPButton, True, True, 0)

		self.add(self.box)


	#User clicks CreateProjectButton
	def CreateProjectButton_clicked(self, widget):
		print("Create Project")

	#User clicks SaveProjectButton
	def SaveProjectButton_clicked(self, widget):
		print("Save Project")

	#User clicks CloseProjectButton
	def CloseProjectButton_clicked(self, widget):
		print("Close Project")

	#User clicks SwitchWorkspaceButton
	def SwitchWorkspaceButton_clicked(self, widget):
		print("Switch Workspace")

	#User clicks ImportProjectButton
	def ImportProjectButton_clicked(self, widget):
		print("Import Project")

	#User clicks ExportProjectButton
	def ExportProjectButton_clicked(self, widget):
		print("Export Project")

	#User clicks GenerateDissectorScriptButton
	def GenerateDissectorScriptButton_clicked(self, widget):
		print("Generate Dissector Script")

	#User clicks Organize Views Button
	def OrganizeViewsButton_clicked(self, widget):
		print("Organize Views")

	#User clicks Organize Views Button
	def OpenPCAPButton_clicked(self, widget):
		print("Open PCAP")

window = MainWindow()
window.set_default_size(1000, 700)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()