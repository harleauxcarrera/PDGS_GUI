#Carlos Herrera
# Start Field[Protocol Name] Widget SRS[17]

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

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






win = GridWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
