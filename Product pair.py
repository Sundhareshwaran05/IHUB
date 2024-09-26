def product_pair(input1, input2):
    x = set()
    input2.sort()
    for i in range (input1):
        for j in range (i+1, input1):
            if (input2[i]*input2[j])%3 == 0:
                x.add((input2[i],input2[j]))
    return len(x)

input1 = int(input())
input2 = list(map(int,input().split()))
print(product_pair(input1,input2))