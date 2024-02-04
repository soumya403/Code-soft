import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root=root
        self.root.title("Todo App")

        # Calculate center position
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        window_width=400
        window_height=300
        x_position=(screen_width - window_width) // 2
        y_position=(screen_height - window_height) // 2

        # Set the window size and position
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Task list
        self.tasks=[]

        # GUI setup
        self.setup_ui()

    def setup_ui(self):
        # Title label
        title_label=tk.Label(self.root, text="Todo List", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry widget to add tasks
        self.task_entry=tk.Entry(self.root, width=30, font=("Arial", 12))
        self.task_entry.grid(row=1, column=0, padx=10, pady=10)

        # Add Task button
        add_button=tk.Button(self.root, text="Add Task", command=self.add_task, font=("Arial", 12))
        add_button.grid(row=1, column=1, padx=10, pady=10)

        # Task listbox
        self.task_listbox=tk.Listbox(self.root, width=40, height=10, font=("Arial", 12))
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Delete Task button
        delete_button=tk.Button(self.root, text="Delete Task", command=self.delete_task, font=("Arial", 12))
        delete_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task=self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index=self.task_listbox.curselection()
        if selected_index:
            task=self.tasks.pop(selected_index[0])
            messagebox.showinfo("Task Deleted", f"Task '{task}' has been deleted.")
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root=tk.Tk()
    app=TodoApp(root)
    root.mainloop()
