import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GenerateDissectorScript(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Dissector Script")

        # Main Box
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(box)

        # Label Box         
        labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        labelBox.set_homogeneous(False)

        # Project Box
        projectBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        projectBox.set_homogeneous(False)

        # Dissector Box
        dissectorBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        dissectorBox.set_homogeneous(False)

        # Save Box
        saveBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        saveBox.set_homogeneous(False)

        # Buttons Box
        buttonsBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        buttonsBox.set_homogeneous(False)

        # Dissector Format Box
        name_store = Gtk.ListStore(str) 
        format_store = ["Format A", "Format B", "Format C"]
        for f in format_store:
            name_store.append([f])

        
        box.pack_start(labelBox, True, True, 5)
        box.pack_start(projectBox, True, True, 5)
        box.pack_start(dissectorBox, True, True, 5)
        box.pack_start(saveBox, True, True, 5)
        box.pack_start(buttonsBox, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Generate a custom dissector from a selected project.")
        label.set_justify(Gtk.Justification.CENTER)
        labelBox.pack_start(label, True, True, 5)

        # Project Name Label
        project = Gtk.Label("Project")
        project.set_justify(Gtk.Justification.RIGHT)
        projectBox.pack_start(project, True, True, 5)

        # Project Name Entry Field
        entry = Gtk.Entry()
        entry.set_text("Project Name")
        projectBox.pack_start(entry, True, True, 5)

        # Browse Button
        browse1Button = Gtk.Button(label = "Browse")
        browse1Button.connect("clicked", self.browse1_clicked)
        projectBox.pack_start(browse1Button, True, True, 5)

        # Dissector Format Label
        dissectorFormat = Gtk.Label("Dissector Format")
        dissectorFormat.set_justify(Gtk.Justification.RIGHT)
        dissectorBox.pack_start(dissectorFormat, True, True, 5)

        # Dissector Format Combo Box
        format_combo = Gtk.ComboBox.new_with_model(name_store)
        format_combo.connect("changed", self.dissector_format_changed)
        renderer_text = Gtk.CellRendererText()
        format_combo.pack_start(renderer_text, True)
        format_combo.add_attribute(renderer_text, "text", 0)
        dissectorBox.pack_start(format_combo, True, True, 5)

        # Save Location Label
        saveLocation = Gtk.Label("Save Location")
        saveLocation.set_justify(Gtk.Justification.RIGHT)
        saveBox.pack_start(saveLocation, True, True, 5)

        # Save Location Entry Field
        saveLocationEntry = Gtk.Entry()
        saveLocationEntry.set_text("Local File System Path")
        saveBox.pack_start(saveLocationEntry, True, True, 5)

        # Browse Button
        browse2Button = Gtk.Button(label = "Browse")
        browse2Button.connect("clicked", self.browse2_clicked)
        saveBox.pack_start(browse2Button, True, True, 5)

        # Generate Button
        generateButton = Gtk.Button(label = "Generate")
        generateButton.connect("clicked", self.generate_clicked)
        buttonsBox.pack_start(generateButton, True, True, 5)

        # Generate Button
        cancelButton = Gtk.Button(label = "Cancel")
        cancelButton.connect("clicked", self.cancel_clicked)
        buttonsBox.pack_start(cancelButton, True, True, 5)



    # Opens a file browser
    def browse1_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a directory", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    # Opens a location browser
    def browse2_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a directory", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def dissector_format_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            format = model[tree_iter][0]
            print("Selected: format=%s" % format)

    # Generate Button 
    def generate_clicked(self, button):
        print("Generate")
        self.destroy()

    # Cancel Button
    def cancel_clicked(self, button):
        print("Cancel")
        self.destroy()