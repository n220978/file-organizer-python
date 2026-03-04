📘 Student Management System with Authentication
📌 Project Overview

This project is a Student Management System built using:

Python

Tkinter (GUI)

MongoDB (Database)

SHA-256 Password Hashing (Security)

It allows users to:

Register and Login securely

Add, View, Update, Delete student records

Store data permanently in MongoDB

🎯 Features
🔐 Authentication System

User Registration

Secure Login

Passwords stored using SHA-256 hashing

Only authenticated users can access the system

👨‍🎓 Student Management (CRUD)

Add Student

View All Students

Search Student by ID

Update Student Details

Delete Student Record

🗄 Database Integration

MongoDB used for persistent data storage

Two collections:

users

students

🛠 Technologies Used

Python 3

Tkinter

PyMongo

MongoDB

hashlib (for password hashing)

🏗 Project Structure
student_manager_with_login.py
README.md
🧠 System Architecture
1️⃣ Presentation Layer

Tkinter GUI
Handles user interaction.

2️⃣ Business Logic Layer

Python functions for:

Authentication

Data validation

CRUD operations

3️⃣ Data Layer

MongoDB database:

student_db

users

students

🚀 How to Run the Project
Step 1: Install Dependencies
pip install pymongo
Step 2: Start MongoDB

Make sure MongoDB server is running:

mongod
Step 3: Run the Application
python student_manager_with_login.py
🔒 Security Implementation

Passwords are not stored in plain text.

They are hashed using:

SHA-256

Example:

Input Password → "admin123"
Stored Value → e99a18c428cb38d5f260853678922e03...

This ensures secure authentication.

📈 Learning Outcomes

Through this project, the following concepts were implemented:

GUI Programming

MongoDB Integration

CRUD Operations

Authentication System

Password Hashing

Database-driven Applications

🌍 Real-World Relevance

This project simulates real systems such as:

College ERP Systems

Admin Dashboards

HR Management Systems

Library Management Software

👩‍💻 Author

Sahithi Pallikonda