"""A plot showing sales income over the months."""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
sales_data = calculate.sales_evolution()

plt.figure(figsize=(12, 6))
plt.plot(sales_data, linewidth=3)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Evolution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
