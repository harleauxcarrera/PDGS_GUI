import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class BuilderCanvas(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Builder Canvas")

        self.set_default_size(600,600)

window = BuilderCanvas()
window.show_all()
window.connect("destroy", Gtk.main_quit)
Gtk.main()