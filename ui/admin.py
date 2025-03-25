import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Initialize App
ctk.set_appearance_mode("light")  # Light Mode
ctk.set_default_color_theme("blue")  # Blue Theme

app = ctk.CTk()
app.title("Admin Dashboard - Hotel Booking")
app.geometry("1000x600")
app.resizable(False, False)

# ---------------- Sidebar (Navigation) ---------------- #
sidebar = ctk.CTkFrame(app, fg_color="#2C3E50", width=200, corner_radius=0)
sidebar.pack(side="left", fill="y")

ctk.CTkLabel(sidebar, text="🏨 Hotel Booking", font=("Arial", 14, "bold"), text_color="white").pack(pady=20)

nav_buttons = ["📊 Dashboard", "📅 Manage Bookings", "👤 Manage Users", "🔑 Logout"]
for btn_text in nav_buttons:
    ctk.CTkButton(sidebar, text=btn_text, fg_color="#34495E", hover_color="#1D3557", width=180).pack(pady=5)

# ---------------- Dashboard Section ---------------- #
dashboard_frame = ctk.CTkFrame(app, fg_color="white")
dashboard_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

ctk.CTkLabel(dashboard_frame, text="Admin Dashboard", font=("Arial", 16, "bold"), text_color="#2C3E50").pack(pady=10)

# ---------------- Stats Cards ---------------- #
stats = [
    ("Total Bookings", "1,250"),
    ("Total Revenue", "$325,000"),
    ("Active Users", "2,500"),
    ("Hotels Listed", "85")
]

stats_frame = ctk.CTkFrame(dashboard_frame, fg_color="white")
stats_frame.pack(pady=5)

for text, value in stats:
    card = ctk.CTkFrame(stats_frame, fg_color="#F8F9FA", width=220, height=80, corner_radius=10)
    card.pack(side="left", padx=10, pady=10)
    ctk.CTkLabel(card, text=text, font=("Arial", 12, "bold"), text_color="#2C3E50").pack(pady=5)
    ctk.CTkLabel(card, text=value, font=("Arial", 14), text_color="black").pack()

# ---------------- Graph (Revenue & Bookings) ---------------- #
ctk.CTkLabel(dashboard_frame, text="📈 Revenue & Bookings Overview", font=("Arial", 12, "bold")).pack(pady=10)

fig, ax = plt.subplots(figsize=(5, 2))
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [40000, 45000, 50000, 55000, 65000, 75000]
bookings = [100, 150, 200, 250, 300, 350]

ax.plot(months, revenue, label="Revenue ($)", color="blue")
ax.plot(months, bookings, label="Bookings", color="green")
ax.legend()

canvas = FigureCanvasTkAgg(fig, master=dashboard_frame)
canvas.get_tk_widget().pack()

app.mainloop()
