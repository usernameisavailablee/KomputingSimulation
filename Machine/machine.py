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


