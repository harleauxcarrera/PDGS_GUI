#Heyi Liu
#New Project Widget SRS[6]

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,
        title="Create New Project")

        grid = Gtk.Grid()
        self.add(grid)
        self.set_default_size(300,50)

        name = Gtk.Label("Name:  ")
        nameInput = Gtk.Entry()

        desc = Gtk.Label("Description:  ")
        descInput = Gtk.Entry()

        createButton = Gtk.Button.new_with_mnemonic("Create")
        createButton.connect("clicked", self.on_open_clicked)

        cancelButton = Gtk.Button.new_with_mnemonic("_Cancel")
        cancelButton.connect("clicked", self.on_close_clicked)

        #Add Properties and inputs to grid#
        #attach(addedWidget, leftAttach, topAttach, widthRow, heighColumn)#
        #attach_next_to(addedWidget, attachedToSibling, sideofSiblingToAttackTo, width, height)#

        grid.add(name)
        grid.attach(nameInput, 1, 0, 6, 1)

        grid.attach_next_to(desc,name, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(descInput, 1, 1, 6, 1)

        grid.attach(createButton, 1, 2, 1, 1)
        grid.attach(cancelButton, 2, 2, 1, 1)

    def on_open_clicked(self, button):
        print("New Project was clicked")

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
