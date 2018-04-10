import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class CreateProject(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Project")

        # Main Box
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(box)

        # Label Box         
        labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        labelBox.set_homogeneous(False)

        # Project Name Box
        projectNameBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        projectNameBox.set_homogeneous(False)

        # Description Box
        descriptionBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        descriptionBox.set_homogeneous(False)

        # Button Box
        buttonBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        buttonBox.set_homogeneous(False)
        
        box.pack_start(labelBox, True, True, 0)
        box.pack_start(projectNameBox, True, True, 0)
        box.pack_start(descriptionBox, True, True, 0)
        box.pack_start(buttonBox, True, True, 0)

        # Title Label Area
        label = Gtk.Label("Create a new project.")
        label.set_justify(Gtk.Justification.CENTER)
        labelBox.pack_start(label, True, True, 5)

        # Project Name Label
        workspace = Gtk.Label("Project Name")
        workspace.set_justify(Gtk.Justification.RIGHT)
        projectNameBox.pack_start(workspace, True, True, 5)

        # Project Name Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Project Name")
        projectNameBox.pack_start(self.entry, True, True, 5)

        # Description Label
        description = Gtk.Label("Description")
        workspace.set_justify(Gtk.Justification.RIGHT)
        descriptionBox.pack_start(description, True, True, 5)

        # Description Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Description")
        descriptionBox.pack_start(self.entry, True, True, 5)

        # Create Button
        createButton = Gtk.Button.new_with_label("Create")
        createButton.connect("clicked", self.CreateButton_clicked)
        buttonBox.pack_start(createButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.CancelButton_clicked)
        buttonBox.pack_start(cancelButton, True, True, 5)


    # Create Button 
    def CreateButton_clicked(self, createButton):
        print("Create")
        self.destroy()

    # Cancel Button
    def CancelButton_clicked(self, cancelButton):
        print("Cancel")
        self.destroy()