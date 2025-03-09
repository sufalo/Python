import random

l1 = [random.randint(-3, 21) for _ in range(10)]

l2 = [a for a in l1 if a < 13]

print(l1)
print(l2)