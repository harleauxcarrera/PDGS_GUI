from Tkinter import *

class DragManager():

    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        pass

    def on_drag(self, event):
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        button = Button(target, text="BUTTTTONNN", command=openFieldWindow)
        print("Dragged to x ",x," and y ",y)
        try:
            target.create_window(x-260, y-125, window=button)
        except:
            pass

class FieldDragManager():

    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        pass

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        button = Button(target, text="Field1Byte", command=openFieldWindow)
        print("Dragged to x ",x," and y ",y)
        try:
            #target.create_rectangle(x-10-260, y-5-125, x+10-260, y+5-125, fill="blue")
            target.create_window(x-260, y-125, window=button)
        except:
            pass