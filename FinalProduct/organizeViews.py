import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class OrganizeViews(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "Workspace Launcher")

        # Main Box
        self.box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        self.add(self.box)

        # Label Box         
        labelBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        labelBox.set_homogeneous(False)

        # Body Box
        bodyBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        bodyBox.set_homogeneous(False)

        # Column 1 Box
        column1Box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        column1Box.set_homogeneous(False)

        # Column 2 Box
        column2Box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        column2Box.set_homogeneous(False)

        # Column 3 Box
        column3Box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 5)
        column3Box.set_homogeneous(False)

        # Button Box
        buttonBox = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
        buttonBox.set_homogeneous(False)
        
        bodyBox.pack_start(column1Box, True, True, 5)
        bodyBox.pack_start(column2Box, True, True, 5)
        bodyBox.pack_start(column3Box, True, True, 5)
        self.box.pack_start(labelBox, True, True, 5)
        self.box.pack_start(bodyBox, True, True, 5)
        self.box.pack_start(buttonBox, True, True, 5)

        # Main Label
        label = Gtk.Label("Customize the views.")
        label.set_justify(Gtk.Justification.CENTER)
        labelBox.pack_start(label, True, True, 5)

        # Empty Corner Label
        emptyLabel = Gtk.Label("   ")
        emptyLabel.set_justify(Gtk.Justification.CENTER)
        column1Box.pack_start(emptyLabel, True, True, 5)

        # Hide Label
        hideLabel = Gtk.Label("Show")
        hideLabel.set_justify(Gtk.Justification.CENTER)
        column2Box.pack_start(hideLabel, True, True, 5)

        # Show Label
        showLabel = Gtk.Label("Hide")
        showLabel.set_justify(Gtk.Justification.CENTER)
        column3Box.pack_start(showLabel, True, True, 5)


        # Project Navigation Label
        projectLabel = Gtk.Label("Project Navigation")
        projectLabel.set_justify(Gtk.Justification.RIGHT)
        column1Box.pack_start(projectLabel, True, True, 5)

        # Project Navigation Hide Radio Button 
        projectShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        projectShowButton.connect("toggled", self.project_nav_toggled, "Hide")
        column2Box.pack_start(projectShowButton, False, False, 5)

        # Project Navigation Show Radio Button
        projectHideButton = Gtk.RadioButton.new_from_widget(projectShowButton)
        projectHideButton.set_label("")
        projectHideButton.connect("toggled", self.project_nav_toggled, "Show")
        column3Box.pack_start(projectHideButton, False, False, 5)
        

        # Dissector Building Area Label
        dissectorBuildingLabel = Gtk.Label("Dissector Building Area")
        dissectorBuildingLabel.set_justify(Gtk.Justification.RIGHT)
        column1Box.pack_start(dissectorBuildingLabel, True, True, 5)

        # Dissector Building Area Hide Radio Button 
        dissectorBuildingShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        dissectorBuildingShowButton.connect("toggled", self.dissector_builder_toggled, "Hide")
        column2Box.pack_start(dissectorBuildingShowButton, False, False, 5)

        # Dissector Building Area Show Radio Button
        dissectorBuildingHideButton = Gtk.RadioButton.new_from_widget(dissectorBuildingShowButton)
        dissectorBuildingHideButton.set_label("")
        dissectorBuildingHideButton.connect("toggled", self.dissector_builder_toggled, "Show")
        column3Box.pack_start(dissectorBuildingHideButton, False, False, 5)


        # Palette Label
        paletteLabel = Gtk.Label("Palette")
        paletteLabel.set_justify(Gtk.Justification.RIGHT)
        column1Box.pack_start(paletteLabel, True, True, 5)

        # Palette Hide Radio Button 
        paletteShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        paletteShowButton.connect("toggled", self.palette_toggled, "Hide")
        column2Box.pack_start(paletteShowButton, False, False, 5)

        # Palette Show Radio Button
        paletteHideButton = Gtk.RadioButton.new_from_widget(paletteShowButton)
        paletteHideButton.set_label("")
        paletteHideButton.connect("toggled", self.palette_toggled, "Show")
        column3Box.pack_start(paletteHideButton, False, False, 5)
        

        # Packet Stream Area Label
        packetStreamLabel = Gtk.Label("Packet Stream Area")
        packetStreamLabel.set_justify(Gtk.Justification.RIGHT)
        column1Box.pack_start(packetStreamLabel, True, True, 5)

        # Packet Stream Area Hide Radio Button
        packetStreamShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        packetStreamShowButton.connect("toggled", self.packet_stream_toggled, "Hide")
        column2Box.pack_start(packetStreamShowButton, False, False, 5)

        # Packet Stream Area Show Radio Button
        packetStreamHideButton = Gtk.RadioButton.new_from_widget(packetStreamShowButton)
        packetStreamHideButton.set_label("")
        packetStreamHideButton.connect("toggled", self.packet_stream_toggled, "Show")
        column3Box.pack_start(packetStreamHideButton, False, False, 5)


        # Dissected Stream Area Label
        dissectedStreamLabel = Gtk.Label("Dissected Stream Area")
        dissectedStreamLabel.set_justify(Gtk.Justification.RIGHT)
        column1Box.pack_start(dissectedStreamLabel, True, True, 5)

        # Dissected Stream Area Hide Radio Button 
        dissectedStreamShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        dissectedStreamShowButton.connect("toggled", self.dissected_stream_toggled, "Hide")
        column2Box.pack_start(dissectedStreamShowButton, False, False, 5)

        # Dissected Stream Area Show Radio Button
        dissectedStreamHideButton = Gtk.RadioButton.new_from_widget(dissectedStreamShowButton)
        dissectedStreamHideButton.set_label("")
        dissectedStreamHideButton.connect("toggled", self.dissected_stream_toggled, "Show")
        column3Box.pack_start(dissectedStreamHideButton, False, False, 5)
        
        
        # Raw Data Area Label
        rawDataLabel = Gtk.Label("Raw Data Area")
        rawDataLabel.set_justify(Gtk.Justification.RIGHT)
        column1Box.pack_start(rawDataLabel, True, True, 5)

         # Raw Data Area Hide Radio Button 
        rawDataShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        rawDataShowButton.connect("toggled", self.raw_data_toggled, "Hide")
        column2Box.pack_start(rawDataShowButton, False, False, 5)

        # Raw Data Area Show Radio Button
        rawDataHideButton = Gtk.RadioButton.new_from_widget(rawDataShowButton)
        rawDataHideButton.set_label("")
        rawDataHideButton.connect("toggled", self.raw_data_toggled, "Show")
        column3Box.pack_start(rawDataHideButton, False, False, 5)

        
        # Console Area Label
        consoleAreaLabel = Gtk.Label("Console Area")
        consoleAreaLabel.set_justify(Gtk.Justification.RIGHT)
        column1Box.pack_start(consoleAreaLabel, True, True, 5)

        # Console Area Hide Radio Button 
        consoleAreaShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        consoleAreaShowButton.connect("toggled", self.console_area_toggled, "Hide")
        column2Box.pack_start(consoleAreaShowButton, False, False, 5)
        
        # Console Area Show Radio Button
        consoleAreaHideButton = Gtk.RadioButton.new_from_widget(consoleAreaShowButton)
        consoleAreaHideButton.set_label("")
        consoleAreaHideButton.connect("toggled", self.console_area_toggled, "Show")
        column3Box.pack_start(consoleAreaHideButton, False, False, 5)


        # Restore to Default Button
        defaultButton = Gtk.Button(label = "Restore to Default")
        defaultButton.connect("clicked", self.default_toggled, projectShowButton, dissectorBuildingShowButton, paletteShowButton, packetStreamShowButton,dissectedStreamShowButton, rawDataShowButton, consoleAreaShowButton)
        buttonBox.pack_start(defaultButton, True, True, 5)

        # Confirm Button
        confirmButton = Gtk.Button(label = "Confirm")
        confirmButton.connect("clicked", self.confirm_clicked)
        buttonBox.pack_start(confirmButton, False, False, 5)

        # Cancel Button
        cancelButton = Gtk.Button(label = "Cancel")
        cancelButton.connect("clicked", self.cancel_clicked)
        buttonBox.pack_start(cancelButton, False, False, 5)
        

    def project_nav_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Project Navigation", name, "was turned", state)


    def dissector_builder_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Dissector Builder Area", name, "was turned", state)


    def palette_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Palette", name, "was turned", state)


    def packet_stream_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Packet Stream Area", name, "was turned", state)


    def dissected_stream_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Dissected Stream Area", name, "was turned", state)


    def raw_data_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Raw Data Area", name, "was turned", state)

    
    def console_area_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Console Area", name, "was turned", state)


    # Restore to Default Button
    def default_toggled(self, button, projectShowButton, dissectorBuildingShowButton, paletteShowButton, packetStreamShowButton, dissectedStreamShowButton, rawDataShowButton, consoleAreaShowButton): 

        projectShowButton.set_active(True) 
        dissectorBuildingShowButton.set_active(True) 
        paletteShowButton.set_active(True)
        packetStreamShowButton.set_active(True)
        dissectedStreamShowButton.set_active(True)
        rawDataShowButton.set_active(True)
        consoleAreaShowButton.set_active(True)
        

    # Confirm Button
    def confirm_clicked(self, button):
        print("Confirm")
        self.destroy()

    # Cancel Button
    def cancel_clicked(self, button):
        print("Cancel")
        self.destroy()