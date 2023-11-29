import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_list.delete(tk.ACTIVE)
    except:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Initialize the main window and set its properties.
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")  # Set initial window size
root.configure(bg="#D3E0EA")  # Set background color

# Add a heading "To-Do List" at the top of the screen
heading_label = tk.Label(root, text="To-Do List", font=("Segoe Script", 24, "bold"), bg="#5E7F9B", fg="white", pady=10)
heading_label.pack(fill=tk.X)

# Entry, buttons, and listbox widgets
entry = tk.Entry(root, width=30, font=("Helvetica", 14))
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#5E7F9B", fg="white", font=("Segoe Script", 12, "bold"))
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#5E7F9B", fg="white", font=("Segoe Script", 12, "bold"))
task_list = tk.Listbox(root, selectmode=tk.SINGLE, borderwidth=5, font=("Helvetica", 12), bg="#D3E0EA", selectbackground="#5E7F9B")

# Grid layout for widgets
entry.pack(pady=10)
add_button.pack(pady=5)
remove_button.pack(pady=5)
task_list.pack(expand=True, fill=tk.BOTH)

# Configure column and row weights for resizing
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

# Start the Tkinter event loop
root.mainloop()
