import pandas as pd


class Calculate():
    def __init__(self):
        self.data = pd.read_csv("superstore.csv")

    def get_sales(self):
        """Obtaining average sales in range prices."""
        return self.data["Sales"]

    def customer_avg_spending(self):
        """Returning the average sales made by customers."""  
        total_sales = self.data.groupby("Customer ID")["Sales"].sum() 
        order_counts = self.data.groupby("Customer ID")["Sales"].count() 
        avg_sales = total_sales / order_counts        
        return avg_sales
    
    def sales_by_state(self):
        """Returns the average sales per State."""
        city_sales = self.data.groupby("State")["Sales"].sum()
        sales_total = self.data.groupby("State")["Sales"].count()       
        return city_sales / sales_total
     
    def sales_evolution(self):
        """Returns monthly sales evolution."""
        # Convert "Order Date" to datetime
        self.data["Order Date"] = pd.to_datetime(self.data["Order Date"], dayfirst=True)
        
        # Create a new column with just Year-Month 
        self.data["YearMonth"] = self.data["Order Date"].dt.to_period("M")
        
        # Group by YearMonth and sum the sales
        monthly_sales = self.data.groupby("YearMonth")["Sales"].sum()
        
        # Convert Period to string
        monthly_sales.index = monthly_sales.index.astype(str)
        return monthly_sales
    
    def weekly_sales(self):
        """Returns weekly sales evolution."""
        self.data["Order Date"] = pd.to_datetime(self.data["Order Date"], dayfirst=True)
        self.data["YearWeek"] = self.data["Order Date"].dt.to_period("W").apply(lambda p: p.start_time.date())
        weekly_sales = self.data.groupby("YearWeek")["Sales"].sum()
        weekly_sales.index = weekly_sales.index.astype(str)
        return weekly_sales
        
    def sales_by_category(self):
        """Returns monthly sales from the beggining by category."""
        self.data["Order Date"] = pd.to_datetime(self.data["Order Date"], dayfirst=True)
        self.data["YearMonth"] = self.data["Order Date"].dt.to_period("M")  
        
        grouped = self.data.groupby(["YearMonth", "Category"])["Sales"].sum()   
        grouped = grouped.unstack() # Columns = categories, index = months
        grouped.index = grouped.index.astype(str)    
        return grouped
    
    def sales_by_region(self):
        """Returns all time sales by region."""
        self.data["Order Date"] = pd.to_datetime(self.data["Order Date"], dayfirst=True)
        self.data["YearMonth"] = self.data["Order Date"].dt.to_period("M")
        
        sales_by_region = self.data.groupby(["YearMonth", "Region"])["Sales"].sum()
        sales_by_region = sales_by_region.unstack()
        sales_by_region.index = sales_by_region.index.astype(str)
        return sales_by_region
        
    def sales_by_segment(self):
        """Returns data to calculate sales by segment."""
        self.data["Order Date"] = pd.to_datetime(self.data["Order Date"], dayfirst=True)
        self.data["YearMonth"] = self.data["Order Date"].dt.to_period("M")
        sales_by_segment = self.data.groupby(["YearMonth", "Segment"])["Sales"].sum()
        sales_by_segment = sales_by_segment.unstack()
        sales_by_segment.index = sales_by_segment.index.astype(str)
        return sales_by_segment
    
if __name__ == "__main__":
    calculate = Calculate()
