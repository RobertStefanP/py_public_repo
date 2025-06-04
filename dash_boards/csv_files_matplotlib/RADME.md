# Plotting from CSV Files using Matplotlib

This folder contains data visualizations created from a CSV file 
(Superstore dataset). All plots are generated using the **Matplotlib** library, 
with data processed using **Pandas**.

## Technologies
- Python 3
- Pandas
- Matplotlib

## Strategy
- A `Calculate` class loads and processes the CSV data.
- Each plot calls a specific method that returns the required data.
- Methods use Pandas functions like `groupby()`, `sum()`, `mean()`, 
  and `to_period()` to organize data by month, category, region, segment, etc.

## Plot Types
- Histograms (distribution of sales, customer spending)
- Line plots (sales evolution over months or weeks)
- Box plots (sales variation by region, category, segment)
- Bar plots (average sales per state or category)

## Purpose
This folder helps practice real-world data manipulation and visualization by:
- Grouping and analyzing data using Pandas
- Displaying trends, comparisons, and distributions with Matplotlib
