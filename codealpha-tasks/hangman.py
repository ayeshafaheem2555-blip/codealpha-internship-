print("Welcome to Hangman Game")

import random

words = ["python", "computer", "developer", "network", "program"]
word = random.choice(words)
guessed = ""
tries = 6

print("🎯 Welcome to Hangman Game!")
print("_ " * len(word))

while tries > 0:
    guess = input("\nGuess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    if guess in word:
        print("✅ Correct!")
        guessed += guess
    else:
        print("❌ Wrong guess!")
        tries -= 1
        print("Tries left:", tries)

    
    display = ""
    for ch in word:
        display += ch if ch in guessed else "_ "
    print(display)

    if "_" not in display:
        print("\n🎉 You won! The word was:", word)
        break
else:
    print("\n💀 Game Over! The word was:", word)
