def candies(input1,input2,input3):
    y = [x for x in input2 if x % 5 !=0]
    if len(y) == 0:
        return input1
    y.sort()
    d = input1 - len(y)
    i = 0
    while i < len(y) and d > 0:
        input3 -= y[i]
        if input3 < 0:
            break
        d += 1
        i += 1
    return d

input1 = int(input())
input2 = list(map(int,input().split))
input3 = int(input())
print(candies(input1,input2,input3))