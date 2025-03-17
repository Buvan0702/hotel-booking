import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Checkbutton, IntVar

# Initialize main window
root = tk.Tk()
root.title("Hotel Booking Login")
root.geometry("550x325")
root.configure(bg="#F5F5F5")  # Light Grey Background (Matching the Outer UI)

# Main container (Holds both sections)
main_frame = Frame(root, bg="white", width=530, height=300, relief="flat", bd=2)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Left Section - Dark Blue Background (Image Placeholder)
left_frame = Frame(main_frame, bg="#2C3E50", width=250, height=300)
left_frame.place(x=0, y=0)

Label(left_frame, text="🏨", font=("Arial", 40), bg="#2C3E50", fg="white").place(relx=0.5, rely=0.3, anchor="center")
Label(left_frame, text="Hotel Booking", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white").place(relx=0.5, rely=0.6, anchor="center")

# Right Section - Login Form
right_frame = Frame(main_frame, bg="white", width=280, height=300)
right_frame.place(x=250, y=0)

# Title
Label(right_frame, text="🏨 Hotel Booking", font=("Arial", 12, "bold"), bg="white").pack(pady=10)

# Subtitle
Label(right_frame, text="Login to Your Account", font=("Arial", 10), bg="white").pack()

# Email Field
Label(right_frame, text="📧 Email", font=("Arial", 9), bg="white").place(x=20, y=60)
email_entry = Entry(right_frame, width=30, font=("Arial", 9), bd=1, relief="solid")
email_entry.place(x=20, y=80)

# Password Field
Label(right_frame, text="🔒 Password", font=("Arial", 9), bg="white").place(x=20, y=110)
password_entry = Entry(right_frame, width=30, font=("Arial", 9), bd=1, relief="solid", show="*")
password_entry.place(x=20, y=130)

# Remember Me Checkbox
remember_var = IntVar()
Checkbutton(right_frame, text="Remember Me", variable=remember_var, bg="white", font=("Arial", 8)).place(x=20, y=160)

# Forgot Password Link
Label(right_frame, text="Forgot Password?", font=("Arial", 8), fg="blue", bg="white", cursor="hand2").place(x=160, y=160)

# Login Button
Button(right_frame, text="Login", font=("Arial", 10, "bold"), bg="#1D3557", fg="white", width=25, height=1, relief="flat").place(x=20, y=190)

# Sign Up Link
Label(right_frame, text="Don't have an account?", font=("Arial", 8), bg="white").place(x=40, y=230)
Label(right_frame, text="Sign Up", font=("Arial", 8, "bold"), fg="blue", bg="white", cursor="hand2").place(x=180, y=230)

root.mainloop()
