"""Histogram showing the number of orders per year."""
import matplotlib.pyplot as plt
from data_process_csv import Calculate


calculate = Calculate()
sales = calculate.customer_sales()


