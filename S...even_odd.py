def even_odd(arr, n):
    res = []
    for i in range(min(n, len(arr))):
        if arr[i] % 2 == 0:
            res.append('even')
        else:
            res.append('odd')
    return ' '.join(res)
input1 = list(map(int,input().split()))
input2 = int(input())
print(even_odd(input1, input2))  