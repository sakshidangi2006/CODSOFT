import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self,root):
        self.root = root
        self.root.title("ToDo App")
        self.root.geometry("400x500")
        self.root.configure(bg="#959292")

        self.label = tk.Label(root, text="My Tasks", font=("Arial",18,"bold"),bg="#f5f5f5")
        self.label.pack(pady=10)

        self.task_entry = tk.Entry(root, font=("Arial",12),width=30)
        self.task_entry.pack(pady=5)
        self.task_entry.bind('<Return>',lambda event: self.add_task())

        btn_frame = tk.Frame(root, bg="#908D8D")
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(btn_frame, text="Add Task", command=self.add_task, bg="#125432", fg="white", width=10)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.del_btn = tk.Button(btn_frame, text="Delete", command=self.delete_task, bg="#ed2516", fg="white", width=10)
        self.del_btn.grid(row=0, column=1, padx=5)

        list_frame = tk.Frame(root)
        list_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, font=("Arial",12),height=10,
                                 yscrollcommand=self.scrollbar.set, selectmode=tk.SINGLE)
        
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)

        self.clear_btn = tk.Button(root, text="Clear All Tasks", command=self.clear_all, bg="#555555", fg="white")
        self.clear_btn.pack(pady=10)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.listbox.insert(tk.END, f". {task}")
            self.task_entry.delete(0, tk.END)
            self.save_tasks()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task name.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error","Please select a task to delete")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all everything."):
            self.listbox.delete(0, tk.END)
            self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt","w") as f:
            tasks = self.listbox.get(0,tk.END)
            for t in tasks:
                f.write(t + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt","r") as f:
                for line in f:
                    self.listbox.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

        
        
        

            