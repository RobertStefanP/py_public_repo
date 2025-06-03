"""A boxplot showing the distribution of the sales by segment.(Corporate, Consumer, Home)"""
import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
sales_by_segment = calculate.sales_by_segment()

sales_by_segment.plot(kind="box", figsize=(12, 6))
plt.xlabel("Segment(area)")
plt.ylabel("Sales")
plt.title("Sales distribution by clients")
plt.tight_layout()
plt.show()
