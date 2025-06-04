"""A boxplot showing the sales based on region."""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
sales_by_region = calculate.sales_by_region()

sales_by_region.plot(kind="box", figsize=(12, 6))
plt.xlabel("Region")
plt.ylabel("Monthly sales")
plt.title("Sales based on region")
plt.tight_layout()
plt.show()
