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

        #THIS IS THE TREE VIEW COMPONENT SKELETON USED FOR DISPLAYING THE PACKET DATA #
        self.liststore = Gtk.ListStore(str, str, str,str,str,str)
        self.liststore.append(["366", "11.76722903","192.168.0.3","192.168.0.2","TCP","get-response-SNMP2"])
        self.liststore.append(["367", "11.76729345","192.168.0.4","192.168.0.3","TCP","get-response-SNMP2"])
        self.liststore.append(["369", "11.76345903","192.168.0.8","192.168.0.3","TCP","get-response-SNMP2"])
        self.liststore.append(["400", "11.76342903","192.168.0.36","192.168.0.36","SNMP","http_request_query"])
        self.liststore.append(["420", "11.76355903","192.168.0.37","192.168.0.3","SNMP","http_request_query"])
        self.liststore.append(["460", "11.76545903","192.168.0.4","192.168.0.3","SNMP","http_request_query"])
        self.liststore.append(["780", "11.76344903","192.168.0.1","192.168.0.3","HTTP","http_request_query"])
        treeview = Gtk.TreeView(model=self.liststore)

        number = Gtk.CellRendererText()
        col1 = Gtk.TreeViewColumn("No.", number, text=0)
        treeview.append_column(col1)

        time = Gtk.CellRendererText()
        col2 = Gtk.TreeViewColumn("Time                    ", time, text=1)
        treeview.append_column(col2)

        source = Gtk.CellRendererText()
        col3 = Gtk.TreeViewColumn("Source                     ", source, text=2)
        treeview.append_column(col3)

        dest = Gtk.CellRendererText()
        col4 = Gtk.TreeViewColumn("Destination                                      ", dest, text=3)
        treeview.append_column(col4)

        protocol = Gtk.CellRendererText()
        col5 = Gtk.TreeViewColumn("Protocol", protocol, text=4)
        treeview.append_column(col5)

        description = Gtk.CellRendererText()
        col6 = Gtk.TreeViewColumn("Text Description                                                 ", description, text=5)
        treeview.append_column(col6)






        # renderer_editabletext = Gtk.CellRendererText()
        # renderer_editabletext.set_property("editable", True)
        #
        # text_descritption = Gtk.TreeViewColumn("Text Description",
        #     renderer_editabletext, text=5)
        # treeview.append_column(column_editabletext)
        #
        # renderer_editabletext.connect("edited", self.text_edited)


        #
        # Number time source destination protcol info

        # Packet Stream Area View
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(treeview)


        packetCaptureLabel = Gtk.Label()
        packetCaptureLabel.set_markup("<b>Packet Stream Area View</b>")
        self.notebook.append_page(self.page1, packetCaptureLabel)

        # Dissected Stream Area View
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)

        #***********LIST COMPONENT***************
    	store = Gtk.TreeStore(str)

        row1 = store.append(None, ['User Datagram Protocol, SRC Port: Domain (53) , Dest Port: Dest (420)        '])
        store.append(row1, ['[Request In: 38]'])
        store.append(row1, ['Time: 0.0025777 seconds'])
        store.append(row1, ['Transaction ID: 0xcf1f'])



        row2 = store.append(None, ['Domain Name System (response)        '])
        store.append(row2, ['[Request In: 38]'])
        store.append(row2, ['Time: 0.0025777 seconds'])
        store.append(row2, ['Transaction ID: 0xcf1f'])
        store.append(row2, ['Flags: 0x867 (Standard query response , No error)'])
        store.append(row2, ['Questions:1'])
        store.append(row2, ['Answers RRS: 6'])
        store.append(row2, ['Authority RRS:0'])
        store.append(row2, ['Additional RRS:0'])

        row3 = store.append(None, ['Queries'])
        store.append(row3, ['www.cnn.com: type A, Class IN'])

        treeView = Gtk.TreeView(store)
        treeViewColumn = Gtk.TreeViewColumn('Project')
        treeView.append_column(treeViewColumn)

        cell = Gtk.CellRendererText()
        treeViewColumn.pack_start(cell, True)
        treeViewColumn.add_attribute(cell, 'text', 0)
        self.page2.add(treeView)

        #************LIST COMPONENT************
        dissectedStreamLabel = Gtk.Label()
        dissectedStreamLabel.set_markup("<b>Dissected Stream Area View</b>")
        self.notebook.append_page(self.page2, dissectedStreamLabel)

        # Raw Data Area View
        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)

        #***********LIST COMPONENT***************
    	store = Gtk.TreeStore(str)

        row1 = store.append(None, ['User Datagram Protocol, SRC Port: Domain (53) , Dest Port: Dest (420)        '])
        store.append(row1, ['[Request In: 38]'])
        store.append(row1, ['Time: 0.0025777 seconds'])
        store.append(row1, ['Transaction ID: 0xcf1f'])



        row2 = store.append(None, ['Domain Name System (response)        '])
        store.append(row2, ['[Request In: 38]'])
        store.append(row2, ['Time: 0.0025777 seconds'])
        store.append(row2, ['Transaction ID: 0xcf1f'])
        store.append(row2, ['Flags: 0x867 (Standard query response , No error)'])
        store.append(row2, ['Questions:1'])
        store.append(row2, ['Answers RRS: 6'])
        store.append(row2, ['Authority RRS:0'])
        store.append(row2, ['Additional RRS:0'])

        row3 = store.append(None, ['Queries'])
        store.append(row3, ['www.cnn.com: type A, Class IN'])

        treeView = Gtk.TreeView(store)
        treeViewColumn = Gtk.TreeViewColumn('Project')
        treeView.append_column(treeViewColumn)

        cell = Gtk.CellRendererText()
        treeViewColumn.pack_start(cell, True)
        treeViewColumn.add_attribute(cell, 'text', 0)
        self.page3.add(treeView)

        #************LIST COMPONENT************

        rawDataLabel = Gtk.Label()
        rawDataLabel.set_markup("<b>Raw Data Area View</b>")
        self.notebook.append_page(self.page3, rawDataLabel)

        # Console Area
        self.page4 = Gtk.Box()
        self.page4.set_border_width(10)
        label = Gtk.Label("No Error at this Moment.")
        self.page4.add(label)
        consoleAreaLabel = Gtk.Label()
        consoleAreaLabel.set_markup("<b>Console Area</b>")
        self.notebook.append_page(self.page4, consoleAreaLabel)

    def on_add_clicked(self, button):
        print("New field was created")
        self.destroy()








window = ConsoleAreaWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
