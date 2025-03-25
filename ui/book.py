import customtkinter as ctk

# Initialize App
ctk.set_appearance_mode("light")  # Light Mode
ctk.set_default_color_theme("blue")  # Blue Theme

app = ctk.CTk()
app.title("Hotel Booking")
app.geometry("1000x600")
app.resizable(False, False)

# ---------------- Sidebar (Navigation) ---------------- #
sidebar = ctk.CTkFrame(app, fg_color="#2C3E50", width=200, corner_radius=0)
sidebar.pack(side="left", fill="y")

ctk.CTkLabel(sidebar, text="🏨 Hotel Booking", font=("Arial", 14, "bold"), text_color="white").pack(pady=20)

nav_buttons = ["🏠 Home", "📅 Bookings", "👤 Profile", "💬 Feedback", "🔑 Logout"]
for btn_text in nav_buttons:
    ctk.CTkButton(sidebar, text=btn_text, fg_color="#34495E", hover_color="#1D3557", width=180).pack(pady=5)

# ---------------- Booking Section ---------------- #
booking_frame = ctk.CTkFrame(app, fg_color="white")
booking_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(booking_frame, text="Luxury Grand Hotel", font=("Arial", 16, "bold"), text_color="#2C3E50").pack(pady=10)
ctk.CTkLabel(booking_frame, text="📍 123 Main Street, Mt. Pleasant, Michigan", font=("Arial", 10)).pack()

# ---------------- Booking Form ---------------- #
form_frame = ctk.CTkFrame(booking_frame, fg_color="white", border_width=1, border_color="#D5D8DC")
form_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(form_frame, text="📅 Select Your Stay", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

form_fields = ["Check-in Date", "Check-out Date", "Guests", "Room Type"]
entry_fields = {}
for field in form_fields:
    row = ctk.CTkFrame(form_frame, fg_color="white")
    row.pack(fill="x", padx=10, pady=5)
    
    ctk.CTkLabel(row, text=field, font=("Arial", 10, "bold"), width=120).pack(side="left")
    entry = ctk.CTkEntry(row, width=200) if "Room Type" not in field else ctk.CTkComboBox(row, values=["Single - $150", "Double - $200"])
    entry.pack(side="left", padx=10)
    entry_fields[field] = entry

# Payment Method
ctk.CTkLabel(form_frame, text="💳 Payment Method", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
payment_method = ctk.StringVar(value="Card")

row = ctk.CTkFrame(form_frame, fg_color="white")
row.pack(fill="x", padx=10, pady=5)
ctk.CTkRadioButton(row, text="Credit/Debit Card", variable=payment_method, value="Card").pack(side="left", padx=10)
ctk.CTkRadioButton(row, text="PayPal", variable=payment_method, value="PayPal").pack(side="left", padx=10)

ctk.CTkButton(form_frame, text="Confirm Booking", fg_color="#FFC107", text_color="black", width=200).pack(pady=10)

# ---------------- Booking Summary ---------------- #
summary_frame = ctk.CTkFrame(booking_frame, fg_color="white", border_width=1, border_color="#D5D8DC", width=300)
summary_frame.pack(pady=10, padx=20, fill="x")

ctk.CTkLabel(summary_frame, text="📝 Booking Summary", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
summary_labels = [
    "Hotel: Luxury Grand Hotel", 
    "Location: New York, USA", 
    "Room Type: Single Room", 
    "Price per Night: $150", 
    "Total Nights: 2", 
    "Total Price: $300"
]

for label in summary_labels:
    ctk.CTkLabel(summary_frame, text=label).pack(anchor="w", padx=10)

app.mainloop()
