import tkinter as tk
from tkinter import messagebox
import string
import secrets

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_random = secrets.SystemRandom()
    password = ''.join(secure_random.choice(characters) for _ in range(length))
    return password

def generate_password_gui():
    """Generate password button click handler."""
    try:
        password_length = int(length_entry.get())
        if password_length < 1:
            messagebox.showwarning("Invalid Length", "Password length must be at least 1.")
            return
        password = generate_password(password_length)
        password_output.config(state=tk.NORMAL)
        password_output.delete(1.0, tk.END)
        password_output.insert(tk.END, password)
        password_output.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create GUI components
tk.Label(window, text="Password Length:").pack(pady=10)
length_entry = tk.Entry(window, width=10)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=10)

password_output = tk.Text(window, height=1, width=30, state=tk.DISABLED)
password_output.pack(pady=10)

# Start the GUI event loop
window.mainloop()

