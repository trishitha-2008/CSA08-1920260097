def stairs(n):
    if n <= 1:
        return 1

    return stairs(n-1) + stairs(n-2)

n = int(input("Enter number of stairs: "))
print("Ways:", stairs(n))
