import matplotlib.pyplot as plt
import numpy as np
from data_process import Calculate


calculate = Calculate()
(mar_pers_20_30, single_20_30, mar_pers_30_40, single_30_40, 
mar_pers_40_50, single_40_50, mar_pers_50_60, single_50_60,     
mar_pers_60_70, single_60_70, mar_pers_70_80, single_70_80, 
mar_pers_80_90, single_80_90) = calculate.age_mariage_distribution()

age_groups = ["20-30", "30-40", "40-50", "50-60", "60-70", "70-80", "80-90"]

married = [
    len(mar_pers_20_30),
    len(mar_pers_30_40),
    len(mar_pers_40_50),
    len(mar_pers_50_60),
    len(mar_pers_60_70),
    len(mar_pers_70_80),
    len(mar_pers_80_90),
]

single = [
    len(single_20_30),
    len(single_30_40),
    len(single_40_50),
    len(single_50_60),
    len(single_60_70),
    len(single_70_80),
    len(single_80_90), 
]
# Creates positions based on the nr of elements in age_group list
x = np.arange(len(age_groups))
width = 0.45

plt.figure(figsize=(10, 6))

plt.bar(x - width/2, married, width, label="Married", color="green")
plt.bar(x + width/2, single, width, label="Single", color="brown")

plt.title("Married People by Age Group", fontsize=18)
plt.xlabel("Age Group", fontsize=12)
plt.ylabel("Number People", fontsize=12)
plt.xticks(x, age_groups, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
