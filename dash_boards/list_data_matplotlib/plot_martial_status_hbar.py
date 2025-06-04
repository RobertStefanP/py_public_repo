import matplotlib.pyplot as plt
import numpy as np
from data_process import Calculate



calculate = Calculate()
singles_males, mar_males, singles_females, mar_females = calculate.martial_status()

gender_groups = ["Females", "Males"]

females = [len(singles_females), len(mar_females)]
males = [len(singles_males), len(mar_males)]

# Creates positions based on the nr of elements in gender_groups list
y = np.arange(len(gender_groups))
width = 0.25

plt.figure(figsize=(10, 6))
# Adding legend
plt.barh(y - width / 2, females, height=width, color="green", label="Single")
plt.barh(y + width / 2, males, height=width, color="red", label="Married")

plt.yticks(y, gender_groups)
plt.title("Maried vs Singles distribution", fontsize=14)
plt.ylabel("Gender")
plt.xlabel("Number Count")
plt.tight_layout()
plt.legend()
plt.show()
