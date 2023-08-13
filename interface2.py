from tkinter import *
from PIL import ImageTk, Image
window = Tk()
window.title("Whether App")


l1 = Label(window,text="FREQUENTLY UPDATE WHETHER INFORMATION", fg="blue",bg="yellow")
l1.pack()

img = PhotoImage(file = "images/logo2.png")
l2 = Label(window, image = img, )
l2.place(x = 480, y = 70)
# l2.pack()


import requests
import json 

v = StringVar()


def action():
    city = v.get()
    url = 'http://api.weatherapi.com/v1/current.json?key=638ba7c08aa4460794393515231104&q=' + city


    data = requests.get(url) 
    df = json.loads(data.content)
    l5.config(text = df['current']['temp_c'],)
    l6.config(text = df['current']['temp_f'])
    l7.config(text = df['current']['last_updated'])
    l8.config(text = df['current']['humidity'])
    l9.config(text = df['location']['country'])

l4 = Button(window,text="Submit",fg="yellow",bg="green", command = action)
l4.place(x=820,y=505)

l3 = Entry(window, font=("corbel",18),bd=5,textvariable = v)
l3.place(x = 550, y = 500)



l5 = Label(window, text = "Temprature in Celcius: ", bg = "yellow", fg = "black")
l5.place(x=400, y=300)

l6 = Label(window, text = "Temprature in Farhenheight: ", bg = "yellow", fg = "black")
l6.place(x=400, y=400)

l7 = Label(window, text = "Temprature Last_updated: ", bg = "yellow", fg = "black")
l7.place(x=400, y=500)

l8 = Label(window, text = "Humidity: ", bg = "yellow", fg = "black")
l8.place(x=400, y=600)

l9 = Label(window, text = "Country: ", bg = "yellow", fg = "black")
l9.place(x=400, y=200)


# img = PhotoImage(file = "images/logo2.png")
# l10 = Label(window, image = img, )
# l10.place(x = 200, y = 70)

window.mainloop()