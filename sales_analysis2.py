import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("sales.csv")

# Add new column "total" (revenue = quantity * price)
df["total"] = df["quantity"] * df["price"]

print("\nFirst 5 rows of data:")
print(df.head())

# 2. General statistics
print("\nGeneral statistics:")
print(df.describe())

# 3. Total sales by product
sales_by_product = df.groupby("product")["total"].sum().sort_values(ascending=False)
print("\nTotal sales by product:")
print(sales_by_product)

# 4. Total sales by date
sales_by_date = df.groupby("date")["total"].sum()
print("\nTotal sales by date:")
print(sales_by_date)

# 5. Most profitable product
top_product = sales_by_product.idxmax()
print(f"\nMost profitable product: {top_product} (${sales_by_product.max():.2f})")

# 6. Visualizations
plt.figure(figsize=(12, 6))

# --- Chart 1: Sales by product ---
plt.subplot(1, 2, 1)
sales_by_product.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Total Sales by Product")
plt.ylabel("Revenue ($)")
plt.xlabel("Product")
plt.xticks(rotation=45)

# --- Chart 2: Sales trend by date ---
plt.subplot(1, 2, 2)
sales_by_date.plot(kind="line", marker="o", color="green")
plt.title("Sales Trend by Date")
plt.ylabel("Revenue ($)")
plt.xlabel("Date")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
