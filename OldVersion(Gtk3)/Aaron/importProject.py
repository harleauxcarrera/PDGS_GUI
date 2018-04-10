import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ImportProject(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "Project Import")

        # Main Box
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(box)

        # Label Box         
        labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        labelBox.set_homogeneous(False)

        # Project Box
        projectBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        projectBox.set_homogeneous(False)

        # Button Box
        buttonBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        buttonBox.set_homogeneous(False)

        box.pack_start(labelBox, True, True, 5)
        box.pack_start(projectBox, True, True, 5)
        box.pack_start(buttonBox, True, True, 5)

        # Main Label
        label = Gtk.Label("Import a project into the current workspace.")
        label.set_justify(Gtk.Justification.CENTER)
        labelBox.pack_start(label, True, True, 5)

        # Project Name Label
        project = Gtk.Label("Project")
        project.set_justify(Gtk.Justification.RIGHT)
        projectBox.pack_start(project, True, True, 5)

        # Project Name Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Project Name")
        projectBox.pack_start(self.entry, True, True, 5)

        # Browse Button
        projectBrowseButton = Gtk.Button(label = "Browse")
        projectBrowseButton.connect("clicked", self.browse_clicked)
        projectBox.pack_start(projectBrowseButton, True, True, 5)

        # Import Button
        importButton = Gtk.Button(label = "Import")
        importButton.connect("clicked", self.import_clicked)
        buttonBox.pack_start(importButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button(label = "Cancel")
        cancelButton.connect("clicked", self.cancel_clicked)
        buttonBox.pack_start(cancelButton, True, True, 5)


    # Opens a file browser
    def browse_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a file", self, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")

        dialog.destroy()

    # Import button 
    def import_clicked(self, button):
        print("Import")
        self.destroy()

    # Cancel button
    def cancel_clicked(self, button):
        print("Cancel")
        self.destroy()