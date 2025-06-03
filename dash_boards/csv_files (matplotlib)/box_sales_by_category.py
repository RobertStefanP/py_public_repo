"""A boxplot showing the sales evolution by category from the start of recordings."""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
sales_by_category = calculate.sales_by_category()

sales_by_category.plot(kind="box", figsize=(12, 6))
plt.xlabel("Category")
plt.ylabel("Monthly Sales")
plt.title("Sales distribution per category")
plt.tight_layout()
plt.show()
