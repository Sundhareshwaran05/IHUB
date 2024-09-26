def financial_dataset(input1, input2):
    d = 0
    for i in input1:
        if i < 0:
            d += 1
    return d

input1 = list(map(int, input().split()))
input2 = int(input())
print(financial_dataset(input1, input2))