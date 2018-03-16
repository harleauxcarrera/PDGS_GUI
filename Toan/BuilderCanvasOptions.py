import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class BuilderCanvasOptions(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Builder Canvas Options")

        grid = Gtk.Grid()
        self.add(grid)
        self.set_default_size(300,50)

        StartField = Gtk.Button("StartField")
        StartField.connect("clicked", self.button_pressed)

        Field1Byte = Gtk.Button.new_with_mnemonic("Field(1 byte)")
        Field1Byte.connect("clicked", self.button_pressed)

        Field2Byte = Gtk.Button.new_with_mnemonic("Field(2 byte)")
        Field2Byte.connect("clicked", self.button_pressed)

        Field4Byte = Gtk.Button.new_with_mnemonic("Field(4 byte)")
        Field4Byte.connect("clicked", self.button_pressed)

        Field8Byte = Gtk.Button.new_with_mnemonic("Field(8 byte)")
        Field8Byte.connect("clicked", self.button_pressed)

        EndField = Gtk.Button.new_with_mnemonic("EndField")
        EndField.connect("clicked", self.button_pressed)

        ReferenceList = Gtk.Button.new_with_mnemonic("Reference List")
        ReferenceList.connect("clicked", self.button_pressed)

        PacketInfo = Gtk.Button.new_with_mnemonic("Packet Info")
        PacketInfo.connect("clicked", self.button_pressed)

        grid.attach(StartField, 1, 1, 1, 1)
        grid.attach(Field1Byte, 2, 1, 1, 1)
        grid.attach(Field2Byte, 3, 1, 1, 1)
        grid.attach(Field4Byte, 4, 1, 1, 1)
        grid.attach(Field8Byte, 1, 2, 1, 1)
        grid.attach(EndField, 2, 2, 1, 1)
        grid.attach(ReferenceList, 3, 2, 1, 1)
        grid.attach(PacketInfo, 4, 2, 1, 1)

    def button_pressed(self, button):
        print("Button Pressed")


window = BuilderCanvasOptions()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()