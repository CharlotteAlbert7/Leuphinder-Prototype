import tkinter as tk
from PIL import Image, ImageTk


def open_mainpage_win():
    mainpage_win = tk.Tk()
    mainpage_win.title("Mainpage")
    # Add your code to create the schedule window

def open_scheduler_win():
    global win
    win.destroy()
    scheduler_win = tk.Tk()
    scheduler_win.title("Find a Study Buddy")

def open_map_win():
    global win
    win.destroy()
    map_win = tk.Tk()
    map_win.title("Map")

path = r'C:\Users\lotti\Downloads\Beige Good Morning Instagram Story.jpg'

win = tk.Tk()
win.title("Mainpage")
win.resizable(0, 0)
win.geometry('400x700')
win.configure(bg="#7d212a")

python_image = Image.open(path)
resized_image = python_image.resize((400, 700), Image.LANCZOS)
tkinter_image = ImageTk.PhotoImage(resized_image)

label = tk.Label(win, image=tkinter_image)
label.grid()

findstudybuddy_button = tk.Button(text='Find a Study Buddy', bg='#740031', fg="white", font=("Aleo", "20"), command=open_scheduler_win)
findstudybuddy_button.place(relx=0.5, rely=0.85, anchor=tk.S)

label1 = tk.Label(text="AND MATCH WITH STUDENTS IN YOUR AREA", font=("ALEO", 7), bg="#1c1a25", fg="white")
label1.place(relx=0.5, rely=0.86, anchor=tk.CENTER)

map_button = tk.Button(text='                      MAP                       ', bg='#740031', font=("Aleo", "18"), command=open_map_win)
map_button.place(relx=0.5, rely=0.98, anchor=tk.S)

win.mainloop()