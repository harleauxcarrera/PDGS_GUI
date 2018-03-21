import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DissectorScriptWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Dissector Script")

        grid = Gtk.Grid()
        self.add(grid)
        self.set_default_size(200,50)

        desc = Gtk.Label("Generate a custom dissector script from a selected project.")
        name = Gtk.Label("Project:  ")

        button1 = Gtk.Button("Browse")
        button1.connect("clicked", self.on_file_clicked)

        dformat = Gtk.Label("Dissector Format:  ")
        formatInput = Gtk.ComboBoxText()
        formatInput.insert(0,"0","Format 1")
        formatInput.insert(1,"1","Format 2")
        formatInput.insert(2,"2","etc..")

        location = Gtk.Label("Save Location:  ")
        button2 = Gtk.Button("Browse")
        button2.connect("clicked", self.on_folder_clicked)

        createButton = Gtk.Button.new_with_mnemonic("Generate")
        createButton.connect("clicked", self.on_open_clicked)

        cancelButton = Gtk.Button.new_with_mnemonic("_Cancel")
        cancelButton.connect("clicked", self.on_close_clicked)

        grid.add(desc)
        grid.attach_next_to(name, desc, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(dformat, name, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach_next_to(location, dformat, Gtk.PositionType.BOTTOM, 1,1)

        grid.attach(button1, 1, 1, 2, 1)
        grid.attach(formatInput, 1, 2, 2, 1)
        grid.attach(button2, 1, 3, 2, 1)

        grid.attach(createButton, 1, 4, 1, 1)
        grid.attach(cancelButton, 2, 4, 1, 1)

    def on_file_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

        self.add_filters(dialog)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)

        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

    def on_folder_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a folder", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()


    def on_open_clicked(self, button):
        print("Dissector Script was created")

    def on_close_clicked(self, button):
        print("Closing application")
        self.destroy()

'''win = DissectorScriptWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()'''
