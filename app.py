from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

def generate():
    link=entry1.get()
    file_name=entry.get()+".png"
    url=pyqrcode.create(link)
    url.png(file_name, scale= 6)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200, 450, window=image_label)


root=Tk()

canvas=Canvas(root, width=400, height=600)
canvas.pack()

app_label=Label(root, text="QR Code Generator", fg='blue', font=("Arial", 20))
canvas.create_window(200, 50, window=app_label)
label1=Label(root, text="Enter the link you want to convert")
canvas.create_window(200, 100, window=label1)
entry1=Entry(root)
canvas.create_window(250, 100, window=entry1)

label=Label(root, text="Enter the name you want to save the QR code with")
canvas.create_window(200, 130, window=label)
entry=Entry(root)
canvas.create_window(250, 130, window=entry)

button=Button(text="Generate QR code", command=generate)
canvas.create_window(200, 230, window=button)
root.mainloop()