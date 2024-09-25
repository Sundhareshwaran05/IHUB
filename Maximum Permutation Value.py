input1 = input().split()
input2 = int(input())
def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)
val = 0
for word in input1:
    out = ""
    for char in word.lower():
        if char not in "aeiou":
            out += char
    if len(out) != 0:
        val = max(val,fact(len(out)))
print(val)