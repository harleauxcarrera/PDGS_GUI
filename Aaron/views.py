import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class viewsWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Organize Views")

        grid = Gtk.Grid()
        self.add(grid)
        self.set_default_size(200,50)

        label0 = Gtk.Label(" ")
        label1 = Gtk.Label("Project Navigation  ")
        label2 = Gtk.Label("Dissector Building Area  ")
        label3 = Gtk.Label("Palette  ")
        label4 = Gtk.Label("Packet Stream Area  ")
        label5 = Gtk.Label("Dissector Stream Area  ")
        label6 = Gtk.Label("Raw Data Area  ")
        label7 = Gtk.Label("Console Area  ")

        hide = Gtk.Label("                           Show")
        show = Gtk.Label("                           Hide")

        button1 = Gtk.RadioButton.new_with_label_from_widget(None, " ")
        button1.connect("toggled", self.on_button_toggled, "1")

        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.connect("toggled", self.on_button_toggled, "2")

        button3 = Gtk.RadioButton.new_with_label_from_widget(None, " ")
        button3.connect("toggled", self.on_button_toggled, "3")

        button4 = Gtk.RadioButton.new_from_widget(button3)
        button4.connect("toggled", self.on_button_toggled, "4")

        button5 = Gtk.RadioButton.new_with_label_from_widget(None, " ")
        button5.connect("toggled", self.on_button_toggled, "5")

        button6 = Gtk.RadioButton.new_from_widget(button5)
        button6.connect("toggled", self.on_button_toggled, "6")

        button7 = Gtk.RadioButton.new_with_label_from_widget(None, " ")
        button7.connect("toggled", self.on_button_toggled, "7")

        button8 = Gtk.RadioButton.new_from_widget(button7)
        button8.connect("toggled", self.on_button_toggled, "8")

        button9 = Gtk.RadioButton.new_with_label_from_widget(None, " ")
        button9.connect("toggled", self.on_button_toggled, "9")

        button10 = Gtk.RadioButton.new_from_widget(button9)
        button10.connect("toggled", self.on_button_toggled, "10")

        button11 = Gtk.RadioButton.new_with_label_from_widget(None, " ")
        button11.connect("toggled", self.on_button_toggled, "11")

        button12 = Gtk.RadioButton.new_from_widget(button11)
        button12.connect("toggled", self.on_button_toggled, "12")

        button13 = Gtk.RadioButton.new_with_label_from_widget(None, " ")
        button13.connect("toggled", self.on_button_toggled, "13")

        button14 = Gtk.RadioButton.new_from_widget(button13)
        button14.connect("toggled", self.on_button_toggled, "14")

        defaultButton = Gtk.Button.new_with_mnemonic("Restore to Default")
        defaultButton.connect("clicked", self.on_default_clicked, button1, button3, button5, button7, button9, button11, button13)

        confirmButton = Gtk.Button.new_with_mnemonic("Confirm")
        confirmButton.connect("clicked", self.on_open_clicked)

        cancelButton = Gtk.Button.new_with_mnemonic("_Cancel")
        cancelButton.connect("clicked", self.on_close_clicked)

        grid.add(label0)
        grid.attach_next_to(label1, label0, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(label2, label1, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(label3, label2, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(label4, label3, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(label5, label4, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(label6, label5, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(label7, label6, Gtk.PositionType.BOTTOM, 1,1)

        #attach(addedWidget, leftAttach, topAttach, widthRow, heighColumn)#
        #attach_next_to(addedWidget, attachedToSibling, sideofSiblingToAttackTo, width, height)#

        grid.attach(hide, 1, 0, 2, 1)
        grid.attach(show, 3, 0, 2, 1)
        grid.attach(button1, 2, 1, 2, 1)
        grid.attach(button2, 4, 1, 2, 1)
        grid.attach(button3, 2, 2, 2, 1)
        grid.attach(button4, 4, 2, 2, 1)
        grid.attach(button5, 2, 3, 2, 1)
        grid.attach(button6, 4, 3, 2, 1)
        grid.attach(button7, 2, 4, 2, 1)
        grid.attach(button8, 4, 4, 2, 1)
        grid.attach(button9, 2, 5, 2, 1)
        grid.attach(button10, 4, 5, 2, 1)
        grid.attach(button11, 2, 6, 2, 1)
        grid.attach(button12, 4, 6, 2, 1)
        grid.attach(button13, 2, 7, 2, 1)
        grid.attach(button14, 4, 7, 2, 1)

        grid.attach(defaultButton, 1, 8, 1, 1)
        grid.attach(confirmButton, 2, 8, 1, 1)
        grid.attach(cancelButton, 3, 8, 1, 1)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

    def on_default_clicked(self, button, button1, button3, button5, button7, button9, button11, button13):
        button1.set_active(True)
        button3.set_active(True)
        button5.set_active(True)
        button7.set_active(True)
        button9.set_active(True)
        button11.set_active(True)
        button13.set_active(True)

    def on_open_clicked(self, button):
        print("Dissector Script was created")

    def on_close_clicked(self, button):
        print("Closing application")
        self.destroy()

'''win = viewsWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()'''
