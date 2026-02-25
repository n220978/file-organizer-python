import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]
collection = db["students"]

def refresh_table():

    table.delete(*table.get_children())

    data = collection.find()

    for s in data:

        table.insert("", "end", values=(s["id"], s["name"], s["branch"]))


def add_student():

    id_ = simpledialog.askstring("Add Student", "Enter ID:")
    name = simpledialog.askstring("Add Student", "Enter Name:")
    branch = simpledialog.askstring("Add Student", "Enter Branch:")

    if not id_ or not name or not branch:
        messagebox.showwarning("Warning", "All fields required")
        return

    if collection.find_one({"id": id_}):

        messagebox.showerror("Error", "ID exists")
        return

    collection.insert_one({

        "id": id_,
        "name": name,
        "branch": branch

    })

    messagebox.showinfo("Success", "Student Added")

    refresh_table()



def search_student():

    id_ = simpledialog.askstring("Search", "Enter ID:")

    student = collection.find_one({"id": id_})

    if student:

        messagebox.showinfo("Found",

        f"ID: {student['id']}\nName: {student['name']}\nBranch: {student['branch']}")

    else:

        messagebox.showinfo("Not Found", "Student not found")



def delete_student():

    id_ = simpledialog.askstring("Delete", "Enter ID:")

    result = collection.delete_one({"id": id_})

    if result.deleted_count:

        messagebox.showinfo("Deleted", "Student deleted")

    else:

        messagebox.showinfo("Not Found", "Student not found")

    refresh_table()


def update_student():

    id_ = simpledialog.askstring("Update", "Enter ID:")

    student = collection.find_one({"id": id_})

    if not student:

        messagebox.showinfo("Not Found", "Student not found")
        return

    name = simpledialog.askstring("Update", "Enter new name:", initialvalue=student["name"])

    branch = simpledialog.askstring("Update", "Enter new branch:", initialvalue=student["branch"])

    collection.update_one(

        {"id": id_},

        {"$set": {"name": name, "branch": branch}}

    )

    messagebox.showinfo("Updated", "Student updated")

    refresh_table()



root = tk.Tk()

root.title("Student Manager MongoDB")

root.geometry("650x450")


frame = tk.Frame(root)

frame.pack(pady=20)


tk.Button(frame, text="Add", width=12, command=add_student).grid(row=0, column=0)

tk.Button(frame, text="View", width=12, command=refresh_table).grid(row=0, column=1)

tk.Button(frame, text="Search", width=12, command=search_student).grid(row=0, column=2)

tk.Button(frame, text="Update", width=12, command=update_student).grid(row=0, column=3)

tk.Button(frame, text="Delete", width=12, command=delete_student).grid(row=0, column=4)


table = ttk.Treeview(root, columns=("ID", "Name", "Branch"), show="headings")

table.heading("ID", text="ID")

table.heading("Name", text="Name")

table.heading("Branch", text="Branch")

table.pack(fill="x")


refresh_table()

root.mainloop()