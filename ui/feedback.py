import tkinter as tk
from tkinter import Frame, Label, Entry, Text, Button
from tkinter import ttk

# Initialize main window
root = tk.Tk()
root.title("Hotel Booking - Feedback Screen")
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

Label(content_frame, text="Give Your Feedback", font=("Arial", 14, "bold"), bg="white").place(x=400, y=30)

# ---------------- Feedback Form ---------------- #
feedback_frame = Frame(content_frame, bg="white", width=900, height=300, highlightbackground="#D5D8DC", highlightthickness=1)
feedback_frame.place(x=30, y=70)

Label(feedback_frame, text="💬 We Value Your Feedback", font=("Arial", 12, "bold"), bg="white").place(x=20, y=10)

# Full Name Entry
Label(feedback_frame, text="👤 Full Name", font=("Arial", 10), bg="white").place(x=20, y=50)
Entry(feedback_frame, width=60).place(x=20, y=70)

# Rating Stars
Label(feedback_frame, text="⭐ Rate Your Experience", font=("Arial", 10), bg="white").place(x=20, y=110)
stars = ["⭐", "⭐", "⭐", "⭐", "⭐"]
for i, star in enumerate(stars):
    Button(feedback_frame, text=star, font=("Arial", 12), relief="flat", bg="white").place(x=180 + (i * 40), y=105)

# Feedback Text Box
Label(feedback_frame, text="💭 Your Feedback", font=("Arial", 10), bg="white").place(x=20, y=150)
Text(feedback_frame, width=80, height=4).place(x=20, y=170)

# Submit Button
Button(feedback_frame, text="Submit Feedback", font=("Arial", 12, "bold"), bg="#001F3F", fg="white", width=40, height=2).place(x=200, y=250)

root.mainloop()
