def magicalnumber(input1):
    c = 0 
    for i in range(1,input1+1):
        temp = list(map(int, bin(i)[2:]))
        s = sum(temp) + len(temp) 
        if s%2 != 0:
            c += 1
    return c

input1 = int(input())
print(magicalnumber(input1))