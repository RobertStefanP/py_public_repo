import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
(worked_hours_males, worked_hours_males_abv_40, 
 worked_hours_males_undr_40, worked_hours_females, 
 worked_hours_females_abv_40, worked_hours_females_undr_40) = calculate.hours_worked()

values = [
    len(worked_hours_males),
    len(worked_hours_females),
    len(worked_hours_males_undr_40),
    len(worked_hours_females_undr_40),
    len(worked_hours_males_abv_40),
    len(worked_hours_females_abv_40),
]

labels = [
    "Males",
    "Females",
    "Males under 40",
    "Females under 40",
    "Males above 40",
    "Females above 40",
]

colors = ["blue", "red"] * 3

plt.figure(figsize=(10, 6))
# Adding legend
plt.bar(labels[0], values[0], color="blue", label="Males")
plt.bar(labels[1], values[1], color="red", label="Females")

plt.bar(labels, values, color=colors)
plt.title("Worked hours by Age group and gender", fontsize=16)
plt.xlabel("Worked hours by group")
plt.xticks(rotation=45)
plt.ylabel("Number of People")
plt.legend(loc="upper center", bbox_to_anchor=(0.8, 0.9))
plt.tight_layout()
plt.show()
