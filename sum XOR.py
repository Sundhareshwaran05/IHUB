input1 = int(input())
input2 = list(map(int,input().split()))
o = 0 
e = 0
arr = input2
for i in range(input1):
    if i % 2 == 0:
        e = e^arr[i]
    else:
        o += arr[i]
print(o-e)