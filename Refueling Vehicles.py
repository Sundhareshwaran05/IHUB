def refuelingVehicles(input1, input2, input3):
    count = 0 
    x = input1
    fuel = input2
    arr = input3
    arr.sort(reverse = True)
    rem = 0
    i = 0
    while i < len(arr):
        ele = arr[i]
        if ele + rem >= x:
            rem - (ele+rem) - x
            if rem < 0:
                rem = 0
            i += 1
        else:
            rem += x
            count += 1
    return count

input1 = int(input())
input2 = int(input())
input3 = list(map(int,input().split()))