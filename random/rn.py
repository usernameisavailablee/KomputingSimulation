import random
import numpy as np
import matplotlib.pyplot as plt


def square_meth(digit,amount_iterations):
  if amount_iterations > 0 and digit > 999 and digit < 10000:
    random_list = []
    for i in range(0,amount_iterations):
      random_Digit = (digit ** 2) % 1000000 // 100
      random_list.append(round(float(random_Digit / 10000), 4))
      digit = random_Digit
    return random_list
  else:
    return 0

def mult_meth(factor, core, amount_iterations):
  if amount_iterations > 0 and factor > 999 and factor < 10000:
    random_list = []
    for i in range (0,amount_iterations):
      random_Digit = (factor * core) % 1000000 // 100
      random_list.append(round(float(random_Digit / 10000), 4))
      factor = (factor * core) % 10000
    return random_list
  else:
    return 0

def MCM(constMult, constDiv, digit, m):
  if m > 0 and 999 < digit < 10000 and 999 < constDiv < 10000 and 999 < constMult < 10000:
    random_list = []
    for i in range(0, m):
      digit = (digit * constMult) % constDiv
      random_list.append(round(digit / 10000, 4))
    return random_list
  else:
    return 0




def plot(list_rDigit,number_of_method):

#, rwidth=0.85


  n, bins, patches = plt.hist(list_rDigit,  color='#0504aa',alpha=0.70, rwidth=1)
  # n, bins, patches = plt.hist(list_rDigit, xRange, color='#0504aa', alpha=0.7, rwidth=0.85)
  if number_of_method == 1:
    plt.title("Метод средних квадратов")

  if number_of_method == 2:
    plt.title("Метод произведений")

  if number_of_method == 3:
    plt.title("Мультипликативный конгруэнтный метод")

  plt.xlabel('Значения')
  plt.ylabel('Количество')
  plt.grid(False)
  plt.show()

if __name__ == '__main__':
  print("\nВведите необходимое количество значений:")
  N = int(input())
  list_A = square_meth(7153, N)
  plot(list_A,1)
  list_A = mult_meth(5167,3729,N)
  plot(list_A,2)
  list_A = MCM(1357,9689,1357,N)
  plot(list_A,3)
