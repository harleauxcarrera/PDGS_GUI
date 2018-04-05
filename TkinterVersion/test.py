from Tkinter import *

root = Tk()
root.title("TESTTTTTT")
root.geometry("500x500")


def printName(event):
    print("Hello")

def printName2():
    print("Hello")


topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, fill=BOTH)

button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button3.bind("<Button-1>", printName)
button4 = Button(bottomFrame, text="Button 4", fg="purple", command=printName2)
one = Label(bottomFrame, text="One", bg="green")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(fill=BOTH)
one.pack(fill=BOTH)

root.mainloop()