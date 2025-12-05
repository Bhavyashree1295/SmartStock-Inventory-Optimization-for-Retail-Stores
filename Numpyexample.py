#  Import NumPy
import numpy as np

#  Create NumPy arrays
quantity = np.array([50, 10, 50, 30, 70, 60])
price = np.array([55, 15, 45, 5, 80, 45])

#  Perform calculations
# Calculate total revenue for each item
revenue = quantity * price

# Calculate average price
avg_price = np.mean(price)

# Filter items with quantity > 40
high_quantity = quantity[quantity > 40]

# Display results
print("Revenue per item:", revenue)
print("Average price:", avg_price)
print("Items with quantity > 40:", high_quantity)
