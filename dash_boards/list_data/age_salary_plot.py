import matplotlib.pyplot as plt
from collections import Counter


# Converting the data in a list of elements
with open("adult.data") as file:
    lines = file.readlines()
data = [line.strip().split(", ") for line in lines]

# Creating empty lists 
ages = []
salaries = []
under_50k_ages = []
over_50k_ages = []

for person in data:
    if len(person) < 15:
        continue    
    age = int(person[0])
    income = person[14]    
    if income == "<=50K":
        under_50k_ages.append(age)
    else:
        over_50k_ages.append(age)
        
    ages.append(age)
    salaries.append(income) 

avg_under = sum(under_50k_ages) / len(under_50k_ages)
avg_over = sum(over_50k_ages) / len(over_50k_ages)

# Return dictionary-like object holding the number of each salarie category
counts = Counter(salaries) 
labels = list(counts.keys()) # Give names to the labels onn the pie
values = list(counts.values()) # Give the size of each slice of pie

# Creating the figure, with window size, sliced piece, and the percentage inside
plt.figure(figsize=(8, 6), dpi=100)
explode = [0.02, 0]
plt.pie(values, labels=labels,
        autopct="%1.2f%%",
        explode=explode,
        )  
# Manually placing ages above percentage on the pie
plt.text(-0.47, 0.5, f"Under {avg_under:.0f}", ha='center')
plt.text(0.43, -0.35, f"Over {avg_over:.0f}", ha='center')

# Creating a legend containing the income based on avg age
plt.legend([f"<=50K: avg age {avg_under:.1f}", f">50K: avg age {avg_over:.1f}"],
           loc="lower left",
           bbox_to_anchor=(-0.4, 0.0))
# Title of the plot
plt.title("Income Distribution")
plt.show()
