n = int(input("Введіть кількість елементів масиву: "))

import random

A = [random.randint(0, 100) for i in range(n)]

print("Masiv:",A)

new = sorted(A,reverse=False)

print("From LOW ti HIGHT:",new)