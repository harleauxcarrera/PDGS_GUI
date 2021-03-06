import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class packetInfoWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PacketInfo")

        self.set_default_size(360, 200)

        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
        #APPEND REFERENCE LIST VALUES HERE#
        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["X", "X"])
        self.liststore.append(["Y", "Y"])
        self.liststore.append(["Y", "Y"])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Value", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_editabletext = Gtk.CellRendererText()
        renderer_editabletext.set_property("editable", True)

        column_editabletext = Gtk.TreeViewColumn("Text Description",
            renderer_editabletext, text=1)
        treeview.append_column(column_editabletext)

        renderer_editabletext.connect("edited", self.text_edited)
        self.add(box)
        box.add(treeview)

        add_button = Gtk.Button.new_with_mnemonic("+")
        add_button.connect("clicked", self.on_add_clicked)
        box.add(add_button)


    def on_add_clicked(self, button):
        print("New field was created")
        self.destroy()

    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text