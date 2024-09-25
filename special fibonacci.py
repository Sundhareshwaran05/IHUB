input1 = int(input())
out = [0]*(input1+1)
out[0] = 1
out[1] = 1
for i in range(2,input1+1):
    out[i] = (out[i-1]*out[i-1]+out[i-2]*out[i-2])%47
print(out[input1])