import matplotlib.pyplot as plt
from data_process import Calculate


calculate = Calculate()
males, females = calculate.genders_total()

#labels = ["Males", "Females"]
values = [len(males), len(females)]

plt.figure(figsize=(10, 6))
explode = [0.05, 0]

plt.pie(values, #labels=labels, 
        explode=explode,
        autopct="%1.1f%%",
        shadow=True,
        startangle=270)

plt.text(-0.53, -0.25, f"Females ", ha='center')
plt.text(0.54, 0.4, f"Males ", ha='center')

plt.title("Gender Dsistribution in Censur Data")
plt.tight_layout()
plt.show()
