import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class BuilderWindow(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Builder Area")

		self.set_border_width(10)

		self.set_default_size(800,400)

		mainBuilderBox = Gtk.Box(spacing=10)
		self.add(mainBuilderBox)

		CanvasLabel = Gtk.Label("Builder Canvas")

		mainBuilderBox.pack_start(CanvasLabel, True, False, 0)

		optionBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		mainBuilderBox.pack_start(optionBox, False, False, 0)

		optionsStack = Gtk.Stack()
		optionsStack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		optionsStack.set_transition_duration(1000)

		#######################################################

		fieldBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		optionsStack.add_titled(fieldBox, "fields", "Field")

		startFieldButton = Gtk.Button("Start Field")
		fieldBox.pack_start(startFieldButton, False, False, 0)

		field1ByteButton = Gtk.Button("Field (1 byte)")
		fieldBox.pack_start(field1ByteButton, False, False, 0)

		field2ByteButton = Gtk.Button("Field (2 byte)")
		fieldBox.pack_start(field2ByteButton, False, False, 0)

		field4ByteButton = Gtk.Button("Field (4 byte)")
		fieldBox.pack_start(field4ByteButton, False, False, 0)

		field8ByteButton = Gtk.Button("Field (8 byte)")
		fieldBox.pack_start(field8ByteButton, False, False, 0)

		field16ByteButton = Gtk.Button("Field (16 byte)")
		fieldBox.pack_start(field16ByteButton, False, False, 0)

		fieldVarSizeButton = Gtk.Button("Field (Var Size)")
		fieldBox.pack_start(fieldVarSizeButton, False, False, 0)

		endFieldButton = Gtk.Button("End Field")
		fieldBox.pack_start(endFieldButton, False, False, 0)

		referenceListButton = Gtk.Button("Reference List")
		fieldBox.pack_start(referenceListButton, False, False, 0)

		packetInfoButton = Gtk.Button("Packet Info")
		fieldBox.pack_start(packetInfoButton, False, False, 0)

		########################################################

		constructorBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		optionsStack.add_titled(constructorBox, "constructors", "Construct")

		expressionButton = Gtk.Button("Expression")
		constructorBox.pack_start(expressionButton, False, False, 0)

		connectorButton = Gtk.Button("Connector")
		constructorBox.pack_start(connectorButton, False, False, 0)

		relationalOperatorBox = Gtk.Box(spacing=10)
		lessThanButton = Gtk.Button("<")
		relationalOperatorBox.pack_start(lessThanButton, False, False, 0)
		greaterThanButton = Gtk.Button(">")
		relationalOperatorBox.pack_start(greaterThanButton, False, False, 0)
		lessThanEqualButton = Gtk.Button("<=")
		relationalOperatorBox.pack_start(lessThanEqualButton, False, False, 0)
		greaterThanEqualButton = Gtk.Button(">=")
		relationalOperatorBox.pack_start(greaterThanEqualButton, False, False, 0)
		equalButton = Gtk.Button("==")
		relationalOperatorBox.pack_start(equalButton, False, False, 0)
		notEqualButton = Gtk.Button("~=")
		relationalOperatorBox.pack_start(notEqualButton, False, False, 0)
		constructorBox.pack_start(relationalOperatorBox, False, False, 0)

		logicalOperatorBox = Gtk.Box(spacing=10)
		andButton = Gtk.Button("And")
		logicalOperatorBox.pack_start(andButton, True, False, 0)
		orButton = Gtk.Button("Or")
		logicalOperatorBox.pack_start(orButton, True, False, 0)
		notButton = Gtk.Button("Not")
		logicalOperatorBox.pack_start(notButton, True, False, 0)
		constructorBox.pack_start(logicalOperatorBox, False, False, 0)

		operandButton = Gtk.Button("Operand")
		constructorBox.pack_start(operandButton, False, False, 0)

		########################################################

		optionsSwitcher = Gtk.StackSwitcher()
		optionsSwitcher.set_stack(optionsStack)
		optionBox.pack_start(optionsSwitcher, True, False, 0)
		optionBox.pack_start(optionsStack, False, False, 0)



win = BuilderWindow()
win.show_all()
win.connect("destroy", Gtk.main_quit)
Gtk.main()