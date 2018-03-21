import gi
import createProject as createProjectWindow
import projectImport as importProjectWindow
import workspaceLauncher as switchWorkspaceWindow
import views as organizeViewsWindows
import openPCAP as openPCAPWindow

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Protocol Dissector Generator System")

        grid = Gtk.Grid()
        self.add(grid)
        self.set_default_size(500,700)

        PDGSLabel = Gtk.Label()
        PDGSLabel.set_markup("\n<span color = 'orange'><b><big>	   Protocol Dissector Generator System</big></b></span>\n")

        CreateProjectButton = Gtk.Button(label="Create Project")
        #CreateProjectButton.set_property("-resquest", 85)
        SaveProjectButton = Gtk.Button(label="Save Project")
        CloseProjectButton = Gtk.Button(label="CloseProject")
        SwitchWorkspaceButton = Gtk.Button(label="Switch Workspace")
        ImportProjectButton = Gtk.Button(label="Import Project")
        ExportProjectButton = Gtk.Button(label="Export Project")
        GenerateDissectorScriptButton = Gtk.Button(label="Generate Dissector Script")
        OrganizeViewsButton = Gtk.Button(label="Organize Views")
        OpenPCAPButton = Gtk.Button(label="Open PCAP")

        testChildWindow = Gtk.Window(title="test")

        CreateProjectButton.connect("clicked", self.create_Project)
        #SaveProjectButton.connect("clicked", self.save_Project)
        #CloseProjectButton.connect("clicked", self.close_Project)
        SwitchWorkspaceButton.connect("clicked", self.switch_Workspace)
        ImportProjectButton.connect("clicked", self.import_Project)
        #ExportProjectButton.connect("clicked", self.export_Project)
        #GenerateDissectorScriptButton.connect("clicked", self.generate_Script)
        OrganizeViewsButton.connect("clicked", self.organize_Views)
        OpenPCAPButton.connect("clicked", self.open_PCAP)



        grid.add(PDGSLabel)
        grid.attach(CreateProjectButton, 0, 1, 1, 1)
        grid.attach_next_to(SaveProjectButton, CreateProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(CloseProjectButton, SaveProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(SwitchWorkspaceButton, CloseProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(ImportProjectButton, SwitchWorkspaceButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(ExportProjectButton, ImportProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(GenerateDissectorScriptButton, ExportProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(OrganizeViewsButton, GenerateDissectorScriptButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(OpenPCAPButton, OrganizeViewsButton, Gtk.PositionType.RIGHT, 8, 1)

        grid.attach_next_to(testChildWindow, CreateProjectButton, Gtk.PositionType.BOTTOM, 1, 3)
       	#grid.add(testChildWindow)


    def create_Project(self, button):
    	print("Create Project")
    	#button action
    	win1 = createProjectWindow.GridWindow()
    	win1.connect("destroy", self.destroy)
    	win1.show_all()

    def switch_Workspace(self, button):
    	print("Switch Workspace")
    	#button action
    	win2 = switchWorkspaceWindow.PathChooserWindow()
    	win2.connect("destroy", self.destroy)
    	win2.show_all()

    def import_Project(self, button):
    	print("Import Project")
    	#button action
    	win3 = importProjectWindow.ProjectImportWindow()
    	win3.connect("destroy", self.destroy)
    	win3.show_all()

    def organize_Views(self, button):
    	print("Organize Views")
    	#button action
    	win4 = organizeViewsWindows.viewsWindow()
    	win4.connect("destroy", self.destroy)
    	win4.show_all()

    def open_PCAP(self, button):
    	print("Open PCAP")
    	#button action
    	win5 = openPCAPWindow.OpenPCAPWindow()
    	win5.connect("destroy", self.destroy)
    	win5.show_all()



win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()