import tkinter as tk
from tkinter import ttk


def destroy_win():
    win.destroy()


def open_match_window():
    win.destroy()
    match_win = tk.Tk()
    match_win.title("win.match")


def activity_selected():
    selected_activity = activity_var.get()

    if selected_activity == "Study":
        study_frame.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        break_frame.grid_forget()
    elif selected_activity == "Break":
        break_frame.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        study_frame.grid_forget()


win = tk.Tk()
win.title('Search for a Study Buddy')
win.geometry('350x300')
win.configure(bg="#7f3536")
win.resizable(0, 0)

# Label for Title:
label1 = tk.Label(win, text="Find a Study Buddy - Schedule for", bg='#740031', fg='white', font=("Aleo", 15))
label1.grid(row=0, column=0, columnspan=2, sticky="w")

# Label for ACTIVITY:
label_activity = tk.Label(win, text="ACTIVITY", bg='#7f3536', fg= "white", font=("Aleo", 12, "bold"))
label_activity.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Activity radio button:
activity_var = tk.StringVar()
activity_radio1 = ttk.Radiobutton(
    win, text="Study", variable=activity_var, value="Study", command=activity_selected)
activity_radio1.grid(row=2, column=0, padx=20, pady=2, sticky="w")

activity_radio2 = ttk.Radiobutton(
    win, text="Break", variable=activity_var, value="Break", command=activity_selected)
activity_radio2.grid(row=3, column=0, padx=20, pady=2, sticky="w")

# Frames for Study and Break options:
study_frame = tk.Frame( bg="#7f3536")
break_frame = tk.Frame( bg="#7f3536")

# Study combobox:
study_var = tk.StringVar()
study_combobox = ttk.Combobox(study_frame, textvariable=study_var)
study_combobox['values'] = ("for a project", "for an exam", "in the library")
study_combobox.current(0)
study_combobox.grid(row=0, column=0, padx=10, pady=5)

# Break combobox:
break_var = tk.StringVar()
break_combobox = ttk.Combobox(break_frame, textvariable=break_var)
break_combobox['values'] = ("go for lunch", "go outside e.g. for a walk", "in the city")
break_combobox.current(0)
break_combobox.grid(row=0, column=0, padx=10, pady=5)

# Label for TIME:
label_time = tk.Label(win, text="TIME", bg='#7f3536', fg="white" ,font=("Aleo", 12, "bold"))
label_time.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Combobox for time selection:
time_var = tk.StringVar()
time_combobox = ttk.Combobox(win, textvariable=time_var)
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

# Search button:
find_buddy_button = tk.Button(win, text="Search", bg="#740031", fg="white", font=("Aleo", 12), command=open_match_window)
find_buddy_button.grid(row=10, column=0, columnspan=2, pady=(85, 0), padx=5, sticky="ew")

win.mainloop()
