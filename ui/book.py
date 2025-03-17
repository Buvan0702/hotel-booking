import tkinter as tk
from tkinter import Frame, Label, Button, Entry, ttk, StringVar, Radiobutton

# Initialize main window
root = tk.Tk()
root.title("Hotel Booking")
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

# ---------------- Main Booking Section ---------------- #
booking_frame = Frame(root, bg="white", width=980, height=600)
booking_frame.place(x=220, y=0)

Label(booking_frame, text="Luxury Grand Hotel", font=("Arial", 14, "bold"), bg="white").place(x=50, y=30)
Label(booking_frame, text="📍 123 Main Street, Mt. Pleasant, Michigan", font=("Arial", 10), bg="white").place(x=50, y=60)

# Booking Form
form_frame = Frame(booking_frame, bg="white", width=600, height=300, highlightbackground="#D5D8DC", highlightthickness=1)
form_frame.place(x=50, y=100)

Label(form_frame, text="📅 Select Your Stay", font=("Arial", 11, "bold"), bg="white").place(x=20, y=20)

Label(form_frame, text="Check-in Date", bg="white").place(x=20, y=60)
Label(form_frame, text="Check-out Date", bg="white").place(x=310, y=60)
Entry(form_frame, width=25).place(x=20, y=80)
Entry(form_frame, width=25).place(x=310, y=80)

Label(form_frame, text="Guests", bg="white").place(x=20, y=110)
Label(form_frame, text="Room Type", bg="white").place(x=310, y=110)
Entry(form_frame, width=25).place(x=20, y=130)
room_type = ttk.Combobox(form_frame, values=["Single Room - $150/night", "Double Room - $200/night"], width=23)
room_type.place(x=310, y=130)
room_type.current(0)

# Payment Method
Label(form_frame, text="💳 Payment Method", font=("Arial", 11, "bold"), bg="white").place(x=20, y=170)
payment_method = StringVar()
Radiobutton(form_frame, text="Credit/Debit Card", variable=payment_method, value="Card", bg="white").place(x=20, y=200)
Radiobutton(form_frame, text="PayPal", variable=payment_method, value="PayPal", bg="white").place(x=150, y=200)

# Confirm Booking Button
Button(form_frame, text="Confirm Booking", font=("Arial", 10, "bold"), bg="#FFC107", fg="black", width=50, height=1).place(x=20, y=240)

# ---------------- Booking Summary ---------------- #
summary_frame = Frame(booking_frame, bg="white", width=300, height=250, highlightbackground="#D5D8DC", highlightthickness=1)
summary_frame.place(x=700, y=100)

Label(summary_frame, text="📝 Booking Summary", font=("Arial", 11, "bold"), bg="white").place(x=20, y=20)
Label(summary_frame, text="Hotel: Luxury Grand Hotel", bg="white").place(x=20, y=50)
Label(summary_frame, text="Location: New York, USA", bg="white").place(x=20, y=70)
Label(summary_frame, text="Room Type: Single Room", bg="white").place(x=20, y=90)
Label(summary_frame, text="Price per Night: $150", bg="white").place(x=20, y=110)
Label(summary_frame, text="Total Nights: 2", bg="white").place(x=20, y=130)

Label(summary_frame, text="Total Price: $300", font=("Arial", 12, "bold"), fg="black", bg="white").place(x=20, y=180)

root.mainloop()
