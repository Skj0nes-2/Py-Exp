def input_func():
    from random import choice
    global hand; hand = input("(R)ock (P)aper (S)cissors: ").lower()
    global bot; bot = choice(["r", "p", "s"])
def check_func():
    global hand; global bot; global result
    match hand:
        case "r":
            if bot == "s":
                result = "Win"
            elif bot == "p":
                result = "Lose"
        case "p":
            if bot == "r":
                result = "Win"
            elif bot == "s":
                result = "Lose"
        case "s":
            if bot == "p":
                result = "Win"
            elif bot == "r":
                result = "Lose"
        case _:
            print("Invalid Hand!")
    if bot == hand:
        result = "Tie"
def output_func():
    global result; global isPlaying
    print(result)
def replay():
    global isPlaying
    playCheck = input("Continue Playing? (Y)es (N)o: ").lower()
    if playCheck == "n":
        isPlaying = False
isPlaying = True
while isPlaying:
    input_func()
    check_func()
    output_func()
    replay()