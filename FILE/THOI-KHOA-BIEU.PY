import tkinter as tk
from tkinter import messagebox
import pandas as pd

class TimeTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thời Khóa Biểu")

        self.days = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7"]
        self.periods = ["Tiết 1", "Tiết 2", "Tiết 3", "Tiết 4","tiết 5", "Tiết 6", "Tiết 7", "Tiết 8"]

        self.create_table()

    def create_table(self):
        for col, day in enumerate(self.days):
            label = tk.Label(self.root, text=day, borderwidth=1, relief="solid")
            label.grid(row=0, column=col + 1, sticky="nsew")

        for row, period in enumerate(self.periods):
            label = tk.Label(self.root, text=period, borderwidth=1, relief="solid")
            label.grid(row=row + 1, column=0, sticky="nsew")

        self.entries = {}
        for row in range(len(self.periods)):
            for col in range(len(self.days)):
                entry = tk.Entry(self.root, width=20)
                entry.grid(row=row + 1, column=col + 1, sticky="nsew")
                self.entries[(row, col)] = entry

        for i in range(len(self.days) + 1):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(len(self.periods) + 1):
            self.root.grid_rowconfigure(i, weight=1)

        btn_show = tk.Button(self.root, text="Hiển thị ghi chú", command=self.show_notes)
        btn_show.grid(row=len(self.periods) + 1, columnspan=len(self.days) + 1)

        btn_save = tk.Button(self.root, text="Lưu vào Excel", command=self.save_to_excel)
        btn_save.grid(row=len(self.periods) + 2, columnspan=len(self.days) + 1)

    def show_notes(self):
        notes = ""
        for (row, col), entry in self.entries.items():
            text = entry.get()
            if text:
                notes += f"{self.periods[row]} - {self.days[col]}: {text}\n"
        if notes:
            messagebox.showinfo("Ghi chú", notes)
        else:
            messagebox.showinfo("Ghi chú", "Không có ghi chú nào.")

    def save_to_excel(self):
        data = {day: [] for day in self.days}
        for row in range(len(self.periods)):
            for col in range(len(self.days)):
                text = self.entries[(row, col)].get()
                data[self.days[col]].append(text)

        df = pd.DataFrame(data, index=self.periods)
        try:
            df.to_excel("thoi_khoa_bieu.xlsx")
            messagebox.showinfo("Thông báo", "Đã lưu vào thoi_khoa_bieu.xlsx")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTableApp(root)
    root.mainloop()