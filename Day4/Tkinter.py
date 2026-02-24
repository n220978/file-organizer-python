# import tkinter as tk
# from tkinter import messagebox,simpledialog,ttk
# import json
# import os
# file="students.json"
# if not os.path.exists(file):
#     with open(file,"w") as f:
#         json.dump([],f)
# def load_data():
#     with open(file,"r") as f:
#         return json.load(f)
# def save_data(data):
#     with open(file,"w") as f:
#         json.dump(data,f,indent=4)
# def add_student():
#     id_=simpledialog.askstring("Add Student","Enter ID : ")
#     name=simpledialog.askstring("Add Student","Enter Name : ")
#     branch=simpledialog.askstring("Add Student","Enter Branch : ")
#     if id_ and name and branch:
#         data =load_data()
#         for s in data:
#             if s["id"]==id_:
#                 messagebox.showerror("Error","ID already exists!")
#                 return
#         data.append({"id":id_,"name":name,"branch":branch})
#         save_data(data)
#         messagebox.showinfo("Success","Student Added Successfully")
#     else:
#         messagebox.showerror("Warning","All fields required")
# def view_students():
#     refresh_table()
# def search_student():
#     id_=simpledialog.askstring("Search Student","Enter ID:")
#     data=load_data()
#     new_data=[s for s in data if s["id"]==id_]
#     if len(new_data)==len(data):
#         messagebox.showinfo("Not Found","Student not found")
#     else:
#         save_data(new_data)
#         messagebox.showinfo("Deleted","Student Deleted")
#         refresh_table()
# def delete_student():
#     id_ = simpledialog.askstring("Delete Student", "Enter ID:")
#     data = load_data()
#     new_data = [s for s in data if s["id"] != id_]
#     if len(new_data) == len(data):
#         messagebox.showinfo("Not Found", "Student not found")
#     else:
#         save_data(new_data)
#         messagebox.showinfo("Deleted", "Student deleted")
#         refresh_table()
# def update_student():
#     id_=simpledialog.askstring("Update Student","Enter ID : ")
#     data=load_data()
#     for s in data:
#         if s["id"]==id_:
#             name=simpledialog.askstring("Update Student","Enter New Name : ",initialvalue=s["name"])
#             branch=simpledialog.askstring("Update Student","Enter New Branch : ",initialvalue=s["branch"])
#             s["name"]=name
#             s["branch"]=branch
#             save_data(data)
#             messagebox.showinfo("Updatted","Student Updated")
#             refresh_table()
#             return
#     messagebox.showinfo("Not Found","Student not found")
# def refresh_table():
#     for row in table.get_children():
#         table.delete(row)
#     data=load_data()
#     for s in data:
#         table.insert("","end",values=(s["id"],s["name"],s["branch"]))
# root=tk.Tk()
# root.title("Student Manager GUI")
# root.geometry("600x400")

# frame=tk.Frame(root)
# frame.pack(pady=20)

# btn_add=tk.Button(frame,text="Add",width=12,command=add_student)
# btn_add.grid(row=0,column=0,padx=5)
# btn_view=tk.Button(frame,text="View",width=12,command=view_students)
# btn_view.grid(row=0,column=1,padx=5)
# btn_search=tk.Button(frame,text="Search",width=12,command=search_student)
# btn_search.grid(row=0,column=2,padx=5)
# btn_update=tk.Button(frame,text="Update",width=12,command=update_student)
# btn_update.grid(row=0,column=3,padx=5)
# btn_delete=tk.Button(frame,text="Delete",width=12,command=delete_student)
# btn_delete.grid(row=0,column=4,padx=5)

# table=ttk.Treeview(root,columns=("ID","Name","Branch"),show="headings")
# table.heading("ID",text="ID")
# table.heading("Name",text="Name")
# table.heading("Branch",text="Branch")

# refresh_table()
# root.mainloop()



import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
import os

file = "students.json"

# Ensure JSON file exists
if not os.path.exists(file):
    with open(file, "w") as f:
        json.dump([], f)

# Load & Save functions
def load_data():
    with open(file, "r") as f:
        return json.load(f)

def save_data(data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Refresh table
def refresh_table():
    table.delete(*table.get_children())  # Clear table
    data = load_data()
    if not data:
        messagebox.showinfo("Info", "No students to display")
        return
    for s in data:
        table.insert("", "end", values=(s["id"], s["name"], s["branch"]))

# Functions for operations
def add_student():
    id_ = simpledialog.askstring("Add Student", "Enter ID:")
    name = simpledialog.askstring("Add Student", "Enter Name:")
    branch = simpledialog.askstring("Add Student", "Enter Branch:")
    
    if id_ and name and branch:
        data = load_data()
        # Check duplicate ID
        for s in data:
            if s["id"] == id_:
                messagebox.showerror("Error", "ID already exists")
                return
        data.append({"id": id_, "name": name, "branch": branch})
        save_data(data)
        messagebox.showinfo("Success", "Student Added")
        refresh_table()
    else:
        messagebox.showwarning("Warning", "All fields required")

def search_student():
    id_ = simpledialog.askstring("Search Student", "Enter ID:")
    data = load_data()
    for s in data:
        if s["id"] == id_:
            messagebox.showinfo("Found", f"ID: {s['id']}\nName: {s['name']}\nBranch: {s['branch']}")
            return
    messagebox.showinfo("Not Found", "Student not found")

def delete_student():
    id_ = simpledialog.askstring("Delete Student", "Enter ID:")
    data = load_data()
    new_data = [s for s in data if s["id"] != id_]
    if len(new_data) == len(data):
        messagebox.showinfo("Not Found", "Student not found")
    else:
        save_data(new_data)
        messagebox.showinfo("Deleted", "Student deleted")
        refresh_table()

def update_student():
    id_ = simpledialog.askstring("Update Student", "Enter ID:")
    data = load_data()
    for s in data:
        if s["id"] == id_:
            name = simpledialog.askstring("Update Student", "Enter New Name:", initialvalue=s["name"])
            branch = simpledialog.askstring("Update Student", "Enter New Branch:", initialvalue=s["branch"])
            s["name"] = name
            s["branch"] = branch
            save_data(data)
            messagebox.showinfo("Updated", "Student updated")
            refresh_table()
            return
    messagebox.showinfo("Not Found", "Student not found")

# GUI Setup
root = tk.Tk()
root.title("Student Manager GUI")
root.geometry("650x450")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=20)

# Buttons
btn_add = tk.Button(frame, text="Add", width=12, command=add_student)
btn_add.grid(row=0, column=0, padx=5)

btn_view = tk.Button(frame, text="View", width=12, command=refresh_table)
btn_view.grid(row=0, column=1, padx=5)

btn_search = tk.Button(frame, text="Search", width=12, command=search_student)
btn_search.grid(row=0, column=2, padx=5)

btn_update = tk.Button(frame, text="Update", width=12, command=update_student)
btn_update.grid(row=0, column=3, padx=5)

btn_delete = tk.Button(frame, text="Delete", width=12, command=delete_student)
btn_delete.grid(row=0, column=4, padx=5)

# Table to show students
table = ttk.Treeview(root, columns=("ID", "Name", "Branch"), show="headings")
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Branch", text="Branch")
table.column("ID", width=100)
table.column("Name", width=200)
table.column("Branch", width=150)
table.pack(pady=20, fill="x")

# Initially load data
refresh_table()

root.mainloop()