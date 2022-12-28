import random
import randomlist
import randomstages

display = []
word_list = randomlist.word_list
chosen_word = random.choice(word_list)
top_word = len(chosen_word)
print(randomstages.logo)

lives = 6
empty = "_"

for x in range(top_word):
    display+= empty

while empty in display:
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print("That letter already in ")

        for letter in range(top_word):
            x = chosen_word[letter]
            if x == guess:
                display[letter] = x

        if chosen_word.count(guess) == 0:
            lives -= 1
            print("You lost health")
            print(lives)
            print(randomstages.stages[lives])

        if chosen_word.count(guess) == False:
            print("That letter is not in the word")

        if lives == 0:
            print("game over")
            break

        print(display)

if empty not in display:
    print("You won")





