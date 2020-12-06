n = int(input("Вкажіть вимір вектора: \n"))

x1 = [float(input("Задайте {0}-координату вектора: ".format(i+1))) for i in range(n)]

x2 = [float(input("Задайте {0}-координату вектора: ".format(i+1))) for i in range(n)]

print("\nVektor 1= {0}\nVektor 2= {1}" .format(x1, x2))

Summ = []
for i in range(n):
    Summ.append(x1[i]+x2[i])



print("Summ vektors = ",Summ)7