input1 = input()
input2 = int(input())
input3 = input()
a = list(input1)
b = []
for i in a:
    if input3 == i:
        b.append(i)
    else :
        continue
print(len(b))