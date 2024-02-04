import tkinter as tk
from tkinter import messagebox
import json

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x300")

        # Load contacts from file
        self.load_contacts()

        # GUI components
        self.heading_label = tk.Label(root, text="Contact Book", font=("Helvetica", 16, "bold"), fg="purple")
        self.heading_label.pack(side="top", pady=20)

        self.name_label = tk.Label(root, text="Name:", font=("Helvetica", 12), fg="blue")
        self.name_label.pack(side="top", pady=5)

        self.name_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.name_entry.pack(side="top", pady=5)

        self.number_label = tk.Label(root, text="Phone Number:", font=("Helvetica", 12), fg="blue")
        self.number_label.pack(side="top", pady=5)

        self.number_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.number_entry.pack(side="top", pady=5)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="top", pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, bg="green", fg="white", font=("Helvetica", 12))
        self.add_button.pack(side="left", padx=5)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, bg="orange", fg="white", font=("Helvetica", 12))
        self.search_button.pack(side="left", padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, bg="red", fg="white", font=("Helvetica", 12))
        self.delete_button.pack(side="left", padx=5)

        self.info_label = tk.Label(root, text="", font=("Helvetica", 12), fg="black")
        self.info_label.pack(side="top", pady=20)

    def add_contact(self):
        name = self.name_entry.get()
        number = self.number_entry.get()
        if name:
            if name.lower() not in map(str.lower, self.contacts.keys()):  # Case-insensitive check
                self.contacts[name] = number
                messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
                self.save_contacts()
                self.clear_entries()
            else:
                messagebox.showerror("Error", f"Contact with name '{name}' already exists.")
        else:
            messagebox.showerror("Error", "Please enter a name.")

    def search_contact(self):
        name = self.name_entry.get()
        if name:
            if name.lower() in map(str.lower, self.contacts.keys()):  # Case-insensitive check
                real_name = next(key for key in self.contacts if key.lower() == name.lower())
                self.display_contact(real_name)
            else:
                messagebox.showerror("Contact Not Found", f"Contact with name '{name}' not found.")
        else:
            messagebox.showerror("Error", "Please enter a name.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            if name.lower() in map(str.lower, self.contacts.keys()):  # Case-insensitive check
                real_name = next(key for key in self.contacts if key.lower() == name.lower())
                del self.contacts[real_name]
                messagebox.showinfo("Success", f"Contact '{real_name}' deleted successfully!")
                self.save_contacts()
                self.clear_entries()
            else:
                messagebox.showerror("Error", f"Contact with name '{name}' not found.")
        else:
            messagebox.showerror("Error", "Please enter a name.")

    def display_contact(self, name):
        self.info_label.config(text=f"Name: {name}\nPhone Number: {self.contacts[name]}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)
        self.info_label.config(text="")

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            # If the file is not found, initialize an empty dictionary
            self.contacts = {}

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lightgray")
    app = ContactBookApp(root)
    root.mainloop()


