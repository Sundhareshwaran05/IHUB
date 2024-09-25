input1 = int(input())
input2 = list(map(int,input().split()))
max_pr = 0
arr = input2
out = []
for i in range (input1-1):
    for j in range(i+1,input1):
        if arr[i]+arr[j] == 18:
            temp = arr[i]*arr[j]
            if temp >= max_pr:
                max_pr = temp
                out = sorted([arr[i],arr[j]],reverse = True)
print(out)