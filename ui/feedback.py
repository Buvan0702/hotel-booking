import customtkinter as ctk
from tkinter import ttk

# Initialize App
ctk.set_appearance_mode("light")  # Light Mode
ctk.set_default_color_theme("blue")  # Blue Theme

app = ctk.CTk()
app.title("Hotel Booking - Feedback Screen")
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

ctk.CTkLabel(content_frame, text="Give Your Feedback", font=("Arial", 16, "bold"), text_color="#2C3E50").pack(pady=10)

# ---------------- Feedback Form ---------------- #
feedback_frame = ctk.CTkFrame(content_frame, fg_color="#F8F9FA", corner_radius=10)
feedback_frame.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(feedback_frame, text="💬 We Value Your Feedback", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

# Full Name Entry
row1 = ctk.CTkFrame(feedback_frame, fg_color="transparent")
row1.pack(fill="x", padx=10, pady=5)
ctk.CTkLabel(row1, text="👤 Full Name", width=120, anchor="w").pack(side="left")
name_entry = ctk.CTkEntry(row1, width=300)
name_entry.pack(side="left", padx=10)

# Rating Stars
ctk.CTkLabel(feedback_frame, text="⭐ Rate Your Experience").pack(anchor="w", padx=10)
rating_frame = ctk.CTkFrame(feedback_frame, fg_color="transparent")
rating_frame.pack(anchor="w", padx=10, pady=5)

stars = []
def set_rating(value):
    for i in range(5):
        stars[i].configure(text="⭐" if i < value else "☆")

for i in range(5):
    star_btn = ctk.CTkButton(rating_frame, text="☆", width=30, height=30, font=("Arial", 20), fg_color="white", text_color="black", command=lambda i=i+1: set_rating(i))
    star_btn.pack(side="left", padx=5)
    stars.append(star_btn)

# Feedback Text Box
ctk.CTkLabel(feedback_frame, text="💭 Your Feedback").pack(anchor="w", padx=10)
feedback_text = ctk.CTkTextbox(feedback_frame, width=400, height=100)
feedback_text.pack(padx=10, pady=5)

# Submit Button
submit_button = ctk.CTkButton(feedback_frame, text="Submit Feedback", fg_color="#007BFF", hover_color="#0056b3", width=200)
submit_button.pack(pady=10)

app.mainloop()
