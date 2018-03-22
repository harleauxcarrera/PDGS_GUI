import gi
import Field as Field
import startField as startField
import endField as endField
import refListField as refListField
import packetInfo as packetInfo
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

DRAG_ACTION = Gdk.DragAction.COPY

class BuilderWindow(Gtk.Box):
	
	def __init__(self):
		Gtk.Box.__init__(self, spacing=10)

		self.set_border_width(10)

		targets = Gtk.TargetList.new([])
		targets.add_text_targets(1)

		CanvasLabel = Gtk.Label("Builder Canvas")
		CanvasLabel.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
		CanvasLabel.connect("drag-data-received", self.on_drag_data_received)
		CanvasLabel.drag_dest_set_target_list(targets)

		self.pack_start(CanvasLabel, True, True, 0)

		optionBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		self.pack_start(optionBox, False, False, 0)

		optionsStack = Gtk.Stack()
		optionsStack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
		optionsStack.set_transition_duration(1000)

		#######################################################
		#Field options fieldBoxMenu1

		fieldBox = Gtk.Box(spacing=10)
		optionsStack.add_titled(fieldBox, "fields", "Field")

		fieldBoxMenu1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		fieldBox.pack_start(fieldBoxMenu1, True, True, 0)

		startFieldButton = Gtk.Button("Start Field")
		fieldBoxMenu1.pack_start(startFieldButton, True, True, 0)
		startFieldButton.connect("clicked", self.startFieldClicked)
		startFieldButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		startFieldButton.drag_source_set_target_list(targets)
		startFieldButton.connect("drag-data-get", self.on_drag_data_get_startField)

		field1ByteButton = Gtk.Button("Field (1 byte)")
		fieldBoxMenu1.pack_start(field1ByteButton, False, False, 0)
		field1ByteButton.connect("clicked" , self.fieldClicked)
		field1ByteButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		field1ByteButton.drag_source_set_target_list(targets)
		field1ByteButton.connect("drag-data-get", self.on_drag_data_get_field)

		field2ByteButton = Gtk.Button("Field (2 byte)")
		fieldBoxMenu1.pack_start(field2ByteButton, False, False, 0)
		field2ByteButton.connect("clicked" , self.fieldClicked)
		field2ByteButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		field2ByteButton.drag_source_set_target_list(targets)
		field2ByteButton.connect("drag-data-get", self.on_drag_data_get_field)

		field4ByteButton = Gtk.Button("Field (4 byte)")
		fieldBoxMenu1.pack_start(field4ByteButton, False, False, 0)
		field4ByteButton.connect("clicked" , self.fieldClicked)
		field4ByteButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		field4ByteButton.drag_source_set_target_list(targets)
		field4ByteButton.connect("drag-data-get", self.on_drag_data_get_field)

		field8ByteButton = Gtk.Button("Field (8 byte)")
		fieldBoxMenu1.pack_start(field8ByteButton, False, False, 0)
		field8ByteButton.connect("clicked" , self.fieldClicked)
		field8ByteButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		field8ByteButton.drag_source_set_target_list(targets)
		field8ByteButton.connect("drag-data-get", self.on_drag_data_get_field)

		fieldBoxMenu2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		fieldBox.pack_start(fieldBoxMenu2, True, True, 0)

		field16ByteButton = Gtk.Button("Field (16 byte)")
		fieldBoxMenu2.pack_start(field16ByteButton, False, False, 0)
		field16ByteButton.connect("clicked" , self.fieldClicked)
		field16ByteButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		field16ByteButton.drag_source_set_target_list(targets)
		field16ByteButton.connect("drag-data-get", self.on_drag_data_get_field)

		fieldVarSizeButton = Gtk.Button("Field (Var Size)")
		fieldBoxMenu2.pack_start(fieldVarSizeButton, False, False, 0)
		fieldVarSizeButton.connect("clicked" , self.fieldClicked)
		fieldVarSizeButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		fieldVarSizeButton.drag_source_set_target_list(targets)
		fieldVarSizeButton.connect("drag-data-get", self.on_drag_data_get_field)

		endFieldButton = Gtk.Button("End Field")
		fieldBoxMenu2.pack_start(endFieldButton, False, False, 0)
		endFieldButton.connect("clicked", self.endFieldClicked)
		endFieldButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		endFieldButton.drag_source_set_target_list(targets)
		endFieldButton.connect("drag-data-get", self.on_drag_data_get_endField)

		referenceListButton = Gtk.Button("Reference List")
		fieldBoxMenu2.pack_start(referenceListButton, False, False, 0)
		referenceListButton.connect("clicked", self.refListClicked)
		referenceListButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		referenceListButton.drag_source_set_target_list(targets)
		referenceListButton.connect("drag-data-get", self.on_drag_data_get_refList)

		packetInfoButton = Gtk.Button("Packet Info")
		fieldBoxMenu2.pack_start(packetInfoButton, False, False, 0)
		packetInfoButton.connect("clicked", self.packetInfoClicked)
		packetInfoButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		packetInfoButton.drag_source_set_target_list(targets)
		packetInfoButton.connect("drag-data-get", self.on_drag_data_get_packetInfo)

		########################################################
		#Construct options menu

		constructorBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
		optionsStack.add_titled(constructorBox, "constructors", "Construct")

		expressionButton = Gtk.Button("Expression")
		constructorBox.pack_start(expressionButton, False, False, 0)
		expressionButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		expressionButton.drag_source_set_target_list(targets)
		expressionButton.connect("drag-data-get", self.on_drag_data_get_expression)

		connectorButton = Gtk.Button("Connector")
		constructorBox.pack_start(connectorButton, False, False, 0)
		connectorButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		connectorButton.drag_source_set_target_list(targets)
		connectorButton.connect("drag-data-get", self.on_drag_data_get_connector)

		relationalOperatorBox = Gtk.Box(spacing=10)
		lessThanButton = Gtk.Button("<")
		relationalOperatorBox.pack_start(lessThanButton, False, False, 0)
		lessThanButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		lessThanButton.drag_source_set_target_list(targets)
		lessThanButton.connect("drag-data-get", self.on_drag_data_get_relationalOperator)

		greaterThanButton = Gtk.Button(">")
		relationalOperatorBox.pack_start(greaterThanButton, False, False, 0)
		greaterThanButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		greaterThanButton.drag_source_set_target_list(targets)
		greaterThanButton.connect("drag-data-get", self.on_drag_data_get_relationalOperator)

		lessThanEqualButton = Gtk.Button("<=")
		relationalOperatorBox.pack_start(lessThanEqualButton, False, False, 0)
		lessThanEqualButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		lessThanEqualButton.drag_source_set_target_list(targets)
		lessThanEqualButton.connect("drag-data-get", self.on_drag_data_get_relationalOperator)

		greaterThanEqualButton = Gtk.Button(">=")
		relationalOperatorBox.pack_start(greaterThanEqualButton, False, False, 0)
		greaterThanEqualButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		greaterThanEqualButton.drag_source_set_target_list(targets)
		greaterThanEqualButton.connect("drag-data-get", self.on_drag_data_get_relationalOperator)

		equalButton = Gtk.Button("==")
		relationalOperatorBox.pack_start(equalButton, False, False, 0)
		equalButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		equalButton.drag_source_set_target_list(targets)
		equalButton.connect("drag-data-get", self.on_drag_data_get_relationalOperator)

		notEqualButton = Gtk.Button("~=")
		relationalOperatorBox.pack_start(notEqualButton, False, False, 0)
		notEqualButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		notEqualButton.drag_source_set_target_list(targets)
		notEqualButton.connect("drag-data-get", self.on_drag_data_get_relationalOperator)

		constructorBox.pack_start(relationalOperatorBox, False, False, 0)

		logicalOperatorBox = Gtk.Box(spacing=10)
		andButton = Gtk.Button("And")
		logicalOperatorBox.pack_start(andButton, True, False, 0)
		andButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		andButton.drag_source_set_target_list(targets)
		andButton.connect("drag-data-get", self.on_drag_data_get_logicalOperator)

		orButton = Gtk.Button("Or")
		logicalOperatorBox.pack_start(orButton, True, False, 0)
		orButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		orButton.drag_source_set_target_list(targets)
		orButton.connect("drag-data-get", self.on_drag_data_get_logicalOperator)

		notButton = Gtk.Button("Not")
		logicalOperatorBox.pack_start(notButton, True, False, 0)
		notButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		notButton.drag_source_set_target_list(targets)
		notButton.connect("drag-data-get", self.on_drag_data_get_logicalOperator)

		constructorBox.pack_start(logicalOperatorBox, False, False, 0)

		operandButton = Gtk.Button("Operand")
		constructorBox.pack_start(operandButton, False, False, 0)
		operandButton.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
		operandButton.drag_source_set_target_list(targets)
		operandButton.connect("drag-data-get", self.on_drag_data_get_operand)

		########################################################

		optionsSwitcher = Gtk.StackSwitcher()
		optionsSwitcher.set_stack(optionsStack)
		optionBox.pack_start(optionsSwitcher, True, False, 0)
		optionBox.pack_start(optionsStack, False, False, 0)

	def startFieldClicked(self, button):
		print("Open Start Field Window")
		win2 = startField.startFieldWindow()
		win2.connect("destroy", Gtk.main_quit)
		win2.show_all()
		Gtk.main()

	def fieldClicked(self, button):
		print("Open Field Window")
		win2 = Field.fieldWindow()
		win2.connect("destroy", Gtk.main_quit)
		win2.show_all()
		Gtk.main()

	def endFieldClicked(self, button):
		print("Open End Field Window")
		win2 = endField.endFieldWindow()
		win2.connect("destroy", Gtk.main_quit)
		win2.show_all()
		Gtk.main()

	def refListClicked(self, button):
		print("Open Reference Field Window")
		win2 = refListField.refListFieldWindow()
		win2.connect("destroy", Gtk.main_quit)
		win2.show_all()
		Gtk.main()

	def packetInfoClicked(self, button):
		print("Open Packet Info Window")
		win2 = packetInfo.packetInfoWindow()
		win2.connect("destroy", Gtk.main_quit)
		win2.show_all()
		Gtk.main()

	def on_drag_data_get_startField(self, widget, drag_context, data, info, time):
		text = "Start field added"
		data.set_text(text, -1)

	def on_drag_data_get_field(self, widget, drag_context, data, info, time):
		text = "Field added"
		data.set_text(text, -1)

	def on_drag_data_get_endField(self, widget, drag_context, data, info, time):
		text = "End Field added"
		data.set_text(text, -1)

	def on_drag_data_get_refList(self, widget, drag_context, data, info, time):
		text = "Reference List added"
		data.set_text(text, -1)

	def on_drag_data_get_packetInfo(self, widget, drag_context, data, info, time):
		text = "Packet Info added"
		data.set_text(text, -1)

	def on_drag_data_get_expression(self, widget, drag_context, data, info, time):
		text = "Expression added"
		data.set_text(text, -1)

	def on_drag_data_get_connector(self, widget, drag_context, data, info, time):
		text = "Connector added"
		data.set_text(text, -1)

	def on_drag_data_get_relationalOperator(self, widget, drag_context, data, info, time):
		text = "Relational Operator added"
		data.set_text(text, -1)

	def on_drag_data_get_logicalOperator(self, widget, drag_context, data, info, time):
		text = "Logical Operator added"
		data.set_text(text, -1)

	def on_drag_data_get_operand(self, widget, drag_context, data, info, time):
		text = "Operand added"
		data.set_text(text, -1)

	def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
		text = data.get_text()
		print(text)


#For testing purposes
#win = Gtk.Window()
#buildBox = BuilderWindow()
#win.add(buildBox)
#win.connect("delete-event", Gtk.main_quit)
#win.show_all()
#Gtk.main()