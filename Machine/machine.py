import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from prettytable import PrettyTable

# Экспоненциальное распределение
intervals = lambda: np.random.exponential(scale=0.18)  # Интервалы работы
# Нормальное распределение
task_execution = lambda: np.random.normal(loc=0.5, scale=0.1)  # Выполнения детали
repair_cooldown = lambda: np.random.normal(loc=20, scale=2)  # кд на починку
# Равномерное распределение
repair = lambda: np.random.uniform(low=0.1, high=0.5)  # Время починки
setting_up = lambda: np.random.uniform(low=0.2, high=0.5)  # Наладка перед выполнением задания


def plot(a, b, c):
    plt.plot(a, color='red', label='Все время станка')
    plt.plot(b, color='orange', label='Работа')
    plt.plot(c, color='green', label='Починка, отладка и интервалы')

    plt.xlabel('Количество сделанных деталей')
    plt.ylabel('Время работы станка')

    plt.title('График работы станка')

    plt.legend()
    plt.show()


def table_draw(td, th, columns):
    table = PrettyTable(th)
    while td:
        table.add_row(td[:columns])
        td = td[columns:]

    print("{}".format(table))


def machine_work(details=500):
    cooldown, current, counter = repair_cooldown(), 0, 0
    time_all, time_work, time_chill, time_repair = 0, 0, 0, 0
    in_progress = deque([i for i in range(details + 1)])

    while len(in_progress) != 0:
        set_up = setting_up()
        val = intervals()
        task = task_execution()
        cooldown -= current

        if cooldown <= 0:
            cooldown = repair_cooldown()
            work = repair()

            time_chill += work
            time_all += work
            time_repair += work
            counter += 1
            current = 0
            in_progress.rotate(-1)

        else:
            time_work += set_up + task
            time_chill += val
            time_all += set_up + val + task
            current = round(set_up + val + task, 2)

            in_progress.pop()

    return round(time_all, 2), round(time_work, 2), round(time_chill, 2), counter, round(time_repair, 2)


if __name__ == '__main__':
    i = int(input("Сколько раз выполнить симуляцию: "))
    td = []

    for _ in range(i):
        t = machine_work()
        td.extend([
            t[0],
            t[1],
            t[2],
            t[4],  # Изменен индекс для учета времени затраченного на ремонт
            t[3]
        ])

    # Вывод результатов на консоль
    table_draw(td, ["Общее время", "Время работы", "Время простоя", "Время ремонта", "Кол-во поломок"], 5)

    # Вывод результатов в текстовый файл
    with open("results.txt", "w") as file:
        file.write("Результаты работы станка\n\n")
        table_draw(td, ["Общее время", "Время работы", "Время простоя", "Время ремонта", "Кол-во поломок"], 5)

        file.write("\n")
        file.write(f"Общее время работы станка: {sum(td[::5]):.2f} ч\n")
        file.write(f"Общее время выполнения всех деталей: {sum(td[1::5]):.2f} ч\n")
        file.write(f"Общее время простоя станка: {sum(td[2::5]):.2f} ч\n")
        file.write(f"Общее время затраченное на ремонт станка: {sum(td[3::5]):.2f} ч\n")
        file.write(f"Количество поломок: {sum(td[4::5])}\n")
