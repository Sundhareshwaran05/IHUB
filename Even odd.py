input1 = list(map(int,input().split()))
input2 = int(input())
out = ""
for i in input1:
    if i % 2 == 0:
        out += "Even"
    else:
        out += "Odd"
print(out)