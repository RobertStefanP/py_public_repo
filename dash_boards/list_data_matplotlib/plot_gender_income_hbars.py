import matplotlib.pyplot as plt
from data_process import Calculate



calculate = Calculate()
(male_inc_und_30, male_inc_abv_30, female_inc_und_30, 
    female_inc_abv_30) = calculate.gender_income()

values = [
    len(male_inc_abv_30),
    len(female_inc_abv_30),
    len(male_inc_und_30),
    len(female_inc_und_30),
]

labels = [
    "Males above 30",
    "Females above 30",
    "Males under 30",
    "Feamles under 30",
]

colors = ["blue", "green"] * 2

plt.figure(figsize=(10, 6))
plt.barh(labels, values, color=colors)
plt.xlabel("Total count")
plt.title("Comparison by age groups, earning > 50K or < 50K", fontsize=16)
plt.tight_layout()
plt.show()
