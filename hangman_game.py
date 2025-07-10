import random
def hangman_game():
    words = ["apple", "banana", "orange", "grapes", "mango"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    display = ["_"] * len(word)

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    
    while attempts > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for idx, letter in enumerate(word):
                if letter == guess:
                    display[idx] = guess
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}")
    
    if "_" not in display:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"\n😢 You lost! The word was: {word}")

hangman_game()
