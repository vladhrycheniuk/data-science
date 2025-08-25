import csv
import tkinter as tk
from tkinter import ttk

# --- Зчитування даних з CSV ---
students = []
with open('student.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students.append({"name": row["name"], "score": int(row["score"])})

high_achievers = [s for s in students if s["score"] >= 80]

# --- Функція для сортування таблиці ---
def sort_tree(tree, data, col, reverse=False):
    data.sort(key=lambda x: x[col], reverse=reverse)
    for row in tree.get_children():
        tree.delete(row)
    for s in data:
        tree.insert("", "end", values=(s["name"], s["score"]))

# --- Створення GUI ---
root = tk.Tk()
root.title("Student Scores")
root.geometry("400x400")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# --- Вкладка: всі студенти ---
frame_all = ttk.Frame(notebook)
notebook.add(frame_all, text="All Students")

tree_all = ttk.Treeview(frame_all, columns=("name", "score"), show="headings")
tree_all.heading("name", text="Name", command=lambda: sort_tree(tree_all, students, "name"))
tree_all.heading("score", text="Score", command=lambda: sort_tree(tree_all, students, "score", True))
tree_all.pack(fill="both", expand=True)

for s in students:
    tree_all.insert("", "end", values=(s["name"], s["score"]))

# --- Вкладка: high achievers ---
frame_high = ttk.Frame(notebook)
notebook.add(frame_high, text="High Achievers (>=80)")

tree_high = ttk.Treeview(frame_high, columns=("name", "score"), show="headings")
tree_high.heading("name", text="Name", command=lambda: sort_tree(tree_high, high_achievers, "name"))
tree_high.heading("score", text="Score", command=lambda: sort_tree(tree_high, high_achievers, "score", True))
tree_high.pack(fill="both", expand=True)

for s in high_achievers:
    tree_high.insert("", "end", values=(s["name"], s["score"]))

root.mainloop()
