import matplotlib.pyplot as plt
import numpy as np
from data_process import Calculate



calculate = Calculate()
(mar_fem_abv_30, mar_fem_und_30, mar_male_abv_30, 
 mar_male_und_30) = calculate.age_martial_status()

age_group = ["Females", "Males"]

under_30 = [len(mar_fem_und_30), len(mar_male_und_30),]
above_30 = [len(mar_fem_abv_30), len(mar_male_abv_30)]

y = np.arange(len(age_group))
width = 0.3

plt.figure(figsize=(10, 6))
plt.barh(y + width / 2, above_30, height=width, color="blue", label="Above 30")
plt.barh(y - width / 2, under_30, height=width, color="skyblue", label="Under 30")

plt.title("Distribution of males and females marriages")
plt.yticks(y, age_group)
plt.ylabel("Age group")
plt.xlabel("People Count")
plt.tight_layout()
plt.legend()
plt.show()
