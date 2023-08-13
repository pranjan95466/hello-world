from tkinter import *
window = Tk()
window.title("Whether App")
l1 = Label(window,text="FREQUENTLY UPDATE WHETHER INFORMATION", fg="blue",bg="red")
l1.grid()
l1.place(x=600, y=100)

l2 = Entry(window, font=("corbel",18),bd=5)
l2.place(x=600,y=200)

l3 = Button(window,text="Submit",fg="yellow",bg="green")
l3.place(x=600,y=300)
# window.minsize(width=200, height=400)
# window.maxsize(width=400, height=800)
window.mainloop()
