input1 =  list(map(int,input().split()))
input2 = int(input())
x = input1[::-1]
print(sum([x[i] for i in range (input2) if i%2 == 0]))