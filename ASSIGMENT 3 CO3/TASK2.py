import copy

location = (13.08, 80.27)
print("Location:", location)

bad = [[0] * 3] * 2
bad[0][0] = 5
print("Bad grid:", bad)

good = [[0 for j in range(3)] for i in range(2)]
good[0][0] = 5
print("Good grid:", good)

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0][0] = 100

print("Original:", a)
print("Copied:", b)
