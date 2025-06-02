"""A plot showing the weekly evolution of the sales."""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
weekly_sales = calculate.weekly_sales()

plt.figure(figsize=(12, 6))
plt.plot(weekly_sales, linewidth=2)
plt.xlabel("Weekly evolution")
plt.ylabel("Total Sales")
plt.title("Last years weekly sales evolution")
plt.xticks(ticks=range(0, len(weekly_sales), 4), 
           labels=weekly_sales.index.to_list()[::4], 
           rotation=45)
plt.tight_layout()
plt.show()
