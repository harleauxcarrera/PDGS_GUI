import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

packet = [("1", "9:20", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("2", "9:21", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("3", "9:22", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("4", "9:23", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("5", "9:24", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("6", "9:25", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("7", "9:26", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("8", "9:27", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info...."),
          ("9", "9:28", "192.168.0.31", "192.168.0.28", "TCP", "Packet Info....")]

class ConsoleAreaWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_border_width(10)
        self.set_default_size(500, 300)
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Packet Preview Area"
        self.set_titlebar(header_bar)

        refresh_button = Gtk.Button()
        refresh_icon = Gio.ThemedIcon(name="view-refresh-symbolic")
        image = Gtk.Image.new_from_gicon(refresh_icon, Gtk.IconSize.BUTTON)
        refresh_button.add(image)
        header_bar.pack_end(refresh_button)

        # Create a box and link items together
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")

        # Left arrow
        left_arrow = Gtk.Button()
        left_arrow.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(left_arrow)

        # Right arrow
        right_arrow = Gtk.Button()
        right_arrow.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(right_arrow)

        header_bar.pack_start(box)

        # Packet Stream Area View
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)

        packet_list_store = Gtk.ListStore(str, str, str, str, str, str)
        for item in packet:
            packet_list_store.append(list(item))

        treeView = Gtk.TreeView(packet_list_store)
        for i, col_title in enumerate(["No.", "Time", "Source", "Destination", "Protocol", "Info"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            column.set_sort_column_id(0)
            treeView.append_column(column)

        self.page1.pack_start(treeView, True, True, 0)
        packetCaptureLabel = Gtk.Label()
        packetCaptureLabel.set_markup("<b>Packet Stream Area View</b>")

        self.notebook.append_page(self.page1, packetCaptureLabel)

        # Dissected Stream Area View
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Image.new_from_file('DissectedStream.png'))
        dissectedStreamLabel = Gtk.Label()
        dissectedStreamLabel.set_markup("<b>Dissected Stream Area View</b>")
        self.notebook.append_page(self.page2, dissectedStreamLabel)

        # Raw Data Area View
        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.page3.add(Gtk.Image.new_from_file('RawData.png'))
        rawDataLabel = Gtk.Label()
        rawDataLabel.set_markup("<b>Raw Data Area View</b>")
        self.notebook.append_page(self.page3, rawDataLabel)

        # Console Area
        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        self.page4.add(Gtk.Label('No message.'))
        consoleAreaLabel = Gtk.Label()
        consoleAreaLabel.set_markup("<b>Console Area</b>")
        self.notebook.append_page(self.page4, consoleAreaLabel)

window = ConsoleAreaWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()


store = Gtk.ListStore(str, str, str, str, str, str)

treeiter = store.append(["Number", "Time", "Source", "Destination", "Length", "Info"])
