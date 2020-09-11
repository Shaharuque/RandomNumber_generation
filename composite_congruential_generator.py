import math
import numpy as np
import matplotlib.pyplot as plt
n = ['100', '120', '160']
z1 = [12, 7]
z2 = [3, 5]
z3 = [2, 7]
u1 = []
u2 = []
u3 = []
u_abs = []  # full value
u_abs2 = []  # cut-off value
u = []  # Final random value using witchman/hill algo
temp = []
temp1 = []
temp2 = []
for j in range(3):

    for i in range(2, int(n[j])):
        new_z = (13 * z1[i - 1] + 11 * z1[i - 2] + 3) % 16
        new_u = new_z / 16
        z1.append(new_z)
        u1.append(new_u)

        new_z1 = (12 * z2[i - 1] ** 2 + 13 * z2[i - 2]) % 17
        new_u1 = new_z1 / 17
        z2.append(new_z1)
        u2.append(new_u1)

        new_z2 = (z3[i - 1] ** 3 + z3[i - 2] ** 2) % 15
        new_u2 = new_z2 / 15
        z3.append(new_z2)
        u3.append(new_u2)

    print("u1, u2, u3 for trail no.:", int(n[j]))
    print(u1)
    print(u2)
    print(u3)
    print("random numbers for trail:", int(n[j]))
    print(z1)
    print(z2)
    print(z3)

for j in range(3):
    for i in range(0, (int(n[j]) - 2)):
        u_new = u1[i] + u2[i] + u3[i]
        u_abs.append(u_new)
        u_new1 = int(u1[i] + u2[i] + u3[i])
        u_abs2.append(u_new1)
        final = u_abs[i] - u_abs2[i]
        u.append(final)

    print("final u:", int(n[j]))
    print(u)

for i in range(3):
    for j in range(0, len(z1)):
        temp.append(str(j))
    plt.bar(temp, z1)
    plt.show()

    for j in range(0, len(z2)):
        temp1.append(str(j))
    plt.bar(temp1, z2)
    plt.show()

    for j in range(0, len(z3)):
        temp2.append(str(j))
    plt.bar(temp2, z3)
    plt.show()