import tkinter as tk
from tkinter import Frame, Label, Button, Entry, ttk

# Initialize main window
root = tk.Tk()
root.title("Hotel Booking - Customer Profile")
root.geometry("1200x600")
root.configure(bg="#EDEDED")  # Light Grey Background

# ---------------- Sidebar (Navigation) ---------------- #
sidebar = Frame(root, bg="#2C3E50", width=220, height=600)
sidebar.place(x=0, y=0)

Label(sidebar, text="🏨 Hotel Booking", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50").place(x=20, y=20)

# Sidebar Buttons
nav_buttons = [
    ("🏠 Home", 70),
    ("📅 Bookings", 120),
    ("👤 Profile", 170),
    ("💬 Feedback", 220),
    ("🔑 Logout", 500)
]
for text, y in nav_buttons:
    Button(sidebar, text=text, font=("Arial", 10), fg="white", bg="#34495E", relief="flat", width=18, height=1).place(x=20, y=y)

# ---------------- Main Content ---------------- #
content_frame = Frame(root, bg="white", width=980, height=600)
content_frame.place(x=220, y=0)

Label(content_frame, text="User Management", font=("Arial", 14, "bold"), bg="white").place(x=400, y=30)

# ---------------- Edit Profile Section ---------------- #
profile_frame = Frame(content_frame, bg="white", width=900, height=150, highlightbackground="#D5D8DC", highlightthickness=1)
profile_frame.place(x=30, y=70)

Label(profile_frame, text="✏ Edit Profile", font=("Arial", 12, "bold"), bg="white").place(x=20, y=10)

# Labels and Entry Fields
Label(profile_frame, text="Full Name", font=("Arial", 10), bg="white").place(x=20, y=40)
Entry(profile_frame, width=30).place(x=20, y=60)

Label(profile_frame, text="Phone Number", font=("Arial", 10), bg="white").place(x=20, y=90)
Entry(profile_frame, width=30).place(x=20, y=110)

Label(profile_frame, text="Email Address", font=("Arial", 10), bg="white").place(x=320, y=40)
Entry(profile_frame, width=30).place(x=320, y=60)

Label(profile_frame, text="Address", font=("Arial", 10), bg="white").place(x=320, y=90)
Entry(profile_frame, width=30).place(x=320, y=110)

Button(profile_frame, text="Update Profile", font=("Arial", 10, "bold"), bg="#007BFF", fg="white", width=15).place(x=650, y=100)

# ---------------- Booking History Section ---------------- #
history_frame = Frame(content_frame, bg="white", width=900, height=180, highlightbackground="#D5D8DC", highlightthickness=1)
history_frame.place(x=30, y=250)

Label(history_frame, text="🔄 Booking History", font=("Arial", 12, "bold"), bg="white").place(x=20, y=10)

# Table (Treeview)
columns = ("Booking ID", "Hotel", "Check-in", "Check-out", "Amount", "Status")

tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=5)
tree.place(x=20, y=40)

# Column Headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=140)

# Sample Data
bookings = [
    ("#12345", "Luxury Grand Hotel", "2025-06-15", "2025-06-20", "$750", "Confirmed"),
    ("#12346", "Mountain Retreat", "2025-07-01", "2025-07-05", "$600", "Cancelled"),
]

# Insert Data
for booking in bookings:
    tree.insert("", "end", values=booking)

root.mainloop()
