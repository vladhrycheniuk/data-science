import matplotlib.pyplot as plt

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

# Виведемо дані
for sale in sales:
    print(f"{sale['item']}: Quantity={sale['quantity']}, Price={sale['price']}, Total={sale['total']}")

print(f"\nTotal income: {total_income}")

# Візуалізація графіка
items = [sale["item"] for sale in sales]
totals = [sale["total"] for sale in sales]

plt.bar(items, totals, color="skyblue")
plt.title("Total Income per Item")
plt.xlabel("Item")
plt.ylabel("Total Income")
plt.show()
