import tkinter as tk
from PIL import Image, ImageTk

def open_noluck_window():
    noluck_win = tk.Tk()
    noluck_win.title("Mainpage")
    win.destroy()
    # Add code to create the schedule window

def destroy_win():
    win.destroy()

path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\logo.jpg'

win = tk.Tk()
win.title("No luck!")
win.resizable(0, 0)
win.geometry('400x450')

python_image = Image.open(path)

resized_image = python_image.resize((400, 700), Image.LANCZOS)

tkinter_image = ImageTk.PhotoImage(resized_image)

label = tk.Label(image=tkinter_image)
label.grid()

title_label1 = tk.Label(text="No luck!", font=("Aleo", 50), bg="#7f3536", fg="white")
title_label1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

title_label2 = tk.Label(text="TRY AGAIN LATER", font=("Aleo", 12), bg="#7f3536", fg="white")
title_label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

tryagain_button = tk.Button(text="                              Try again                                ", bg="#740031", fg="white", command=open_noluck_window)
tryagain_button.place(relx=0.5, rely=0.7, anchor=tk.S)

cancel_button = tk.Button(text="                                 Cancel                                 ", bg="#740031", fg="white", command=destroy_win)
cancel_button.place(relx=0.5, rely=0.8, anchor=tk.S)

win.mainloop()