import tkinter as tk
from PIL import Image, ImageTk

def open_map_win():
    win.destroy()  # Close the current window
    map_win = tk.Tk()
    map_win.title("Map")
    # Add your code to create the map window

def destroy_win():
    win.destroy()

path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\map.jpg'

win = tk.Tk()
win.title("Map")
win.resizable(0, 0)  # Disable window resizing
win.geometry('400x500')

python_image = Image.open(path)

resized_image = python_image.resize((400, 700), Image.LANCZOS)  # Fix resize dimensions

tkinter_image = ImageTk.PhotoImage(resized_image)

label = tk.Label(win, image=tkinter_image)
label.grid()

title_label = tk.Label(win, text="Find my Buddy - on the map", font=("Aleo", 14), bg="#740031", fg="white")
title_label.place(x=10, y=10, anchor=tk.NW)

return_button = tk.Button(win, text="                                                        Return                                                         ", bg="#740031", fg="white", command=open_map_win)
return_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

win.mainloop()