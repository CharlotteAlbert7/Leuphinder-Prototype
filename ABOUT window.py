import tkinter as tk
from PIL import Image, ImageTk


def open_about_window():
    about_win = tk.Tk()
    about_win.title("Login")
    # Add your code to create the schedule window

def destroy_win():
    win.destroy()
    open_about_window()

path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\logo.jpg'

win = tk.Tk()
win.title("ABOUT")
win.resizable(0, 0)
win.geometry('400x700')
win.configure(bg="#7d212a")

python_image = Image.open(path)
resized_image = python_image.resize((400, 700), Image.LANCZOS)
tkinter_image = ImageTk.PhotoImage(resized_image)

label = tk.Label(win, image=tkinter_image)
label.grid()

title_label1 = tk.Label(win, text="ABOUT", font=("Aleo", 50), bg="#7f3536", fg="white")
title_label1.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

title_label2 = tk.Label( text="Leuphinder is an app designed for university students seeking study buddies to enjoy project work, study time, or break time together.", font=(
        "Aleo", 14), bg="#7f3536", fg="white", wraplength=350)
title_label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

title_label3 = tk.Label(text="An app to make new friends with similar interests on campus. Just enter your preferred time slot and activity to enjoy time with a potential study buddy, and the app will match you with a student to meet on campus with just a few clicks.", font=(
        "Aleo", 14), bg="#7f3536", fg="white", wraplength=350)
title_label3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

return_button = tk.Button(win, text="                      Return                     ", bg="#740031", fg="white", font=("Aleo", 12), command=destroy_win)
return_button.place(relx=0.5, rely=0.8, anchor=tk.S)

win.mainloop()