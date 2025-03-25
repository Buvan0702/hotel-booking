import customtkinter as ctk

# Initialize App
ctk.set_appearance_mode("light")  # Light Mode
ctk.set_default_color_theme("blue")  # Blue Theme

app = ctk.CTk()
app.title("Hotel Booking - Sign Up")
app.geometry("1000x700")
app.resizable(False, False)

# ----------------- Main Frame -----------------
main_frame = ctk.CTkFrame(app, fg_color="white", corner_radius=15)
main_frame.pack(padx=20, pady=20, expand=True, fill="both")

# ---------------- Left Section (Illustration) -----------------
left_frame = ctk.CTkFrame(main_frame, fg_color="#2C3E50", width=250, corner_radius=15)
left_frame.pack(side="left", fill="y")

ctk.CTkLabel(left_frame, text="🏨", font=("Arial", 50), text_color="white").pack(pady=(60, 10))
ctk.CTkLabel(left_frame, text="Hotel Booking", font=("Arial", 14, "bold"), text_color="white").pack()
ctk.CTkLabel(left_frame, text="Your Stay, Your Way!", font=("Arial", 12), text_color="white").pack(pady=10)

# ---------------- Right Section (Sign-Up Form) -----------------
right_frame = ctk.CTkFrame(main_frame, fg_color="white")
right_frame.pack(side="right", expand=True, fill="both", padx=15, pady=15)

# Title
ctk.CTkLabel(right_frame, text="🏨 Hotel Booking", font=("Arial", 16, "bold"), text_color="#2C3E50").pack(pady=(10, 2))
ctk.CTkLabel(right_frame, text="Create a New Account", font=("Arial", 12), text_color="gray").pack(pady=(0, 15))

# Form Fields
fields = [
    ("👤 Full Name", 1),
    ("📧 Email", 2),
    ("📞 Phone Number", 3),
    ("🔒 Password", 4),
    ("🔑 Confirm Password", 5),
]

entry_fields = {}
for label, row in fields:
    ctk.CTkLabel(right_frame, text=label, font=("Arial", 10)).pack(anchor="w", padx=30)
    entry = ctk.CTkEntry(right_frame, width=250)
    entry.pack(pady=5, padx=30)
    entry_fields[label] = entry

# Terms & Conditions Checkbox
agree_var = ctk.IntVar()
ctk.CTkCheckBox(right_frame, text="I agree to the Terms & Conditions", variable=agree_var).pack(pady=10, padx=30, anchor="w")

# Sign-Up Button
ctk.CTkButton(right_frame, text="Sign Up", fg_color="#1D3557", width=250).pack(pady=10)

# Login Redirect
bottom_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
bottom_frame.pack(pady=5)
ctk.CTkLabel(bottom_frame, text="Already have an account?", font=("Arial", 10)).pack(side="left")
ctk.CTkLabel(bottom_frame, text="Login", text_color="blue", font=("Arial", 10, "bold"), cursor="hand2").pack(side="left", padx=5)

# Run App
app.mainloop()
