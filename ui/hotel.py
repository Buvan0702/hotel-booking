import customtkinter as ctk

# Initialize App
ctk.set_appearance_mode("light")  # Light Mode
ctk.set_default_color_theme("blue")  # Blue Theme

app = ctk.CTk()
app.title("Hotel Booking - Customer Home")
app.geometry("1000x600")
app.resizable(False, False)

# ---------------- Sidebar (Navigation) ---------------- #
sidebar = ctk.CTkFrame(app, fg_color="#2C3E50", width=200, corner_radius=0)
sidebar.pack(side="left", fill="y")

ctk.CTkLabel(sidebar, text="🏨 Hotel Booking", font=("Arial", 14, "bold"), text_color="white").pack(pady=20)

# Sidebar Buttons
nav_buttons = [
    ("🏠 Home"),
    ("📅 Bookings"),
    ("👤 Profile"),
    ("💬 Feedback"),
    ("🔑 Logout")
]

for btn_text in nav_buttons:
    ctk.CTkButton(sidebar, text=btn_text, fg_color="#34495E", hover_color="#1D3557", width=180).pack(pady=5)

# ---------------- Main Content ---------------- #
content_frame = ctk.CTkFrame(app, fg_color="white")
content_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(content_frame, text="Find Your Perfect Stay", font=("Arial", 16, "bold"), text_color="#2C3E50").pack(pady=10)

# ---------------- Search Section ---------------- #
search_frame = ctk.CTkFrame(content_frame, fg_color="white", border_width=1, border_color="#D5D8DC")
search_frame.pack(pady=10, padx=20, fill="x")

search_fields = [
    ("📍 Location", 150),
    ("📅 Check-in Date", 120),
    ("📅 Check-out Date", 120),
    ("👤 Guests", 80)
]

entry_fields = {}
for label_text, width in search_fields:
    row = ctk.CTkFrame(search_frame, fg_color="white")
    row.pack(side="left", padx=10, pady=10)
    
    ctk.CTkLabel(row, text=label_text, font=("Arial", 10, "bold")).pack(anchor="w")
    entry = ctk.CTkEntry(row, width=width)
    entry.pack()
    entry_fields[label_text] = entry

ctk.CTkButton(search_frame, text="Search Rooms", fg_color="#FFC107", text_color="black", width=120).pack(side="left", padx=10, pady=10)

# ---------------- Popular Hotels Section ---------------- #
ctk.CTkLabel(content_frame, text="Popular Hotels", font=("Arial", 14, "bold"), text_color="#2C3E50").pack(pady=10)

hotels = [
    ("Luxury Grand Hotel", "A 5-star hotel with exclusive services and amenities.", "📶 Free WiFi | 🏊 Pool | 🚗 Free Parking", "$250 per night"),
    ("Ocean View Resort", "Enjoy stunning ocean views with top-notch hospitality.", "🍽 Restaurant | 🧖 Spa | 🍳 Breakfast", "$300 per night"),
    ("Mountain Retreat Lodge", "Escape to nature with this peaceful mountain lodge.", "🌲 Nature Trails | 🔥 Fireplace | ❄ Air Conditioning", "$180 per night")
]

hotel_frame = ctk.CTkFrame(content_frame, fg_color="white")
hotel_frame.pack(pady=10)

for hotel in hotels:
    card = ctk.CTkFrame(hotel_frame, fg_color="white", border_width=1, border_color="#D5D8DC", width=280, height=140)
    card.pack(side="left", padx=10, pady=10)
    
    ctk.CTkLabel(card, text=hotel[0], font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
    ctk.CTkLabel(card, text=hotel[1], font=("Arial", 10), wraplength=250).pack(anchor="w", padx=10)
    ctk.CTkLabel(card, text=hotel[2], font=("Arial", 9), wraplength=250).pack(anchor="w", padx=10)
    ctk.CTkLabel(card, text=hotel[3], font=("Arial", 10, "bold"), text_color="blue").pack(anchor="w", padx=10, pady=5)

# Run App
app.mainloop()
