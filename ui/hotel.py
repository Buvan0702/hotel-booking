import tkinter as tk
from tkinter import Frame, Label, Button, Entry, ttk

# Initialize main window
root = tk.Tk()
root.title("Hotel Booking - Customer Home")
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

Label(content_frame, text="Find Your Perfect Stay", font=("Arial", 14, "bold"), bg="white").place(x=350, y=30)

# ---------------- Search Section ---------------- #
search_frame = Frame(content_frame, bg="white", width=800, height=100, highlightbackground="#D5D8DC", highlightthickness=1)
search_frame.place(x=100, y=70)

Label(search_frame, text="📍 Location", font=("Arial", 10, "bold"), bg="white").place(x=20, y=10)
Entry(search_frame, width=20).place(x=20, y=30)

Label(search_frame, text="📅 Check-in Date", font=("Arial", 10, "bold"), bg="white").place(x=220, y=10)
Entry(search_frame, width=15).place(x=220, y=30)

Label(search_frame, text="📅 Check-out Date", font=("Arial", 10, "bold"), bg="white").place(x=400, y=10)
Entry(search_frame, width=15).place(x=400, y=30)

Label(search_frame, text="👤 Guests", font=("Arial", 10, "bold"), bg="white").place(x=580, y=10)
Entry(search_frame, width=10).place(x=580, y=30)

Button(search_frame, text="Search Rooms", font=("Arial", 10, "bold"), bg="#FFC107", fg="black", width=80, height=1).place(x=20, y=60)

# ---------------- Popular Hotels Section ---------------- #
Label(content_frame, text="Popular Hotels", font=("Arial", 12, "bold"), bg="white").place(x=100, y=180)

hotels = [
    ("Luxury Grand Hotel", "A 5-star hotel with exclusive services and amenities.", "📶 Free WiFi | 🏊 Pool | 🚗 Free Parking", "$250 per night"),
    ("Ocean View Resort", "Enjoy stunning ocean views with top-notch hospitality.", "🍽 Restaurant | 🧖 Spa | 🍳 Breakfast", "$300 per night"),
    ("Mountain Retreat Lodge", "Escape to nature with this peaceful mountain lodge.", "🌲 Nature Trails | 🔥 Fireplace | ❄ Air Conditioning", "$180 per night")
]

# Display Hotel Listings
x_offset = 100
for hotel in hotels:
    hotel_frame = Frame(content_frame, bg="white", width=250, height=130, highlightbackground="#D5D8DC", highlightthickness=1)
    hotel_frame.place(x=x_offset, y=220)

    Label(hotel_frame, text=hotel[0], font=("Arial", 10, "bold"), bg="white").place(x=10, y=10)
    Label(hotel_frame, text=hotel[1], font=("Arial", 9), bg="white").place(x=10, y=30)
    Label(hotel_frame, text=hotel[2], font=("Arial", 9), bg="white").place(x=10, y=50)
    Label(hotel_frame, text=hotel[3], font=("Arial", 9, "bold"), fg="blue", bg="white").place(x=10, y=90)

    x_offset += 280  # Move to the next column

root.mainloop()
