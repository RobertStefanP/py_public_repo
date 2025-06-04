"""A plot showing the sales evolution by category from the start of recordings."""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
monthly_sales= calculate.category_monthly_sales()

monthly_sales.plot(figsize=(12, 6), linewidth=2)
plt.xlabel("Monthly Evolution")
plt.ylabel("Total Sales")
plt.title("Monthly sales evolution")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend(title="Category")
plt.show()
