import tkinter as tk
from PIL import Image, ImageTk

def destroy_win():
    win.destroy()

def create_mainpage_window():
    destroy_win()  # Close the current window
    mainpage_win = tk.Tk()
    mainpage_win.title("Main Page")

def open_windowmainpage():
    win.destroy()

def open_main_page():
    create_mainpage_window()

win = tk.Tk()
win.title("Login")
win.geometry("390x540")
win.configure(bg="#7d212a")
win.resizable(0, 0)

title_label = tk.Label(text="Leuphinder Login", fg="white", font=("Aleo", 32), bg="#7d212a")
title_label.grid(row=1, column=0, columnspan=3, sticky="ew", padx=25)

name_label = tk.Label(text="Name", fg="white", bg="#7d212a", font="Aleo")
name_label.grid(row=5, column=0, padx=20, pady=10, sticky="nw")

name_entry = tk.Entry(fg="black", bg="white", font="Aleo")
name_entry.grid(row=5, column=1, columnspan=2, padx=(5, 20), pady=10, sticky="nw")

email_label = tk.Label(text="E-mail", fg="white", bg="#7d212a", font="Aleo")
email_label.grid(row=7, column=0, padx=20, pady=10, sticky="nw")

email_entry = tk.Entry(fg="black", bg="white", font="Aleo")
email_entry.grid(row=7, column=1, columnspan=2, padx=(5, 20), pady=10, sticky="nw")

password_label = tk.Label(text="Password", fg="white", bg="#7d212a", font="Aleo")
password_label.grid(row=9, column=0, padx=20, pady=10, sticky="nw")

password_entry = tk.Entry(fg="black", bg="white", font="Aleo")
password_entry.grid(row=9, column=1, columnspan=2, padx=(5, 20), pady=10, sticky="nw")

cancel_button = tk.Button(text="Cancel", fg="white", bg="#740031", command=destroy_win)
cancel_button.grid(row=11, column=0, columnspan=3, pady=10, padx=5, sticky="nsew")

start_button = tk.Button(text="Start", fg="white", bg="#740031", command=open_main_page)
start_button.grid(row=10, column=0, columnspan=3, pady=10, padx=5, sticky="nsew")

# Load and display the logo
logo_image = Image.open(r"C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\logo.jpg")
logo_image = logo_image.resize((90, 90), Image.LANCZOS)
tk_logo_image = ImageTk.PhotoImage(logo_image)

# Create a separate label to hold the logo
logo_label = tk.Label(image=tk_logo_image, bg="#7d212a")
logo_label.grid(row=0, column=0, columnspan=3, pady=10)

# Make the logo clickable
logo_label.bind("<Button-1>", lambda event: open_main_page())

win.mainloop()