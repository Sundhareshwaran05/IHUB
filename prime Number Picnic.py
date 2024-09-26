def primesum(input1):
    def prime(n):
        for i in  range (2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    out = 0
    for i in range (input1+1):
        if i not in [0,1] and prime(i):
            out += i
    return out

input1 = int(input())
print(primesum(input1))