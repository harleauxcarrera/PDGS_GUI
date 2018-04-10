import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PathChooserWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")

        grid = Gtk.Grid()
        self.add(grid)
        self.set_default_size(300,50)

        desc = Gtk.Label("Select a directory as workspace.")
        name = Gtk.Label("Workspace:  ")

        button2 = Gtk.Button("Browse")
        button2.connect("clicked", self.on_folder_clicked)

        createButton = Gtk.Button.new_with_mnemonic("Launch")
        createButton.connect("clicked", self.on_open_clicked)

        cancelButton = Gtk.Button.new_with_mnemonic("_Cancel")
        cancelButton.connect("clicked", self.on_close_clicked)

        grid.add(desc)
        grid.attach_next_to(name, desc, Gtk.PositionType.BOTTOM, 1,1)
        grid.attach(button2, 1, 1, 2, 1)
        grid.attach(createButton, 1, 2, 1, 1)
        grid.attach(cancelButton, 2, 2, 1, 1)


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
        print("Workspace was created")

    def on_close_clicked(self, button):
        print("Closing application")
        self.destroy()


