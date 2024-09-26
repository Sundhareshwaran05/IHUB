def island_life(input1, input2, input3):
    days = input3 - input3//7
    required = input2 * input3
    maximum = input1 * days
    if required > maximum:
        return -1
    box =  required // input1
    if required % input1 != 0:
        box += 1
    return box


input1 = int(input())
input2 = int(input())
input3 = int(input())