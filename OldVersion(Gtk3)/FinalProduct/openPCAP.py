import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class OpenPCAP(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Open PCAP")

        # Main Box
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(box)

        # Label Box         
        labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        labelBox.set_homogeneous(False)

        # PCAP Box
        PCAPBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        PCAPBox.set_homogeneous(False)

        # Button Box
        buttonBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        buttonBox.set_homogeneous(False)

        box.pack_start(labelBox, True, True, 5)
        box.pack_start(PCAPBox, True, True, 5)
        box.pack_start(buttonBox, True, True, 5)

        # Main Label
        label = Gtk.Label("Open a PCAP file")
        label.set_justify(Gtk.Justification.CENTER)
        labelBox.pack_start(label, True, True, 5)

        # PCAP Name Label
        pcapName = Gtk.Label("PCAP Name")
        pcapName.set_justify(Gtk.Justification.RIGHT)
        PCAPBox.pack_start(pcapName, True, True, 5)

        # PCAP Name Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("PCAP File")
        PCAPBox.pack_start(self.entry, True, True, 5)

        # Browse Button
        browseButton = Gtk.Button(label = "Browse")
        browseButton.connect("clicked", self.browse_clicked)
        PCAPBox.pack_start(browseButton, True, True, 5)

        # Open Button
        openButton = Gtk.Button(label = "Open")
        openButton.connect("clicked", self.open_clicked)
        buttonBox.pack_start(openButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button(label = "Cancel")
        cancelButton.connect("clicked", self.cancel_clicked)
        buttonBox.pack_start(cancelButton, True, True, 5)


    # Opens a PCAP file browser
    def browse_clicked(self, button):
        dialog = Gtk.FileChooserDialog("Please choose a PCAP file", self, Gtk.FileChooserAction.OPEN, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel")

        dialog.destroy()

    # Open button 
    def open_clicked(self, button):
        print("Open")
        self.destroy()

    # Cancel button
    def cancel_clicked(self, button):
        print("Cancel")
        self.destroy()