import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SwitchWorkspace(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "Workspace Launcher")

        # Main Box
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(self.box)

        # Label Box         
        labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        labelBox.set_homogeneous(False)

        # Workspace Box`````````````````````````
        workspaceBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        workspaceBox.set_homogeneous(False)

        # Buttons Box
        buttonsBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        buttonsBox.set_homogeneous(False)
        
        self.box.pack_start(labelBox, True, True, 5)
        self.box.pack_start(workspaceBox, True, True, 5)
        self.box.pack_start(buttonsBox, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Select a directory as workspace: PDGS uses the workspace \n directory to store projects.")
        label.set_justify(Gtk.Justification.CENTER)
        labelBox.pack_start(label, True, True, 5)

        # Workspace Label
        workspace = Gtk.Label("Workspace")
        workspace.set_justify(Gtk.Justification.LEFT)
        workspaceBox.pack_start(workspace, True, True, 5)

        # Workspace Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Workspace Directory Path")
        workspaceBox.pack_start(self.entry, True, True, 5)

        # Browse Button
        browseButton = Gtk.Button(label = "Browse")
        browseButton.connect("clicked", self.browse_clicked)
        workspaceBox.pack_start(browseButton, True, True, 5)

        # Launch Button
        launchButton = Gtk.Button(label = "Launch")
        launchButton.connect("clicked", self.launch_clicked)
        buttonsBox.pack_start(launchButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button(label = "Cancel")
        cancelButton.connect("clicked", self.cancel_clicked)
        buttonsBox.pack_start(cancelButton, True, True, 5)

    # File browser
    def browse_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a directory", self, Gtk.FileChooserAction.SELECT_FOLDER, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")

        dialog.destroy()

    # Launch button 
    def launch_clicked(self, button):
        print("Launch")
        self.destroy()

    # Cancel button
    def cancel_clicked(self, button):
        print("Cancel")
        self.destroy()