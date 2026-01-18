
import random
import time

high_scores = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}

def show_rules():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You must guess the number within limited chances.\n")

def select_difficulty():
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            return "Easy", 10
        elif choice == "2":
            return "Medium", 5
        elif choice == "3":
            return "Hard", 3
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def give_hint(secret_number):
    return "Hint: The number is EVEN." if secret_number % 2 == 0 else "Hint: The number is ODD."

def play_game():
    show_rules()
    difficulty, chances = select_difficulty()

    print(f"\nGreat! You have selected the {difficulty} difficulty level.")
    print("Let's start the game!")

    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    for remaining in range(chances, 0, -1):
        try:
            guess = int(input(f"\nEnter your guess ({remaining} chances left): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            time_taken = round(time.time() - start_time, 2)
            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {time_taken} seconds")

            if high_scores[difficulty] is None or attempts < high_scores[difficulty]:
                high_scores[difficulty] = attempts
                print("New High Score!")
            return
        elif guess > secret_number:
            print("Incorrect! The number is LESS than your guess.")
        else:
            print("Incorrect! The number is GREATER than your guess.")

        if attempts == chances // 2:
            print(give_hint(secret_number))

    print("\nYou've run out of chances!")
    print(f"The correct number was: {secret_number}")

def show_high_scores():
    print("\nHigh Scores:")
    for level, score in high_scores.items():
        print(f"{level}: {score if score else 'No record'}")

def main():
    while True:
        play_game()
        show_high_scores()
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
