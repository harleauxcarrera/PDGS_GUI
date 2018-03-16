import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio

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
        self.page1.add(Gtk.Image.new_from_file('PacketCapture.png'))
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
