import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import WorkspaceLauncher
import NewProject
import DissectorScript
import ProjectImport
import ProjectExport
import PCAP
import OrganizeViews
import SaveProject

class MenuSection(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Menu Section")

         # Creates Big Box
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.add(box)

        # Create Project Button
        createProjectButton = Gtk.Button.new_with_label("Create Project")
        createProjectButton.connect("clicked", self.on_create_project_clicked)
        box.pack_start(createProjectButton, True, True, 5)

        # Save Project Button
        saveProjectButton = Gtk.Button.new_with_label("Save Project")
        saveProjectButton.connect("clicked", self.on_save_project_clicked)
        box.pack_start(saveProjectButton, True, True, 5)

        # Close Project Button
        closeProjectButton = Gtk.Button.new_with_label("Close Project")
        closeProjectButton.connect("clicked", self.on_close_project_clicked)
        box.pack_start(closeProjectButton, True, True, 5)

        # Switch Workspace Button
        switchWorkspaceButton = Gtk.Button.new_with_label("Switch Workspace")
        switchWorkspaceButton.connect("clicked", self.on_workspace_button_clicked)
        box.pack_start(switchWorkspaceButton, True, True, 5)

        # Import Project Button
        importProjectButton = Gtk.Button.new_with_label("Import Project")
        importProjectButton.connect("clicked", self.on_import_button_clicked)
        box.pack_start(importProjectButton, True, True, 5)

        # Export Project Button
        exportProjectButton = Gtk.Button.new_with_label("Export Project")
        exportProjectButton.connect("clicked", self.on_export_button_clicked)
        box.pack_start(exportProjectButton, True, True, 5)    

        # Generate Dissector Script Button
        generateDSButton = Gtk.Button.new_with_label("Generate Dissector Script")
        generateDSButton.connect("clicked", self.on_generateDS_button_clicked)
        box.pack_start(generateDSButton, True, True, 5)

        # Organize Views Button
        organizeViewsButton = Gtk.Button.new_with_label("Organize Views")
        organizeViewsButton.connect("clicked", self.on_organize_views_button_clicked)
        box.pack_start(organizeViewsButton, True, True, 5)

        # Open PCAP Button
        openPCAPButton = Gtk.Button.new_with_label("Open PCAP")
        openPCAPButton.connect("clicked", self.on_open_pcap_button_clicked)
        box.pack_start(openPCAPButton, True, True, 5)


    def on_save_project_clicked(self, saveProjectButton):
        win = SaveProject.SaveProject()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_close_project_clicked(self, closeProjectButton):
        print("Closing Project")

    def on_workspace_button_clicked(self, switchWorkspaceButton):
        win = WorkspaceLauncher.WorkspaceLauncher()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_create_project_clicked(self, createProjectButton):
        win = NewProject.NewProject()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_generateDS_button_clicked(self, generateDSButton):
        win = DissectorScript.DissectorScript()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_import_button_clicked(self, importProjectButton):
        win = ProjectImport.ProjectImport()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_export_button_clicked(self, exportProjectButton):
        win = ProjectExport.ProjectExport()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
    
    def on_organize_views_button_clicked(self, organizeViewsButton):
        win = OrganizeViews.OrganizeViews()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
    
    def on_open_pcap_button_clicked(self, openPCAPButton):
        win = PCAP.PCAP()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

'''
win = MenuSection()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''