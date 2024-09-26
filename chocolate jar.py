def chocolate_jar(input1,input2):
    arr = input1
    c = 0
    for i in arr:
        if i == 0:
            continue
        if i <=3:
            c += 1
        else:
            if i % 3 == 0:
                c += (i//3)
            else:
                c += (i//3) + 1
    return c

input1 = list(map(int,input().split()))
input2 = int(input())
print(chocolate_jar(input1,input2))