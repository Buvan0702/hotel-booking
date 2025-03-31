import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import hashlib
import subprocess  # To open login.py

# ------------------- Database Connection -------------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="new_password",  # Replace with your MySQL password
        database="hotel_booking"  # Replace with your database name
    )

# ------------------- Password Hashing -------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ------------------- Sign Up Function -------------------
def signup_user():
    first_name = entry_fields["👤 First Name"].get()
    last_name = entry_fields["👤 Last Name"].get()
    email = entry_fields["📧 Email"].get()
    password = entry_fields["🔒 Password"].get()
    confirm_password = entry_fields["🔑 Confirm Password"].get()

    # Check if any fields are empty
    if not first_name or not last_name or not email or not password or not confirm_password:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    # Check if passwords match
    if password != confirm_password:
        messagebox.showwarning("Password Error", "Passwords do not match.")
        return

    # Hash the password
    hashed_password = hash_password(password)

    try:
        connection = connect_db()
        cursor = connection.cursor()

        # Insert the user data into the database (without phone number)
        cursor.execute(
            "INSERT INTO Users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, hashed_password)
        )

        connection.commit()
        messagebox.showinfo("Success", "User registered successfully!")
        
        # After successful registration, redirect to login page
        open_login_page()

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# ------------------- Open Login Page -------------------
def open_login_page(event=None):
    try:
        subprocess.run(["python", "login.py"])  # Run signup.py
        app.quit()  # Close the current signup window
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open login page: {e}")

# ----------------- Setup -----------------
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
    ("👤 First Name", 1),
    ("👤 Last Name", 2),
    ("📧 Email", 3),
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
ctk.CTkButton(right_frame, text="Sign Up", fg_color="#1D3557", width=250, command=signup_user).pack(pady=10)

# Login Redirect
bottom_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
bottom_frame.pack(pady=5)
ctk.CTkLabel(bottom_frame, text="Already have an account?", font=("Arial", 10)).pack(side="left")
login_label = ctk.CTkLabel(bottom_frame, text="Login", text_color="blue", font=("Arial", 10, "bold"), cursor="hand2")
login_label.pack(side="left", padx=5)
login_label.bind("<Button-1>", open_login_page)  # Bind click event to open login page

# Run App
app.mainloop()
