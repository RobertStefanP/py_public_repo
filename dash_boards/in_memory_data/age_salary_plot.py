import matplotlib.pyplot as plt
from collections import Counter


with open("adult.data") as file:
    lines = file.readlines()
data = [line.strip().split(", ") for line in lines]

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

counts = Counter(salaries) # Return dictionary-like object 
labels = list(counts.keys()) # 
values = list(counts.values())

plt.figure()
plt.pie(values, labels=labels, autopct="%1.1f%%")      
plt.title("Income Distribution")
plt.legend([f"<=50K: avg age {avg_under:.1f}", f">50K: avg age {avg_over:.1f}"], 
           loc="lower left",
           bbox_to_anchor=(-0.3, 0.0))
plt.show()
      
    
