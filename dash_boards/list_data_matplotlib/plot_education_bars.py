import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
(doctorate, prof_school, masters, bachelors, some_college, hs_grad, 
others_9th_12th, others_1st_8th, preschool) = calculate.degrees()

values = [
    len(doctorate), 
    len(prof_school), 
    len(masters), 
    len(bachelors), 
    len(some_college), 
    len(hs_grad),
    len(others_9th_12th),
    len(others_1st_8th),
    len(preschool),
]

labels = [
    "Doctorate", 
    "Prof-school", 
    "Masters", 
    "Bachelors", 
    "Some-college", 
    "HS-grad", 
    "9th to 12th",
    "1st to 8th",
    "Preschool"
]

# Advanced concept suggested by AI to sort the bars in descended order
labels, values = zip(*sorted(zip(labels, values), key=lambda x: x[1], reverse=True))

plt.figure(figsize=(10, 6))
plt.bar(labels, values)
plt.title("Education Level Distribution")
plt.xlabel("Degree")
plt.ylabel("Number of People")
plt.tight_layout()
plt.show()
