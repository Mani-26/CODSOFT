import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql


def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo("Error", "Field is Empty.")
    else:
        tasks.append(task_string)
        the_cursor.execute("insert into tasks values (?)", (task_string,))
        list_update()
        task_field.delete(0, "end")


def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert("end", task)


def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute("delete from tasks where title = ?", (the_value,))
    except:
        messagebox.showinfo("Error", "No Task Selected. Cannot Delete.")


def delete_all_tasks():
    message_box = messagebox.askyesno(
        "Delete All", "This will Delete all Tasks Are you sure?"
    )
    if message_box == True:
        while len(tasks) != 0:
            tasks.pop()
        the_cursor.execute("delete from tasks")
        list_update()


def clear_list():
    task_listbox.delete(0, "end")


def close():
    print(tasks)
    guiWindow.destroy()


def retrieve_database():
    while len(tasks) != 0:
        tasks.pop()
    for row in the_cursor.execute("select title from tasks"):
        tasks.append(row[0])


if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("Mani's To-Do List")
    guiWindow.geometry("300x600+550+50")

    the_connection = sql.connect("listOfTasks.db")
    the_cursor = the_connection.cursor()
    the_cursor.execute("create table if not exists tasks (title text)")

    tasks = []

    header_frame = tk.Frame(guiWindow, bg="grey")
    functions_frame = tk.Frame(guiWindow, bg="cyan")
    listbox_frame = tk.Frame(guiWindow, bg="lime")

    header_frame.pack(fill="both")
    functions_frame.pack(side="bottom", expand=True, fill="both")
    listbox_frame.pack(side="top", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="Task to be completed",
        font=("Brush Script MT", "30"),
    )
    header_label.pack(padx=10, pady=10)

    task_label = ttk.Label(
        functions_frame,
        text="Enter your Task:",
        font=("Times New Roman", "12", "bold"),
        background="#000000",
        foreground="white",
    )
    task_label.place(x=85, y=20)

    task_field = ttk.Entry(
        functions_frame,
        font=("Times New Roman", "14"),
        width=24,
        background="white",
        foreground="#000000",
    )
    task_field.place(x=36, y=55)

    add_button = ttk.Button(
        functions_frame, text="Add Task", width=24, command=add_task
    )
    del_button = ttk.Button(
        functions_frame, text="Delete Task", width=24, command=delete_task
    )
    del_all_button = ttk.Button(
        functions_frame, text="Delete All Tasks", width=24, command=delete_all_tasks
    )
    exit_button = ttk.Button(functions_frame, text="Exit", width=24, command=close)
    add_button.place(x=70, y=90)
    del_button.place(x=70, y=120)
    del_all_button.place(x=70, y=150)
    exit_button.place(x=70, y=180)

    task_listbox = tk.Listbox(
        listbox_frame, font=("Times New Roman", "14"), width=28, height=10
    )
    task_listbox.place(x=20, y=15)

    retrieve_database()
    list_update()
    guiWindow.mainloop()
    the_connection.commit()
    the_cursor.close()
