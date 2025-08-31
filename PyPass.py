import customtkinter as ctk

# App settings
ctk.set_appearance_mode("dark")  # "light" or "dark"
ctk.set_default_color_theme("blue")

# Create window
app = ctk.CTk()
app.title("Password Checker")
app.geometry("400x250")

# Title
title_label = ctk.CTkLabel(app, text="🔐 Password Checker", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Entry
password_entry = ctk.CTkEntry(app, placeholder_text="Enter your password", show="*")
password_entry.pack(pady=10, padx=20, fill="x")

# Result label
result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Check function
def check_password():
    pwd = password_entry.get()
    if pwd in compromised_passwords:
        result_label.configure(text="❌ Warning! Your Password has been compromised! Change it Now.", text_color="red")
    else:
        result_label.configure(text="✅ Your Password is unique! Keep it up!", text_color="green")

# Button
check_button = ctk.CTkButton(app, text="Check Password", command=check_password)
check_button.pack(pady=10)

# Load compromised passwords
with open("rockyou_utf8.txt", "r", encoding="latin-1", errors="ignore") as file:
    compromised_passwords = set(line.strip() for line in file)

app.mainloop()
