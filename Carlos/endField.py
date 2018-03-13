#Carlos Herrera
# Start Field[Protocol Name] Widget SRS[18]

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,
        title="End Field")

        grid = Gtk.Grid()
        self.add(grid)







win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
