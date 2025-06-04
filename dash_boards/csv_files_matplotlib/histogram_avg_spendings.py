"""Histogram showing the average customer spendings."""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
avg_sales = calculate.customer_avg_spending()

bins = list(range(0, 1800, 50))
plt.figure(figsize=(12, 6))
plt.hist(avg_sales, bins=bins, edgecolor="black", linewidth=0.1, align="mid")
plt.xlabel("Total customer spendings")
plt.xticks(bins, rotation=45)
plt.xlim(0, 1800)
plt.ylabel("Amount of customers")
plt.title("Average customer spendings")
plt.show()
