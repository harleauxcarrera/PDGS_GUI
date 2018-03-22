#Carlos Herrera
# Start Field[Protocol Name] Widget SRS[17]

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class startFieldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,
        title="Start Field [Protocol Name]")

        grid = Gtk.Grid()
        self.add(grid)

        # Field Properties and Inputs#
        protoName = Gtk.Label("Protocol Name:  ")
        name = Gtk.Entry()

        protoDescr = Gtk.Label("Protocol Description:  ")
        descr = Gtk.Entry()

        depProto = Gtk.Label("Dependedent Protocol:  ")
        dep = Gtk.Entry()


        depPattern = Gtk.Label("Dependency Pattern:  ")
        pattern = Gtk.Entry()



        #Add Properties and inputs to grid#
        #attach(addedWidget, leftAttach, topAttach, widthRow, heighColumn)#
        #attach_next_to(addedWidget, attachedToSibling, sideofSiblingToAttackTo, width, height)#
        grid.add(protoName)
        grid.attach(name, 1, 0, 4, 1)

        grid.attach_next_to(protoDescr,protoName, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(descr, 1, 1, 4, 1)

        grid.attach_next_to(depProto,protoDescr, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(dep, 1, 2, 4, 1)

        grid.attach_next_to(depPattern,depProto, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(pattern, 1, 3, 4, 1)

        button1 = Gtk.Button("OK")
        button1.connect("clicked", self.on_open_clicked)
        grid.attach_next_to(button1, pattern, Gtk.PositionType.BOTTOM, 1, 1)
        cancel_button = Gtk.Button("Cancel")
        cancel_button.connect("clicked", self.on_close_clicked)
        grid.attach_next_to(cancel_button, button1, Gtk.PositionType.RIGHT, 1, 1)

        #added these funcs for cancel and ok button
    def on_open_clicked(self, button):
        print("New start field was created")
        self.destroy()

    def on_close_clicked(self, button):
        print("Closing application")
        self.destroy()