print("Think of a number between 1 and 1000.")
input("Press Enter when you're ready...")

low = 1
high = 1000
guess = 0

while True:
    guess = (low + high) // 2  
    print("Is your number:", guess, "?")
    
    answer = input("Type 'h' if too high, 'l' if too low, 'c' if correct: ")

    if answer == "c":
        print("Yay! I guessed your number!")
        break

    if answer == "h":
        high = guess - 1

    if answer == "l":
        low = guess + 1
