def bugfix(input1):
    x = str(input1).replace('0','5')
    return int(x)

input1 = int(input())
print(bugfix(input1))