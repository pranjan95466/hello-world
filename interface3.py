from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
# win.geometry(700 250)

# Set the size of the tkinter window
image = Image.open('images/logo2.png')

# Resize the image in the given (width, height)
img = image.resize((550, 450))

# Resize the image in the given (width, height)
my_image = ImageTk.PhotoImage(img)

label=Label(win, image = my_image)
label.pack()


win.mainloop()