from Tkinter import *
import Tkinter as tk
import ttk

class packetStreamArea(Toplevel):

    def __init__(self, main):

        Toplevel.__init__(self, width=180, height=160)
        self.title("Packet Stream Area")
        packetStreamFrame = Frame(self)
        packetStreamFrame.pack(fill=BOTH, expand=1)

        frameButton = tk.Frame(packetStreamFrame, width=100, height=100)
        frameButton.grid(row=0, sticky='nsew')

        self.treeview_frame = tk.Frame(packetStreamFrame, width=100, height=100)
        self.treeview_frame.grid(row=1, sticky='nsew')

        self.treeview = ttk.Treeview(self.treeview_frame)
        self.treeview.pack(fill='both', expand=True)

        # List of tuples for each packet stream, containing the number, time, source, destination, protocol, and info
        packets_list = [("102", "11:23.76", "192.168.0.31", "192.168.0.28", "SNMP",
                         "get-response SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.7.1"),
                        ("103", "11:23.96", "192.168.0.28", "192.168.0.31", "SNMP",
                         "get-request SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.8.1"),
                        ("104", "11:24.03", "192.168.0.31", "192.168.0.28", "SNMP",
                         "get-response SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.8.1"),
                        ("105", "11:24.50", "192.168.0.1", "192.168.0.1", "DNS", "Standard query www.google.com"),
                        ("106", "11:24.59", "192.168.0.1", "192.168.0.28", "DNS",
                         "Standard query response A 64.236.91.21 A 64.236.91.23 A 64.23"),
                        ("107", "11:24.75", "192.168.0.28", "64.236.91.21", "TCP",
                         "56606 > http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2"),
                        ("108", "11:24.84", "64.236.91.21", "192.168.0.28", "TCP",
                         "http > 56606 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460"),
                        ("109", "11:25.02", "192.168.0.28", "64.236.91.21", "TCP",
                         "56606 > http [ACK] Seq=1 Ack=1 Win=17520 Len=0"),
                        ("110", "11:25.17", "192.168.0.28", "64.236.91.21", "HTTP", "GET / HTTP/1.1"),
                        ("111", "11:25.30", "64.236.91.21", "192.168.0.28", "TCP",
                         "http > 56606 [ACK] Seq=1 Ack=845 Win=6960 Len=0"),
                        ("112", "11:25.52", "64.236.91.21", "192.168.0.28", "TCP",
                         "[TCP segment of a reassembled PDU]"),
                        ("113", "11.25.80", "64.236.91.21", "192.168.0.28", "TCP",
                         "[TCP segment of a reassembled PDU]")]

        self.treeview['columns'] = ('No.', 'Time', 'Source', 'Destination', 'Protocol', 'Info')

        # Window min, max, close button, and title
        title = tk.Label(frameButton, text="Packet Stream Area", font='System 14 bold', background='lightblue')
        title.grid(row=0, column=0)

        minimize = tk.Button(frameButton, text="_", bg="lightblue")
        minimize.grid(row=0, column=1)

        maximize = tk.Button(frameButton, text="[ ]", bg='lightblue')
        maximize.grid(row=0, column=2)

        close = tk.Button(frameButton, text="X", bg='lightblue')
        close.grid(row=0, column=3)

        # supress the unused identifier column (first column) and keep it out of view
        self.treeview['show'] = 'headings'

        # set up heading and column for the parent tree view: No.
        self.treeview.heading('No.', text='No.', anchor='w')
        self.treeview.column('No.', anchor='w', width=75)

        # set up heading and column for 'Time'
        self.treeview.heading('Time', text='Time')
        self.treeview.column('Time', anchor='w', width=100)

        # set up heading and column for 'Source'
        self.treeview.heading('Source', text='Source')
        self.treeview.column('Source', anchor='w', width=100)

        # set up heading and column for 'Destination'
        self.treeview.heading('Destination', text='Destination')
        self.treeview.column('Destination', anchor='w', width=100)

        # set up heading and column for 'Protocol'
        self.treeview.heading('Protocol', text='Protocol')
        self.treeview.column('Protocol', anchor='w', width=50)

        # set up heading and column for 'Info'
        self.treeview.heading('Info', text='Info')
        self.treeview.column('Info', anchor='w', width=100)

        # populate table
        for packet in packets_list:
            self.treeview.insert('', 'end',
                                 values=((packet[0]), (packet[1]), (packet[2]), (packet[3]), (packet[4]), (packet[5])))

