import json
import os
file="students.json"
if not os.path.exists(file):
    with open(file,"w") as f:
        json.dump([],f)
def load():
    with open(file,"r") as f:
        return json.load(f)
def save(data):
    with open(file,"w") as f:
        json.dump(data,f,indent=4)
def add():
    data=load()
    id=input("Enter ID : ")
    name=input("Enter Name : ")
    branch=input("Enter Branch : ")

    data.append({"id":id,"name":name,"branch":branch})
    save(data)
    print("Student added")
def view():
    data=load()
    for s in data:
        print(s)
def search():
    id=input("Enter ID : ")
    data=load()
    for s in data:
        if s["id"]==id:
            print(s)
            return
    print("Student Not Found")
def delete():
    id=input("Enter ID : ")
    data=load()
    data=[s for s in data if s["id"]!=id]
    save(data)
    print("Student Record Deleted")
def update():
    id=input("Enter ID : ")
    data=load()
    for s in data:
        if s["id"]==id:
            s["name"]=input("New Name : ")
            s["branch"]=input("New Branch : ")
            save(data)
            print("Student Record Updated")
            return
    print("Student Not Found")
while True:
    print("\n1 ADD \n2 View \n3 Search \n4 Delete \n5 Update \n6 Exit")
    ch=input("Enter choice : ")
    if ch=="1":
        add()
    elif ch=="2":
        view()
    elif ch=="3":
        search()
    elif ch=="4":
        delete()
    elif ch=="5":
        update()
    elif ch=="6":
        break