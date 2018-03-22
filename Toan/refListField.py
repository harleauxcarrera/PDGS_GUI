import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class refListFieldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Reference List[Reference List Name]")

        self.set_default_size(360, 200)

        #APPEND REFERENCE LIST VALUES HERE#
        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["Fedora", "http://fedoraproject.org/"])
        self.liststore.append(["Slackware", "http://www.slackware.com/"])
        self.liststore.append(["Sidux", "http://sidux.com/"])

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

        self.add(treeview)
    

    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text

