import random
from Stages import stages

word_list = [
    "aardvark", "baleia", "camelo", "doninha", "elefante",
    "flamingo", "galinha", "hiena", "iguana", "jararaca",
    "kiwi", "lince", "morsa", "narval", "ovelha", "papagaio",
    "quati", "rinoceronte", "suricate", "tartaruga", "urso",
    "vagalume", "wallaby", "ximango", "yak", "zebra"
]

chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)

lives = 6
game_over = False

print("🎮 Welcome to Hangman!")

while not game_over:

    print(stages[lives])
    print(f"\nLives Remaining: {lives}")
    print("Word:", " ".join(display))

    guess = input("\nGuess a letter: ").lower()

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
    else:
        lives -= 1
        print(f"❌ '{guess}' is not in the word.")

    if "_" not in display:
        print("\n🎉 Congratulations! You guessed the word:")
        print(chosen_word)
        game_over = True

    elif lives == 0:
        print(stages[0])
        print(f"\n💀 Game Over! The word was '{chosen_word}'.")
        game_over = True
