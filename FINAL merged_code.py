import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Global variables
root = None
activity_var = None
name_entry = None
email_entry = None
password_entry = None
activity_var = None
time_var = None


def destroy_win():
    root.destroy()

def open_main_page():
    global root
    root.withdraw()  # Temporarily hide the login window
    mainpage_win = tk.Toplevel(root)
    mainpage_win.title("Main Page")
    mainpage_win.geometry("400x700")
    mainpage_win.resizable(0, 0)

    
    path = r'C:\Users\lotti\Downloads\Beige Good Morning Instagram Story.jpg'

    python_image = Image.open(path)
    resized_image = python_image.resize((400, 700), Image.LANCZOS)
    tkinter_image = ImageTk.PhotoImage(resized_image)

    label = tk.Label(mainpage_win, image=tkinter_image)
    label.image = tkinter_image
    label.pack()

    findstudybuddy_button = tk.Button(mainpage_win, text='Find a Study Buddy', bg='#740031', fg="white", font=(
        "Aleo", "20"), command=lambda: open_scheduler_win())
    findstudybuddy_button.place(relx=0.5, rely=0.85, anchor=tk.S)

    label1 = tk.Label(mainpage_win, text="AND MATCH WITH STUDENTS IN YOUR AREA", font=(
        "ALEO", 7), bg="#1c1a25", fg="white")
    label1.place(relx=0.5, rely=0.86, anchor=tk.CENTER)

    map_button = tk.Button(mainpage_win, text='                      MAP                       ',
                           bg='#740031', font=("Aleo", "18"), command=lambda: open_map_win())
    map_button.place(relx=0.5, rely=0.98, anchor=tk.S)


def open_about_window():
    about_win = tk.Toplevel(root)
    about_win.title("ABOUT")
    about_win.resizable(0, 0)
    about_win.geometry('400x700')
    about_win.configure(bg="#7f3536")

    path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\logo.jpg'

    python_image = Image.open(path)
    resized_image = python_image.resize((400, 700), Image.LANCZOS)
    tkinter_image = ImageTk.PhotoImage(resized_image)

    label = tk.Label(about_win, image=tkinter_image)
    label.grid()

    title_label1 = tk.Label(about_win, text="ABOUT", font=(
        "Aleo", 50), bg="#7f3536", fg="white")
    title_label1.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    title_label2 = tk.Label(about_win, text="Leuphinder is an app designed for university students seeking study buddies to enjoy project work, study time, or break time together.", font=(
        "Aleo", 14), bg="#7f3536", fg="white", wraplength=350)
    title_label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    title_label3 = tk.Label(about_win, text="An app to make new friends with similar interests on campus. Just enter your preferred time slot and activity to enjoy time with a potential study buddy, and the app will match you with a student to meet on campus with just a few clicks.", font=(
        "Aleo", 14), bg="#7f3536", fg="white", wraplength=350)
    title_label3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    return_button = tk.Button(about_win, text=" 	                  Return                                    ", bg="#740031", fg="white", font=(
        "Aleo", 12), command=lambda: (about_win.destroy(), root.deiconify()))
    return_button.place(relx=0.5, rely=0.8, anchor=tk.S)

def open_noluck_window():
    noluck_win = tk.Toplevel(root)
    noluck_win.title("No Match")
    noluck_win.resizable(0, 0)
    noluck_win.geometry('400x450')

    path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\logo.jpg'

    python_image = Image.open(path)
    resized_image = python_image.resize((400, 700), Image.LANCZOS)
    tkinter_image = ImageTk.PhotoImage(resized_image)

    label = tk.Label(noluck_win, image=tkinter_image)
    label.grid()

    title_label1 = tk.Label(noluck_win, text="No luck!", font=(
        "Aleo", 50), bg="#7f3536", fg="white")
    title_label1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    title_label2 = tk.Label(noluck_win, text="TRY AGAIN LATER", font=(
        "Aleo", 12), bg="#7f3536", fg="white")
    title_label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    tryagain_button = tk.Button(noluck_win, text="Try again", bg="#740031", fg="white", font=(
        "Aleo", 12), command=lambda: (noluck_win.destroy(), root.deiconify()))
    tryagain_button.place(relx=0.5, rely=0.7, anchor=tk.S)

    cancel_button = tk.Button(noluck_win, text="Cancel", bg="#740031", fg="white", font=(
        "Aleo", 12), command=destroy_win)
    cancel_button.place(relx=0.5, rely=0.8, anchor=tk.S)


def open_match_window(matched_name, matched_email):
    match_win = tk.Toplevel(root)
    match_win.title("It´s a match!")

    path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\Profile window.jpg'

    python_image = Image.open(path)
    resized_image = python_image.resize((400, 700), Image.LANCZOS)
    tkinter_image = ImageTk.PhotoImage(resized_image)

    label = tk.Label(match_win, image=tkinter_image)
    label.grid()

    title_label1 = tk.Label(match_win, text="It´s a match!", font=(
        "Aleo", 50), bg="#7f3536", fg="white")
    title_label1.place(relx=0.5, rely=0.23, anchor=tk.CENTER)

    title_label2 = tk.Label(match_win, text="SOMEONE WANTS TO MEET YOU", font=(
        "Aleo", 12), bg="#7f3536", fg="white")
    title_label2.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    name_label = tk.Label(match_win, text="Name:", font=(
        "Aleo", 12), bg="#7f3536", fg="white")
    name_label.place(relx=0.3, rely=0.6, anchor=tk.E)

    email_label = tk.Label(match_win, text="E-mail:", font=(
        "Aleo", 12), bg="#7f3536", fg="white")
    email_label.place(relx=0.305, rely=0.65, anchor=tk.E)

    # Display the matched name and email
    matched_name_label = tk.Label(match_win, text=matched_name, font=(
        "Aleo", 12), bg="#7f3536", fg="white")
    matched_name_label.place(relx=0.32, rely=0.6, anchor=tk.W)

    matched_email_label = tk.Label(match_win, text=matched_email, font=(
        "Aleo", 12), bg="#7f3536", fg="white")
    matched_email_label.place(relx=0.32, rely=0.65, anchor=tk.W)

    connect_button = tk.Button(match_win, text="Find my Study Buddy on the MAP",
                               bg="#740031", fg="white", command=open_map_win)
    connect_button.place(relx=0.5, rely=0.9, anchor=tk.S)

    cancel_button = tk.Button(match_win, text="Cancel",
                              bg="#740031", fg="white", command=destroy_win)
    cancel_button.place(relx=0.5, rely=0.95, anchor=tk.S)


def search_file():
    # Get the values of activity and time
    activity = activity_var.get()
    time = time_var.get()

    # File path
    file_path = r"C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\Records.txt"

    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the entire file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if the combination of activity and time exists in any entry
        global matched_name, matched_email
        match_found = False
        matched_name = None
        matched_email = None
        # Exclude the last entry (currently entered data)
        for i in range(0, len(lines)-5, 5):  # Each entry has 5 lines
            if lines[i+2].strip() == activity and lines[i+3].strip() == time:
                match_found = True
                matched_name = lines[i].strip()  # First line is name
                matched_email = lines[i+1].strip()  # Second line is email
                break

        # Display the appropriate window based on the match result
        if match_found:
            scheduler_win.destroy()
            open_match_window(matched_name, matched_email)
        else:
            scheduler_win.destroy()
            open_noluck_window()
    else:
        scheduler_win.destroy()
        open_noluck_window()  # File doesn't exist, so no match


def store_user_data():
    global name_entry, email_entry, activity_var, time_var

    # Get the values from the entry fields and variables
    name = name_entry.get()
    email = email_entry.get()
    activity = activity_var.get()
    time = time_var.get()

    # File path
    file_path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\Records.txt'

    # Check if the file exists
    if os.path.isfile(file_path):
        # Check if email exists in any line of the file
        email_exists = False
        with open(file_path, 'r') as file:
            for line in file:
                if email in line.split():
                    email_exists = True
                    break

        if email_exists:
            # Email exists, so we overwrite the line
            with open(file_path, 'r') as file:
                lines = file.readlines()
            with open(file_path, 'w') as file:
                for line in lines:
                    if email not in line.split():
                        file.write(line)
            with open(file_path, 'a') as file:
                file.write(f"{name}\n{email}\n{activity}\n{time}\n\n")
        else:
            # Email does not exist, so we append to a new line
            with open(file_path, 'a') as file:
                file.write(f"{name}\n{email}\n{activity}\n{time}\n\n")
    else:
        # File doesn't exist, create a new file and write data
        with open(file_path, 'w') as file:
            file.write(f"{name}\n{email}\n{activity}\n{time}\n\n")

    search_file()


def open_scheduler_win():
    global root, activity_var, scheduler_win
    root.withdraw()
    scheduler_win = tk.Toplevel(root)
    scheduler_win.title("Search for a Study Buddy")
    scheduler_win.geometry("350x300")
    scheduler_win.configure(bg="#7f3536")
    scheduler_win.resizable(0, 0)

    label1 = tk.Label(scheduler_win, text="Find a Study Buddy - Schedule for",bg='#740031', fg='white', font=("Aleo", 15))
    label1.grid(row=0, column=0, columnspan=2, sticky="w")

    label_activity = tk.Label(
        scheduler_win, text="ACTIVITY", bg='#7f3536', fg="white", font=("Aleo", 12, "bold"))
    label_activity.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    activity_var = tk.StringVar()
    activity_radio1 = ttk.Radiobutton(scheduler_win, text="Study", variable=activity_var, value="Study", command=show_study_combobox)
    activity_radio1.grid(row=2, column=0, padx=20, pady=2, sticky="w")

    activity_radio2 = ttk.Radiobutton(
        scheduler_win, text="Break", variable=activity_var, value="Break", command=show_break_combobox)
    activity_radio2.grid(row=3, column=0, padx=20, pady=2, sticky="w")

    global study_frame
    study_frame = tk.Frame(scheduler_win, bg="#7f3536")
    global break_frame
    break_frame = tk.Frame(scheduler_win, bg="#7f3536")

    global time_var, study_var, break_var

    study_var = tk.StringVar()
    study_combobox = ttk.Combobox(
        study_frame, textvariable=study_var)
    study_combobox['values'] = ("for a project", "for an exam", "in the library")
    study_combobox.current(0)
    study_combobox.grid(row=0, column=0, padx=10, pady=5)

    break_var = tk.StringVar()
    break_combobox = ttk.Combobox(
        break_frame, textvariable=break_var)
    break_combobox['values'] = (
        "go for lunch", "go outside e.g. for a walk", "in the city")
    break_combobox.current(0)
    break_combobox.grid(row=0, column=0, padx=10, pady=5)

    label_time = tk.Label(
        scheduler_win, text="TIME", bg='#7f3536', fg="white", font=("Aleo", 12, "bold"))
    label_time.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    time_var = tk.StringVar()
    time_combobox = ttk.Combobox(scheduler_win, textvariable=time_var)
    time_combobox['values'] = (
        'Today - 9am to 12pm',
        'Today - 12pm to 3pm',
        'Today - 3pm to 6pm',
        'Today - after 6pm',
        'Tomorrow - 9am to 12pm',
        'Tomorrow - 12pm to 3pm',
        'Tomorrow - 3pm to 6pm',
        'Tomorrow - after 6pm',
        'Next weekend'
    )
    time_combobox.current(0)
    time_combobox.grid(row=2, column=1, padx=10, pady=5)

    find_buddy_button = tk.Button(scheduler_win, text="Search", bg="#740031", fg="white", font=(
        "Aleo", 12), command=lambda: store_user_data())
    find_buddy_button.grid(
        row=10, column=0, columnspan=2, pady=(85, 0), padx=5, sticky="ew")

    if activity_var == "Study":
        activity_var = study_var
    else:
        activity_var = break_var


def show_study_combobox():
    study_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    break_frame.grid_forget()


def show_break_combobox():
    break_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
    study_frame.grid_forget()


def open_map_win():
    global root
    root.withdraw()
    map_win = tk.Toplevel(root)
    map_win.title("Map")
    map_win.resizable(0, 0)

    path = r'C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\pages for the tkinker backgrounds\map.jpg'

    python_image = Image.open(path)
    resized_image = python_image.resize((400, 500), Image.LANCZOS)
    tkinter_image = ImageTk.PhotoImage(resized_image)

    label = tk.Label(map_win, image=tkinter_image)
    label.image = tkinter_image
    label.grid()

    title_label = tk.Label(map_win, text="Find my Buddy - on the map", font=(
        "Aleo", 14), bg="#740031", fg="white")
    title_label.place(x=10, y=10, anchor=tk.NW)

    return_button = tk.Button(
        map_win, text="Return", bg="#740031", fg="white", command=lambda: map_win.destroy())
    return_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


def login():
    global root, name, email, name_entry, email_entry
    root = tk.Tk()
    root.title("Login")
    root.geometry("390x540")
    root.configure(bg="#7d212a")
    root.resizable(0, 0)

    title_label = tk.Label(
        root, text="Leuphinder Login", fg="white", font=("Aleo", 32), bg="#7d212a")
    title_label.grid(row=1, column=0, columnspan=3, sticky="ew", padx=25)

    name_label = tk.Label(root, text="Name",
                          fg="white", bg="#7d212a", font="Aleo")
    name_label.grid(row=5, column=0, padx=20, pady=10, sticky="nw")

    name_entry = tk.Entry(
        root, fg="black", bg="white", font="Aleo")
    name_entry.grid(row=5, column=1, columnspan=2,
                    padx=(5, 20), pady=10, sticky="nw")

    email_label = tk.Label(root, text="E-mail",
                           fg="white", bg="#7d212a", font="Aleo")
    email_label.grid(row=7, column=0, padx=20, pady=10, sticky="nw")

    email_entry = tk.Entry(
        root, fg="black", bg="white", font="Aleo")
    email_entry.grid(row=7, column=1, columnspan=2,
                     padx=(5, 20), pady=10, sticky="nw")

    password_label = tk.Label(
        root, text="Password", fg="white", bg="#7d212a", font="Aleo")
    password_label.grid(row=9, column=0, padx=20, pady=10, sticky="nw")

    password_entry = tk.Entry(
        root, fg="black", bg="white", font="Aleo")
    password_entry.grid(
        row=9, column=1, columnspan=2, padx=(5, 20), pady=10, sticky="nw")

    cancel_button = tk.Button(
        root, text="Cancel", fg="white", bg="#740031", command=destroy_win)
    cancel_button.grid(row=11, column=0, columnspan=3,
                       pady=10, padx=5, sticky="nsew")

    start_button = tk.Button(
        root, text="Start", fg="white", bg="#740031", command=open_main_page)
    start_button.grid(row=10, column=0, columnspan=3,
                      pady=10, padx=5, sticky="nsew")

    # Load and display the logo
    logo_image = Image.open(r"C:\Users\lotti\Documents\Leuphana assignments 2023\Tech Basics 2\logo.jpg")
    logo_image = logo_image.resize((90, 90), Image.LANCZOS)
    tk_logo_image = ImageTk.PhotoImage(logo_image)

    # Create a separate label to hold the logo
    logo_label = tk.Label(
        root, image=tk_logo_image, bg="#7d212a")
    logo_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Make the logo clickableW
    logo_label.bind("<Button-1>", lambda event: open_about_window())

    name = name_entry.get()
    email = email_entry.get()

    root.mainloop()


login()
