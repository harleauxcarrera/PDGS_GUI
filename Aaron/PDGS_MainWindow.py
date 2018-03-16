import gi
import createProject as createProjectWindow


gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Protocol Dissector Generator System")

        grid = Gtk.Grid()
        self.add(grid)
        self.set_default_size(500,700)

        PDGSLabel = Gtk.Label(label = "Protocol Dissector Generator System")
        CreateProjectButton = Gtk.Button(label="Create Project")
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



        grid.add(PDGSLabel)
        grid.attach(CreateProjectButton, 0, 1, 8, 3)
        grid.attach_next_to(SaveProjectButton, CreateProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(CloseProjectButton, SaveProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(SwitchWorkspaceButton, CloseProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(ImportProjectButton, SwitchWorkspaceButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(ExportProjectButton, ImportProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(GenerateDissectorScriptButton, ExportProjectButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(OrganizeViewsButton, GenerateDissectorScriptButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(OpenPCAPButton, OrganizeViewsButton, Gtk.PositionType.RIGHT, 8, 1)
        grid.attach_next_to(testChildWindow, CreateProjectButton, Gtk.PositionType.BOTTOM, 1, 3)



    def create_Project(self, button):
    	print("Create Project")
    	#button action
    	win2 = createProjectWindow.GridWindow()
    	win2.connect("destroy", self.destroy)
    	win2.show_all()





win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()