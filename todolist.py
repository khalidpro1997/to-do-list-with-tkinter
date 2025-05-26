import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        # Entry for new task
        self.entry = tk.Entry(root, width=30, font=('Arial', 14))
        self.entry.pack(pady=10)

        # Add Task button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Listbox to display tasks
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.listbox.pack(pady=10)

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.pack()

        # Save and Load buttons
        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=(10, 0))

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            self.tasks.pop(index)
        else:
            messagebox.showwarning("Select Error", "Please select a task to delete.")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as f:
                for task in self.tasks:
                    f.write(task + '\n')

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                self.tasks = [line.strip() for line in lines]
                self.listbox.delete(0, tk.END)
                for task in self.tasks:
                    self.listbox.insert(tk.END, task)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
