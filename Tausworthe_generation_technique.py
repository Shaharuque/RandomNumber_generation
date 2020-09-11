import math
import matplotlib.pyplot as plt
b = [1, 1, 1, 1, 1]
r = 3
q = 5
l = 4
a = 2 ** l
u = []
val = []
temp = []
for i in range(5, 1000):
    new_b = b[i - r] ^ b[i - q]
    b.append(new_b)
print("bits:")
print(b)

for i in range(0, 1000, l):
    b_segment = b[i:i + l]  # seperation 4 bits respectively
    # print(b_segment)
    str1 = ""
    for j in b_segment:
        str1 = str1 + str(j)  # each b_segment converts in to 1 string
    # print(str1)
    w_i = int(str1, 2)  # binary to decimal convertion
    # print(w_i)
    u.append(w_i / a)
    val.append(w_i)
print(val)
print(u)  # random numbers between 0 to 1
# print(len(u))
# print(len(val))
for i in range(len(u)):
    temp.append(str(i))

plt.bar(temp, u)
plt.show()