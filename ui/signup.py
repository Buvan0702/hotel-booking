import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Checkbutton, IntVar

# Initialize main window
root = tk.Tk()
root.title("Hotel Booking - Sign Up")
root.geometry("1000x550")
root.configure(bg="#EDEDED")  # Light Grey Background

# ---------------- Left Side - Dark Blue Section ---------------- #
left_frame = Frame(root, bg="#2C3E50", width=400, height=550)
left_frame.place(x=0, y=0)

Label(left_frame, text="🏨 Hotel Illustration Here", font=("Arial", 12, "bold"), fg="white", bg="#2C3E50").place(x=100, y=250)

# ---------------- Right Side - Sign-Up Form ---------------- #
form_frame = Frame(root, bg="white", width=600, height=550)
form_frame.place(x=400, y=0)

Label(form_frame, text="🏨 Hotel Booking", font=("Arial", 14, "bold"), bg="white").place(x=200, y=40)
Label(form_frame, text="Create a New Account", font=("Arial", 12), bg="white").place(x=200, y=70)

# Form Fields
labels = [
    ("👤 Full Name", 120),
    ("📧 Email", 170),
    ("📞 Phone Number", 220),
    ("🔒 Password", 270),
    ("🔑 Confirm Password", 320),
]
entries = []
for text, y in labels:
    Label(form_frame, text=text, font=("Arial", 10), bg="white").place(x=50, y=y)
    entry = Entry(form_frame, width=40, font=("Arial", 10))
    entry.place(x=50, y=y+20)
    entries.append(entry)

# Checkbox for Terms
agree_var = IntVar()
Checkbutton(form_frame, text="I agree to the Terms & Conditions", bg="white", variable=agree_var).place(x=50, y=370)

# Sign-Up Button
Button(form_frame, text="Sign Up", font=("Arial", 12, "bold"), bg="#001F3F", fg="white", width=30, height=2).place(x=50, y=400)

# Login Redirect
Label(form_frame, text="Already have an account?", bg="white", font=("Arial", 10)).place(x=140, y=450)
Button(form_frame, text="Login", font=("Arial", 10, "bold"), fg="blue", relief="flat", bg="white").place(x=280, y=445)

root.mainloop()
