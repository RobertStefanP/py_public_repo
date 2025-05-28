from random import choice
import matplotlib.pyplot as plt

class RandomWalk:   
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = choice([1, -1, 0])
            y_step = choice([1, -1, 0])
            if x_step == 0 and y_step == 0:
                continue

            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

rand = RandomWalk()
rand.fill_walk()

plt.figure(figsize=(10, 6))
plt.plot(rand.x_values, rand.y_values, linewidth=1)
plt.title("Random walk Path")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
