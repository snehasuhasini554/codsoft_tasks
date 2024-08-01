import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")

listbox = tk.Listbox(root)
listbox.pack()

entry = tk.Entry(root)
entry.pack(pady=10)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def remove_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "You must select a task.")

add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)

add_button.pack()
remove_button.pack()

root.mainloop()