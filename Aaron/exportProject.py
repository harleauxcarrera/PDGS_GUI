import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ExportProject(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Project Export")

        # Main Box
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(box)

        # Label Box         
        labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        labelBox.set_homogeneous(False)

        # Project Box
        projectBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        projectBox.set_homogeneous(False)

        # Export File Box
        exportBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        exportBox.set_homogeneous(False)

        # Buttons Box
        buttonsBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        buttonsBox.set_homogeneous(False)

        box.pack_start(labelBox, True, True, 5)
        box.pack_start(projectBox, True, True, 5)
        box.pack_start(exportBox, True, True, 5)
        box.pack_start(buttonsBox, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Export a project to the local file system.")
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
        browse1Button = Gtk.Button(label = "Browse")
        browse1Button.connect("clicked", self.browse1_clicked)
        projectBox.pack_start(browse1Button, True, True, 5)

        # Export File Label
        export = Gtk.Label("To export file")
        export.set_justify(Gtk.Justification.RIGHT)
        exportBox.pack_start(export, True, True, 5)

        # Export File Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Local File System Path")
        exportBox.pack_start(self.entry, True, True, 5)

         # Browse Button
        browse2Button = Gtk.Button(label = "Browse")
        browse2Button.connect("clicked", self.browse2_clicked)
        exportBox.pack_start(browse2Button, True, True, 5)

        # Export Button
        exportButton = Gtk.Button.new_with_label("Export")
        exportButton.connect("clicked", self.export_clicked)
        buttonsBox.pack_start(exportButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.cancel_clicked)
        buttonsBox.pack_start(cancelButton, True, True, 5)


    # Opens a file browser
    def browse1_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Choose a file", self, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")

        dialog.destroy()

     # Opens a location browser
    def browse2_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Choose a directory", self, Gtk.FileChooserAction.SELECT_FOLDER, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,"Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")

        dialog.destroy()

    # Export button 
    def export_clicked(self, button):
        print("Export")
        self.destroy()

    # Cancel button
    def cancel_clicked(self, button):
        print("Cancel")
        self.destroy()