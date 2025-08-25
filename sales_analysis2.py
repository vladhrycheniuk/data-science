import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("sales.csv")
data["Revenue"] = data["quantity"] * data["price"]
data["date"] = pd.to_datetime(data["date"])
data["month"] = data["date"].dt.to_period("M")

# --- Basic stats ---
print("\n--- Basic Sales Stats ---")
print(f"Total Revenue: ${data['Revenue'].sum():,.2f}")
print(f"Average Revenue per transaction: ${data['Revenue'].mean():,.2f}")
print(f"Total Quantity Sold: {data['quantity'].sum()} units")

# --- Top Products ---
top3_revenue = data.groupby("product")["Revenue"].sum().sort_values(ascending=False).head(3)
top3_quantity = data.groupby("product")["quantity"].sum().sort_values(ascending=False).head(3)
print("\nTop 3 Products by Revenue:")
print(top3_revenue)
print("\nTop 3 Products by Quantity Sold:")
print(top3_quantity)

# --- Revenue and Quantity by Month ---
rev_by_month = data.groupby("month")["Revenue"].sum()
qty_by_month = data.groupby("month")["quantity"].sum()
print("\nRevenue by Month:")
print(rev_by_month)
print("\nQuantity Sold by Month:")
print(qty_by_month)

# --- Share of Revenue and Quantity ---
share_revenue = data.groupby("product")["Revenue"].sum() / data["Revenue"].sum() * 100
share_quantity = data.groupby("product")["quantity"].sum() / data["quantity"].sum() * 100
print("\nShare of Revenue by Product (%):")
print(share_revenue)
print("\nShare of Quantity by Product (%):")
print(share_quantity)

# --- Visualization ---
plt.figure(figsize=(10,5))
rev_by_month.plot(kind="bar", color="skyblue")
plt.title("Revenue by Month")
plt.ylabel("Revenue ($)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
qty_by_month.plot(kind="bar", color="green")
plt.title("Quantity Sold by Month")
plt.ylabel("Units Sold")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart for revenue share
plt.figure(figsize=(7,7))
share_revenue.plot(kind="pie", autopct='%1.1f%%', startangle=90)
plt.title("Revenue Share by Product")
plt.ylabel("")
plt.show()
