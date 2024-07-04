import random

while True:
    n = random.randint(1, 50)
    a = -1
    guesses = 0
    print("********************************************* The Perfect Guess **********************************************************")
    while a != n:
        guesses += 1
        a = int(input("Guess the number (between 1 and 50): "))
        if (a > n):
            print("Lower number please")
        elif (a < n):
            print("Higher number please")

    print(f"Congratulations! You guessed the number {n} correctly in {guesses} attempts")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "yes":
        continue
    else:
        break

print("Thanks for playing The Perfect Guess game!")
