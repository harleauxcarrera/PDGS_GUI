#Carlos Herrera
# Field Widget SRS[16]

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GridWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,
        title="Field")

        grid = Gtk.Grid()
        self.add(grid)

        # Field Properties and Inputs#
        name = Gtk.Label("Name:  ")
        nameInput = Gtk.Entry()

        abbrv = Gtk.Label("Abbreviation:  ")
        abbrevInput = Gtk.Entry()

        descr = Gtk.Label("Description:  ")
        descInput = Gtk.Entry()

        ref = Gtk.Label("Reference List:  ")
        refInput = Gtk.ComboBoxText()
        refInput.insert(0,"0", "type 1")
        refInput.insert(1,"1", "type 2")
        refInput.insert(2, "2", "ect..")

        dataT = Gtk.Label("Data Type:  ")
        dataTypeInput = Gtk.ComboBoxText()
        dataTypeInput.insert(0,"0", "type 1")
        dataTypeInput.insert(1,"1", "type 2")
        dataTypeInput.insert(2, "2", "ect..")

        base = Gtk.Label("Base:  ")
        baseInput = Gtk.ComboBoxText()
        baseInput.insert(0,"0", "type 1")
        baseInput.insert(1,"1", "type 2")
        baseInput.insert(2, "2", "ect..")

        mask = Gtk.Label("Mask:  ")
        maskInput = Gtk.Entry()

        vconst = Gtk.Label("Value Constraint:  ")
        constraintInput = Gtk.Entry()

        req = Gtk.Label("Required:  ")
        requiredBox = Gtk.CheckButton()

        #Add Properties and inputs to grid#
        #attach(addedWidget, leftAttach, topAttach, widthRow, heighColumn)#
        #attach_next_to(addedWidget, attachedToSibling, sideofSiblingToAttackTo, width, height)#
        grid.add(name)
        grid.attach(nameInput, 1, 0, 4, 1)

        grid.attach_next_to(abbrv,name, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(abbrevInput, 1, 1, 4, 1)

        grid.attach_next_to(descr,abbrv, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(descInput, 1, 2, 4, 1)

        grid.attach_next_to(ref,descr, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(refInput, 1, 3, 4, 1)

        grid.attach_next_to(dataT,ref, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(dataTypeInput, 1, 4, 4, 1)

        grid.attach_next_to(base,dataT, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(baseInput, 1, 5, 4, 1)

        grid.attach_next_to(mask,base, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(maskInput, 1, 6, 4, 1)

        grid.attach_next_to(vconst,mask, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(constraintInput, 1, 7, 4, 1)

        grid.attach_next_to(req,vconst, Gtk.PositionType.BOTTOM, 1,1 )
        grid.attach(requiredBox, 1, 8, 4, 1)




win = GridWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
