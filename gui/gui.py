import re
import os
import random
import string
import customtkinter as ctk
import pyperclip
from datetime import datetime

rockyou = set()
rockyou_loaded = False

def load_rockyou():
    global rockyou, rockyou_loaded
    if os.path.exists("rockyou.txt"):
        try:
            with open("rockyou.txt", "r", encoding="latin-1", errors="ignore") as file:
                rockyou = set(line.strip().lower() for line in file if line.strip())
            rockyou_loaded = True
        except Exception as e:
            print("Error loading rockyou.txt:", e)

def common_pass(pwd):
    return pwd.lower() in rockyou if rockyou_loaded else False

def check_password_strength(pwd):
    length = len(pwd)
    types = sum([
        bool(re.search(r'[A-Z]', pwd)),
        bool(re.search(r'[a-z]', pwd)),
        bool(re.search(r'\d', pwd)),
        bool(re.search(r'[^A-Za-z0-9]', pwd))
    ])
    if length < 6 or common_pass(pwd) or types < 2:
        return 'Weak'
    elif length >= 12 and types == 4:
        return 'Strong'
    else:
        return 'Moderate'

def suggest_strong_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(14))

def update_strength_label(event=None):
    pwd = entry.get()
    if not pwd:
        result_label.configure(text="", text_color="white")
        suggestion_label.configure(text="")
        return
    strength = check_password_strength(pwd)
    colors = {"Weak": "red", "Moderate": "orange", "Strong": "green"}
    result_label.configure(text=f"Strength: {strength}", text_color=colors[strength])
    if strength == "Weak":
        suggestion_label.configure(text=f"💡 Try: {suggest_strong_password()}")
    else:
        suggestion_label.configure(text="")

def toggle_password():
    if entry.cget("show") == "*":
        entry.configure(show="")
        toggle_btn.configure(text="🙈 Hide")
    else:
        entry.configure(show="*")
        toggle_btn.configure(text="👁 Show")

def copy_to_clipboard():
    pwd = entry.get()
    if pwd:
        pyperclip.copy(pwd)
        copy_btn.configure(text="✅ Copied!", fg_color="green")
        app.after(1000, lambda: copy_btn.configure(text="📋 Copy", fg_color="gray"))

def save_report():
    pwd = entry.get()
    if not pwd:
        return
    strength = check_password_strength(pwd)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("Internship\\password_report.txt", "a") as f:
            f.write(f"[{now}] Password: {pwd} | Strength: {strength}\n")
        save_btn.configure(text="💾 Saved!", fg_color="green")
        app.after(1500, lambda: save_btn.configure(text="💾 Save", fg_color="gray"))
    except Exception as e:
        save_btn.configure(text="❌ Failed", fg_color="red")

def switch_theme():
    mode = theme_switch.get()
    ctk.set_appearance_mode("dark" if mode else "light")

# --- GUI Setup ---
load_rockyou()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Password Strength Checker")
app.geometry("460x400")

title = ctk.CTkLabel(app, text="🔐 Password Strength Checker", font=("Arial", 20, "bold"))
title.pack(pady=15)

entry = ctk.CTkEntry(app, placeholder_text="Enter your password", width=300, show="*")
entry.pack(pady=10)
entry.bind("<KeyRelease>", update_strength_label)

btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.pack(pady=5)

toggle_btn = ctk.CTkButton(btn_frame, text="👁 Show", width=100, command=toggle_password)
toggle_btn.grid(row=0, column=0, padx=5)

copy_btn = ctk.CTkButton(btn_frame, text="📋 Copy", width=100, command=copy_to_clipboard)
copy_btn.grid(row=0, column=1, padx=5)

save_btn = ctk.CTkButton(btn_frame, text="💾 Save", width=100, command=save_report)
save_btn.grid(row=0, column=2, padx=5)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
result_label.pack(pady=10)

suggestion_label = ctk.CTkLabel(app, text="", font=("Arial", 12), text_color="yellow")
suggestion_label.pack()

theme_switch = ctk.CTkSwitch(app, text="🌗 Dark Mode", command=switch_theme)
theme_switch.pack(pady=20)
theme_switch.select()

app.mainloop()
