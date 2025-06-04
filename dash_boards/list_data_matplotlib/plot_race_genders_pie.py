import matplotlib.pyplot as plt
from data_process import Calculate



calculate = Calculate()
white_males, white_females, black_males, black_females = calculate.race_genders()

values = [
    len(white_males),
    len(white_females),
    len(black_males),
    len(black_females),
]

labels = [
    "White Males",
    "White Females",
    "Black Males",
    "Black Females",
]

colors = ["blue", "skyblue", "peru", "burlywood"]
plt.figure(figsize=(10, 6))

plt.pie(values, labels=labels, colors=colors)
plt.title("Plot showing race distribution")
plt.tight_layout()
plt.show()
