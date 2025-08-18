import matplotlib.pyplot as plt
import seaborn as sns  # для стильного графіка

# Задаємо стиль графіка
sns.set_style("darkgrid")

# Дані продажів
sales = [
    {"item": "Apple", "quantity": 10, "price": 2.5},
    {"item": "Banana", "quantity": 5, "price": 1.2},
    {"item": "Orange", "quantity": 8, "price": 1.8},
    {"item": "Mango", "quantity": 3, "price": 3.0},
]

# Порахуємо загальний дохід для кожного товару
for sale in sales:
    sale["total"] = sale["quantity"] * sale["price"]

# Загальний дохід всіх товарів
total_income = sum(sale["total"] for sale in sales)

# Виведемо дані у консоль
for sale in sales:
    print(f"{sale['item']}: Quantity={sale['quantity']}, Price={sale['price']}, Total={sale['total']}")

print(f"\nTotal income: {total_income}")

# Візуалізація графіка
items = [sale["item"] for sale in sales]
totals = [sale["total"] for sale in sales]

# Використовуємо палітру Seaborn
colors = sns.color_palette("pastel", len(items))

fig, ax = plt.subplots(figsize=(8, 5))  # розмір графіка
bars = ax.bar(items, totals, color=colors)

# Додаємо підписи значень над стовпчиками
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # зсув над стовпчиком
                textcoords="offset points",
                ha='center', va='bottom')

ax.set_title("Total Income per Item", fontsize=14, fontweight='bold')
ax.set_xlabel("Item", fontsize=12)
ax.set_ylabel("Total Income ($)", fontsize=12)

plt.show()
