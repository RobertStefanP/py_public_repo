"""Counts the average sales per state."""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
# Returns a panda series
avg_state_sales = calculate.sales_by_state().sort_values(ascending=False) 
states = avg_state_sales.index
value = avg_state_sales.to_numpy() # convert to numpy 


plt.figure(figsize=(12, 6))
plt.bar(states, value)
plt.xlabel("State name")
plt.ylabel("Average Sales")
plt.title("Average sales per State", fontsize=18)
plt.xlim(-0.5)
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()
