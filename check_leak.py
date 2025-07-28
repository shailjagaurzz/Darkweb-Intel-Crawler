from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

def show_popup(title, message, kind="info"):
    # Create a hidden root window for popup
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    if kind == "info":
        messagebox.showinfo(title, message)
    elif kind == "warning":
        messagebox.showwarning(title, message)
    elif kind == "error":
        messagebox.showerror(title, message)

    root.destroy()

def send_email_alert(to_email, found_email):
    msg = MIMEText(f"⚠️ Leak found for: {found_email}")
    msg['Subject'] = "Leak Alert!"
    msg['From'] = "your_email@example.com"
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_app_password")
        server.send_message(msg)

def main():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["darkweb_leaks"]
    collection = db["leaked_emails"]

    # Take email input from terminal
    email = input("🔐 Enter your email to check for leaks: ").strip().lower()

    # Check for leak
    leak = collection.find_one({"email": email})

    if leak:
        print(f"❗ Leak found for: {email}")
        show_popup("Leak Alert", f"⚠️ Leak found for: {email}", kind="warning")
        send_email_alert("your_email@example.com", email)
    else:
        print(f"✅ No leak found for: {email}")
        show_popup("All Clear", f"No leak found for: {email}", kind="info")

if __name__ == "__main__":
    main()
