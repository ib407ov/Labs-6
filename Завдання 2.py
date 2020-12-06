n = int(input('line lenghts: '))

if n < 3:
    print('Error')
    exit(0)

A = []
A = [int(input('write {0} numer : '.format(i))) for i in range(3)]

for i in range(3, n):
    A.append(A[i - 2] + (A[i - 1] / (2 ** (i - 1))) * A[i - 3])

print('\n{0}' .format(A))