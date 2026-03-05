import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from pymongo import MongoClient
import hashlib

client = MongoClient("mongodb://localhost:27017/")
db = client["student_db"]

students_collection = db["students"]
users_collection = db["users"]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

root = tk.Tk()
root.title("Student Manager MongoDB")
root.geometry("650x450")
root.withdraw()

login_window = tk.Toplevel()
login_window.title("Login System")
login_window.geometry("350x250")
login_window.resizable(False, False)

def register():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Warning", "All fields required")
        return

    if users_collection.find_one({"username": username}):
        messagebox.showerror("Error", "User already exists")
        return

    users_collection.insert_one({
        "username": username,
        "password": hash_password(password)
    })

    messagebox.showinfo("Success", "User Registered")

def login():
    username = username_entry.get()
    password = password_entry.get()

    user = users_collection.find_one({"username": username})

    if user and user["password"] == hash_password(password):
        messagebox.showinfo("Success", "Login Successful")
        login_window.destroy()
        root.deiconify()
    else:
        messagebox.showerror("Error", "Invalid Credentials")

tk.Label(login_window, text="Username").pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", width=15, command=login).pack(pady=5)
tk.Button(login_window, text="Register", width=15, command=register).pack(pady=5)

def refresh_table():
    table.delete(*table.get_children())
    for s in students_collection.find():
        table.insert("", "end", values=(s["id"], s["name"], s["branch"]))

def add_student():
    id_ = simpledialog.askstring("Add Student", "Enter ID:")
    name = simpledialog.askstring("Add Student", "Enter Name:")
    branch = simpledialog.askstring("Add Student", "Enter Branch:")

    if not id_ or not name or not branch:
        messagebox.showwarning("Warning", "All fields required")
        return

    if students_collection.find_one({"id": id_}):
        messagebox.showerror("Error", "ID exists")
        return

    students_collection.insert_one({
        "id": id_,
        "name": name,
        "branch": branch
    })

    messagebox.showinfo("Success", "Student Added")
    refresh_table()

def search_student():
    id_ = simpledialog.askstring("Search", "Enter ID:")
    student = students_collection.find_one({"id": id_})

    if student:
        messagebox.showinfo(
            "Found",
            f"ID: {student['id']}\nName: {student['name']}\nBranch: {student['branch']}"
        )
    else:
        messagebox.showinfo("Not Found", "Student not found")

def delete_student():
    id_ = simpledialog.askstring("Delete", "Enter ID:")
    result = students_collection.delete_one({"id": id_})

    if result.deleted_count:
        messagebox.showinfo("Deleted", "Student deleted")
    else:
        messagebox.showinfo("Not Found", "Student not found")

    refresh_table()

def update_student():
    id_ = simpledialog.askstring("Update", "Enter ID:")
    student = students_collection.find_one({"id": id_})

    if not student:
        messagebox.showinfo("Not Found", "Student not found")
        return

    name = simpledialog.askstring("Update", "Enter new name:", initialvalue=student["name"])
    branch = simpledialog.askstring("Update", "Enter new branch:", initialvalue=student["branch"])

    students_collection.update_one(
        {"id": id_},
        {"$set": {"name": name, "branch": branch}}
    )

    messagebox.showinfo("Updated", "Student updated")
    refresh_table()

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