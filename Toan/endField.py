#Carlos Herrera
# Start Field[Protocol Name] Widget SRS[18]

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class endFieldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,
        title="End Field")
        self.set_default_size(300,50)

        grid = Gtk.Grid()
        self.add(grid)
