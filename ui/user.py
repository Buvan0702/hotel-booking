import customtkinter as ctk
from tkinter import ttk

# Initialize App
ctk.set_appearance_mode("light")  # Light Mode
ctk.set_default_color_theme("blue")  # Blue Theme

app = ctk.CTk()
app.title("Hotel Booking - Customer Profile")
app.geometry("1000x600")
app.resizable(False, False)

# ---------------- Sidebar (Navigation) ---------------- #
sidebar = ctk.CTkFrame(app, fg_color="#2C3E50", width=200, corner_radius=0)
sidebar.pack(side="left", fill="y")

ctk.CTkLabel(sidebar, text="🏨 Hotel Booking", font=("Arial", 14, "bold"), text_color="white").pack(pady=20)

nav_buttons = ["🏠 Home", "📅 Bookings", "👤 Profile", "💬 Feedback", "🔑 Logout"]
for btn_text in nav_buttons:
    ctk.CTkButton(sidebar, text=btn_text, fg_color="#34495E", hover_color="#1D3557", width=180).pack(pady=5)

# ---------------- Main Content ---------------- #
content_frame = ctk.CTkFrame(app, fg_color="white")
content_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(content_frame, text="User Management", font=("Arial", 16, "bold"), text_color="#2C3E50").pack(pady=10)

# ---------------- Edit Profile Section ---------------- #
profile_frame = ctk.CTkFrame(content_frame, fg_color="#F8F9FA", corner_radius=10)
profile_frame.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(profile_frame, text="✏ Edit Profile", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

fields = ["Full Name", "Phone Number", "Email Address", "Address"]
entries = {}

for i, field in enumerate(fields):
    row = ctk.CTkFrame(profile_frame, fg_color="transparent")
    row.pack(fill="x", padx=10, pady=2)
    ctk.CTkLabel(row, text=field, width=120, anchor="w").pack(side="left")
    entries[field] = ctk.CTkEntry(row, width=250)
    entries[field].pack(side="left", padx=10)

ctk.CTkButton(profile_frame, text="Update Profile", fg_color="#007BFF", hover_color="#0056b3", width=200).pack(pady=10)

# ---------------- Booking History Section ---------------- #
history_frame = ctk.CTkFrame(content_frame, fg_color="white", corner_radius=10)
history_frame.pack(pady=10, padx=10, fill="both", expand=True)

ctk.CTkLabel(history_frame, text="🔄 Booking History", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

# Table (Treeview)
columns = ("Booking ID", "Hotel", "Check-in", "Check-out", "Amount", "Status")
tree = ttk.Treeview(history_frame, columns=columns, show="headings", height=5)
tree.pack(fill="both", padx=10, pady=5)

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

app.mainloop()
