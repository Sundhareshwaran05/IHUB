def canopy_area(input1):
    a = 3.14 * (input1**2)
    if a - int(a) > 0.5:
        return int(a) + 1
    else:
        return int(a)

input1 = int(input())
print(canopy_area(input1))