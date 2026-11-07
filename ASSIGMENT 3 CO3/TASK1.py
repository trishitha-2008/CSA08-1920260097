rainfall = [10, 20, 0, 15, 30, 5, 0, 25, 40, 10]

print("Weekly total:", sum(rainfall[:7]))
print("Maximum:", max(rainfall))
print("Minimum:", min(rainfall))

for i in range(len(rainfall) - 6):
    print("Average:", sum(rainfall[i:i+7]) / 7)

print("Dry days:", [i+1 for i, x in enumerate(rainfall) if x == 0])
