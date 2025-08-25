import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Button

# Load data
df = pd.read_csv("sales.csv", parse_dates=["date"])
df["Revenue"] = df["quantity"] * df["price"]
df["Month"] = df["date"].dt.to_period("M")

# --- Functions for plots ---
def revenue_by_month():
    revenue = df.groupby("Month")["Revenue"].sum()
    revenue.plot(kind="line", marker="o", figsize=(8,5), title="Revenue by Month")
    plt.ylabel("Revenue ($)")
    plt.grid(True)
    plt.show()

def revenue_by_product():
    revenue = df.groupby("product")["Revenue"].sum().sort_values(ascending=False)
    revenue.plot(kind="bar", figsize=(8,5), title="Revenue by Product", color="skyblue")
    plt.ylabel("Revenue ($)")
    plt.show()

def top_days():
    top_days = df.groupby(df["date"].dt.date)["Revenue"].sum().sort_values(ascending=False).head(5)
    top_days.plot(kind="bar", figsize=(8,5), title="Top 5 Sales Days", color="orange")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=30)
    plt.show()

def price_distribution():
    plt.figure(figsize=(8,6))
    sns.boxplot(x="product", y="price", data=df, palette="Set2")
    plt.title("Price Distribution by Product")
    plt.ylabel("Price ($)")
    plt.xlabel("Product")
    plt.show()

def heatmap():
    pivot = df.pivot_table(index="Month", columns="product", values="Revenue", aggfunc="sum").fillna(0)
    plt.figure(figsize=(8,6))
    sns.heatmap(pivot, cmap="YlGnBu", annot=True, fmt=".0f")
    plt.title("Revenue Heatmap (Month × Product)")
    plt.show()

def pie_chart():
    revenue = df.groupby("product")["Revenue"].sum()
    plt.figure(figsize=(6,6))
    plt.pie(revenue, labels=revenue.index, autopct="%1.1f%%", startangle=90, colors=sns.color_palette("Set2"))
    plt.title("Revenue Share by Product")
    plt.show()

# --- Tkinter GUI ---
root = Tk()
root.title("Sales Analysis Dashboard")

Button(root, text="Revenue by Month", width=25, command=revenue_by_month).pack(pady=5)
Button(root, text="Revenue by Product", width=25, command=revenue_by_product).pack(pady=5)
Button(root, text="Top 5 Sales Days", width=25, command=top_days).pack(pady=5)
Button(root, text="Price Distribution", width=25, command=price_distribution).pack(pady=5)
Button(root, text="Revenue Heatmap", width=25, command=heatmap).pack(pady=5)
Button(root, text="Revenue Share (Pie)", width=25, command=pie_chart).pack(pady=5)
Button(root, text="Exit", width=25, command=root.quit).pack(pady=5)

root.mainloop()
