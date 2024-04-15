import tkinter as tk
from PIL import Image, ImageTk

def open_map_window():
    map_window = tk.Tk()
    map_window.title("Map")
    win.destroy()
    # Add your code to create the schedule window

def destroy_win():
    win.destroy()

path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\Profile window.jpg'

win = tk.Tk()
win.title("It´s a match!")
win.resizable(0, 0)
win.geometry('400x700')

python_image = Image.open(path)

resized_image = python_image.resize((400, 700), Image.LANCZOS)

tkinter_image = ImageTk.PhotoImage(resized_image)

label = tk.Label(image=tkinter_image)
label.grid()

title_label1 = tk.Label(text="It´s a match!", font=("Aleo", 50), bg="#7f3536", fg="white")
title_label1.place(relx=0.5, rely=0.23, anchor=tk.CENTER)

title_label2 = tk.Label(text="SOMEONE WANTS TO MEET YOU", font=("Aleo", 12), bg="#7f3536", fg="white")
title_label2.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

name_label = tk.Label(text="Name:", font=("Aleo", 12), bg="#7f3536", fg="white")
name_label.place(relx=0.3, rely=0.7, anchor=tk.E)

email_label = tk.Label(text="E-mail:", font=("Aleo", 12), bg="#7f3536", fg="white")
email_label.place(relx=0.305, rely=0.75, anchor=tk.E)

location_label = tk.Label(text="Location:", font=("Aleo", 12), bg="#7f3536", fg="white")
location_label.place(relx=0.34, rely=0.8, anchor=tk.E)

connect_button = tk.Button(text="                               Find my Study Buddy on the MAP                              ", bg="#740031", fg="white", command=open_map_window)
connect_button.place(relx=0.5, rely=0.9, anchor=tk.S)

cancel_button = tk.Button(text="                                                        Cancel                                                      ", bg="#740031", fg="white", command=destroy_win)
cancel_button.place(relx=0.5, rely=0.95, anchor=tk.S)

win.mainloop()