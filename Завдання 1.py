n = int(input('line lenghts: '))

import random
A = [random.randint(0, 100)   for i in range(n)]
print('{0}'.format(A))

mean = 0
for i in range(n):
    mean += A[i]

mean = mean / n
print('\nAvarage : {0}' .format(mean))