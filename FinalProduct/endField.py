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

        #OK and CANCEL BUTTONS
        ok_button = Gtk.Button.new_with_mnemonic("OK")
        ok_button.connect("clicked", self.on_open_clicked)

        cancel_button = Gtk.Button.new_with_mnemonic("Cancel")
        cancel_button.connect("clicked", self.on_close_clicked)

        grid.add(ok_button)
        grid.attach_next_to(cancel_button,ok_button, Gtk.PositionType.RIGHT, 1, 1 )

    #added these funcs for cancel and ok button
    def on_open_clicked(self, button):
        print("New field was created")
        self.destroy()

    def on_close_clicked(self, button):
        print("Closing application")
        self.destroy()
