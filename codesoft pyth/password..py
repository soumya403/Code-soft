import tkinter as tk
import random
import string

def generate_password():
    length = int(length_var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Label and Entry for password length
length_label = tk.Label(root, text="Password Length:", font=("Helvetica", 12), fg="blue")
length_label.pack(pady=10)
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, font=("Arial", 12), width=20)
length_entry.pack(pady=5)
length_var.set("10")  # Default password length

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", padx=20, pady=10, font=("Arial", 12), command=generate_password, bg="green", fg="white")
generate_button.pack(pady=10)

# Display generated password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=40, state='readonly', fg="purple")
password_entry.pack(pady=10)

# Run the main loop
root.mainloop()
