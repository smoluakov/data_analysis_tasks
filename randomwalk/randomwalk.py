import matplotlib.pyplot as plt
from random import choice


class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        # вычисляет все точки блуждания
        # шаги генерируються до достижения нужной длинны
        while len(self.x_values) < self.num_points:
            # определения направления и длинны перемещения
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # отклонения нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # вычиление следующих значений x и y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


while True:

    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=10)
    # выделим первую и последнюю точку
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # удаление пустого места вокург графика
    plt.figure(dpi=128, figsize=(10, 6))


    keep_running = input('Make another walk? (y/n):')

    if keep_running == 'n':
        break

plt.show()