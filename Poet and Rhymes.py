def findRhyme(input1, input2, input3):
    out = "No Word"
    max_val = 0
    t = input1[::-1]
    for word in input2:
        if word != input1:
            cur = 0
            s = word[::-1]
            i = 0
            while i < min(len(s),len(t)):
                if s[i] == t[i]:
                    cur += 1
                else:
                    break
                i += 1
            if cur > max_val:
                max_val = cur
                out = word
    return out


input1 = input()
input2 = input().split()
input3 = int(input())