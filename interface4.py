from tkinter import *
# from PIL import Image, ImageTk

window = Tk()
window.title("Weather App1")

img = PhotoImage(file = 'images/applogo.png')
label_1 = Label(window, image = img)
label_1.pack()

# img = Image.open('images/applogo.png')
# img = img.resize((550, 450))
# label_1 = Label(window, image = img)
# label_1.pack()
# my_image = ImageTk.PhotoImage(img)

window.mainloop()