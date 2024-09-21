import tkinter as tk
from tkinter import messagebox, ttk

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Sinh Viên")
        
        self.students = []

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Tên Sinh Viên:").grid(row=0, column=0)
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(frame, text="Tuổi:").grid(row=1, column=0)
        self.age_entry = tk.Entry(frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(frame, text="Lớp:").grid(row=2, column=0)
        self.class_entry = tk.Entry(frame)
        self.class_entry.grid(row=2, column=1)

        self.add_button = tk.Button(frame, text="Thêm Sinh Viên", command=self.add_student)
        self.add_button.grid(row=3, columnspan=2)

        self.tree = ttk.Treeview(self.root, columns=("name", "age", "class"), show='headings')
        self.tree.heading("name", text="Tên")
        self.tree.heading("age", text="Tuổi")
        self.tree.heading("class", text="Lớp")
        self.tree.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Xóa Sinh Viên", command=self.delete_student)
        self.delete_button.pack(pady=5)

    def add_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        class_ = self.class_entry.get()

        if name and age and class_:
            self.students.append((name, age, class_))
            self.update_treeview()
            self.clear_entries()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ thông tin!")

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student in self.students:
            self.tree.insert("", "end", values=student)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)

    def delete_student(self):
        selected_item = self.tree.selection()
        if selected_item:
            for item in selected_item:
                self.tree.delete(item)
                index = self.tree.index(item)
                del self.students[index]
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn sinh viên để xóa!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()