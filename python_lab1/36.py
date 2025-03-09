m = [1, 2, 3, ["a", "b", "c"]]
n = m
m[0] = 8

print("m:", m)
print("n:", n)

m = [1, 2, 3, ["a", "b", "c"]]
n = m.copy()

print("m:", m)
print("n:", n)

m[3][1] = "ups"

print("m:", m)
print("n:", n)

m = [1, 2, 3, ["a", "b", "c"]]
n = m[:]
m[3][1] = "oops"

print("m:", m)
print("n:", n)

import copy

m = [1, 2, 3, ["a", "b", "c"]]
n = copy.deepcopy(m)
m[3][1] = "OMG"

print("m:", m)
print("n:", n)

