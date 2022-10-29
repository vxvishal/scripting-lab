import numpy as np

l1 = [1, 2, 3, 4, 5]
l2 = [[6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
print(l2[1][2])

a1 = np.array(l1)
print(a1)

a2 = np.array(l2)
print(a2)

print(a2.shape)

l3 = ["12", "13", 14]
a3 = np.array(l3)
print(a3)

a4 = np.ones((5,8), dtype=int)
print(a4)

a5 = np.zeros((5,8), dtype=int)
print(a5)

a6 = np.arrange(20,30)
print(a6)