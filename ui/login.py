import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
import hashlib
import subprocess
import sys

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
# ------------------- Open Sign Up Page -------------------
def open_signup():
    try:
        subprocess.Popen([sys.executable, "signup.py"])
        root.destroy()  # Close the current login window
    except Exception as e:
        messagebox.showerror("Error", f"Unable to open signup page: {e}")
# ------------------- Login Function -------------------
def login_user():
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showwarning("Input Error", "Please enter both email and password.")
        return

    hashed_password = hash_password(password)

    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT first_name, last_name FROM Users WHERE email = %s AND password = %s",
            (email, hashed_password)
        )
        user = cursor.fetchone()

        if user:
            first_name, last_name = user
            messagebox.showinfo("Success", f"Welcome {first_name} {last_name}!")
            # Open home page or next screen here
            app.quit()  # Close the login window
            open_home_page()  # This will open the home page after login
        else:
            messagebox.showerror("Login Failed", "Invalid Email or Password.")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# ------------------- Open Home Page -------------------
def open_home_page():
    # Code to open home page (e.g., home.py or just a new window)
    home_page = ctk.CTk()
    home_page.title("Hotel Booking - Home")
    home_page.geometry("1000x800")
    home_page.resizable(False, False)

    ctk.CTkLabel(home_page, text="Welcome to the Hotel Booking System!", font=("Arial", 20, "bold")).pack(pady=20)
    
    # Add your home page content here

    home_page.mainloop()

# ----------------- Setup -----------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Hotel Booking Login")
app.geometry("1000x800")
app.resizable(False, False)

# ----------------- Main Frame -----------------
main_frame = ctk.CTkFrame(app, fg_color="white", corner_radius=15)
main_frame.pack(padx=20, pady=20, expand=True, fill="both")

# ----------------- Left Frame (Branding) -----------------
left_frame = ctk.CTkFrame(main_frame, fg_color="#2C3E50", width=250, corner_radius=15)
left_frame.pack(side="left", fill="y")

ctk.CTkLabel(left_frame, text="🏨", font=("Arial", 45), text_color="white").pack(pady=(50, 10))
ctk.CTkLabel(left_frame, text="Hotel Booking", font=("Arial", 14, "bold"), text_color="white").pack()

# ----------------- Right Frame (Login Form) -----------------
right_frame = ctk.CTkFrame(main_frame, fg_color="white")
right_frame.pack(side="right", expand=True, fill="both", padx=15, pady=15)

# Top Titles
ctk.CTkLabel(right_frame, text="🏨 Hotel Booking", font=("Arial", 16, "bold"), text_color="#2C3E50").pack(pady=(10, 2))
ctk.CTkLabel(right_frame, text="Login to Your Account", font=("Arial", 12), text_color="gray").pack(pady=(0, 15))

# Email
ctk.CTkLabel(right_frame, text="Email", anchor="w", font=("Arial", 10)).pack(fill="x", padx=30)
email_entry = ctk.CTkEntry(right_frame, width=200)
email_entry.pack(padx=30, pady=5)

# Password
ctk.CTkLabel(right_frame, text="Password", anchor="w", font=("Arial", 10)).pack(fill="x", padx=30, pady=(10, 0))
password_entry = ctk.CTkEntry(right_frame, show="*", width=200)
password_entry.pack(padx=30, pady=5)

# Options Row
options_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
options_frame.pack(fill="x", padx=30, pady=(5, 10))

remember_var = ctk.IntVar()
ctk.CTkCheckBox(options_frame, text="Remember Me", variable=remember_var).pack(side="left")
ctk.CTkLabel(options_frame, text="Forgot Password?", text_color="blue", font=("Arial", 10), cursor="hand2").pack(side="right")

# Login Button
login_btn = ctk.CTkButton(right_frame, text="Login", fg_color="#1D3557", width=200, command=login_user)
login_btn.pack(pady=(5, 10))

# Sign Up
signup_frame = ctk.CTkFrame(right_frame, fg_color="transparent")
signup_frame.pack()
ctk.CTkLabel(signup_frame, text="Don't have an account?", font=("Arial", 10)).pack(side="left")
ctk.CTkLabel(signup_frame, text="Sign Up", text_color="blue", font=("Arial", 10, "bold"), cursor="hand2", command=open_signup()).pack(side="left", padx=5)

# Run App
app.mainloop()
