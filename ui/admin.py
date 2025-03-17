import tkinter as tk
from tkinter import Frame, Label, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize main window
root = tk.Tk()
root.title("Admin Dashboard - Hotel Booking")
root.geometry("1200x600")
root.configure(bg="#EDEDED")  # Light Grey Background

# ---------------- Sidebar (Navigation) ---------------- #
sidebar = Frame(root, bg="#2C3E50", width=220, height=600)
sidebar.place(x=0, y=0)

Label(sidebar, text="🏨 Hotel Booking", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50").place(x=20, y=20)

# Sidebar Buttons
nav_buttons = [
    ("📊 Dashboard", 60),
    ("📅 Manage Bookings", 110),
    ("👤 Manage Users", 160),
    ("🔑 Logout", 500)
]
for text, y in nav_buttons:
    Button(sidebar, text=text, font=("Arial", 10), fg="white", bg="#34495E", relief="flat", width=18, height=1).place(x=20, y=y)

# ---------------- Main Dashboard ---------------- #
dashboard_frame = Frame(root, bg="white", width=980, height=600)
dashboard_frame.place(x=220, y=0)

Label(dashboard_frame, text="Admin Dashboard", font=("Arial", 14, "bold"), bg="white").place(x=400, y=20)

# Stats Cards
stats = [
    ("Total Bookings", "1,250", 50),
    ("Total Revenue", "$325,000", 280),
    ("Active Users", "2,500", 510),
    ("Hotels Listed", "85", 740)
]
for text, value, x in stats:
    card = Frame(dashboard_frame, bg="white", width=220, height=80, highlightbackground="#D5D8DC", highlightthickness=1)
    card.place(x=x, y=60)
    Label(card, text=text, font=("Arial", 10, "bold"), bg="white").place(x=10, y=10)
    Label(card, text=value, font=("Arial", 12), bg="white").place(x=10, y=40)

# ---------------- Graph (Revenue & Bookings Overview) ---------------- #
Label(dashboard_frame, text="Revenue & Bookings Overview", font=("Arial", 12, "bold"), bg="white").place(x=50, y=160)

# Sample Matplotlib Graph
fig, ax = plt.subplots(figsize=(5, 2))
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [40000, 45000, 50000, 55000, 65000, 75000]
bookings = [100, 150, 200, 250, 300, 350]

ax.plot(months, revenue, label="Revenue ($)", color="blue")
ax.plot(months, bookings, label="Bookings", color="green")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=dashboard_frame)
canvas.get_tk_widget().place(x=50, y=200)

root.mainloop()
