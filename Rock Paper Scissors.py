def winningmove(input1):
    if input1 == "rock":
        return "paper"
    elif input1 == "paper":
        return "scissors"
    elif input1 == "scissors":
        return "rock"
    
input1 = input()
print(winningmove(input1))