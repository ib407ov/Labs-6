n = int(input('How many numbers = '))
x = int(input('x = '))
y = int(input('y = '))

import random
A = [x, x, y]
print(A)

if n < 3:
    print('Error')
    exit(0)

for i in range(3, n):
    A.append(A[i - 2] + (A[i - 1] / (2 ** (i - 1))) * A[i - 3])

print('\n{0}' .format(A))