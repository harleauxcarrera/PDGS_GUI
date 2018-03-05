# SRS[16] - Field Widget


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FieldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Field[Abbreviation]")
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        #Name
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_1.add(box_1)
        label = Gtk.Label("Name")
        nameInput = Gtk.Entry()
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(nameInput, True, True, 0)
        listbox.add(row_1)

        #Abbreviation
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_2.add(box_2)
        label = Gtk.Label("Abbreviation")
        abbrevInput = Gtk.Entry()
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(abbrevInput, True, True, 0)
        listbox.add(row_2)

        #Description
        row_3 = Gtk.ListBoxRow()
        box_3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_3.add(box_3)
        label = Gtk.Label("Description")
        descInput = Gtk.Entry()
        box_3.pack_start(label, True, True, 0)
        box_3.pack_start(descInput, True, True, 0)
        listbox.add(row_3)

        #Reference List
        row_4 = Gtk.ListBoxRow()
        box_4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_4.add(box_4)
        label = Gtk.Label("Reference List")
        refInput = Gtk.ComboBoxText()
        refInput.insert(0,"0", "type 1")
        refInput.insert(1,"1", "type 2")
        refInput.insert(2, "2", "ect..")
        box_4.pack_start(label, True, True, 0)
        box_4.pack_start(refInput, True, True, 0)
        listbox.add(row_4)

        #Data Type
        row_5 = Gtk.ListBoxRow()
        box_5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_5.add(box_5)
        label = Gtk.Label("Data Type")
        dataTypeInput = Gtk.ComboBoxText()
        dataTypeInput.insert(0,"0", "type 1")
        dataTypeInput.insert(1,"1", "type 2")
        dataTypeInput.insert(2, "2", "ect..")
        box_5.pack_start(label, True, True, 0)
        box_5.pack_start(dataTypeInput, True, True, 0)
        listbox.add(row_5)

        #Base
        row_6 = Gtk.ListBoxRow()
        box_6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_6.add(box_6)
        label = Gtk.Label("Base")
        baseInput = Gtk.ComboBoxText()
        baseInput.insert(0,"0", "type 1")
        baseInput.insert(1,"1", "type 2")
        baseInput.insert(2, "2", "ect..")
        box_6.pack_start(label, True, True, 0)
        box_6.pack_start(baseInput, True, True, 0)
        listbox.add(row_6)

        #Mask
        row_7 = Gtk.ListBoxRow()constraintInput
        box_7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_7.add(box_7)
        label = Gtk.Label("Mask")
        maskInput = Gtk.Entry()
        box_7.pack_start(label, True, True, 0)
        box_7.pack_start(maskInput, True, True, 0)
        listbox.add(row_7)

        #Value Contraint
        row_8 = Gtk.ListBoxRow()
        box_8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_8.add(box_8)
        label = Gtk.Label("Value Constraint")
        constraintInput = Gtk.Entry()
        box_8.pack_start(label, True, True, 0)
        box_8.pack_start(constraintInput, True, True, 0)
        listbox.add(row_8)

        #Required
        row_9 = Gtk.ListBoxRow()
        box_9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_9.add(box_9)
        label = Gtk.Label("Required")
        requiredBox = Gtk.CheckButton()
        box_9.pack_start(label, True, True, 0)constraintInput
        box_9.pack_start(requiredBox, True, True, 0)
        listbox.add(row_9)


win = FieldWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
