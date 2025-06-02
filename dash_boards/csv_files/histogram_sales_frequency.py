"""A histogram showing how frequently sales occur whithin specific price intervals (0 - 1000)."""
import matplotlib.pyplot as plt
from data_process import Calculate


calc = Calculate()
sales = calc.get_sales()
bins = list(range(0, 1001, 12))

plt.figure(figsize=(12, 6))
plt.hist(sales, bins=bins)
plt.xlabel("Sale Amount")
plt.xticks(range(0, 1001, 25), rotation=45)
plt.xlim(0, 1000) # sets the visible range value on x axis for product prices
plt.ylabel("Frequency")
plt.title("Sales frequencie based on products price", fontsize=16)
plt.show()
