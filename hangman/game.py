import random
import os


# --- Hangman Art ---
hangman_pics = [
r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


# --- Function to handle guessing logic ---
def making_a_guess():
  x = 0
  global update_display
  correct_guess = False
  for letter in chosen_word:
    if guess.lower() == chosen_word[x]:
      blank_list[x] = guess.lower()
      correct_guess = True
    x += 1
  if not correct_guess:
    print(f"There is no {guess}, sorry.")
    update_display += 1
  x = 0


# --- Word List ---
WORD_LIST = ["aardvark", "baboon", "camel", "shark", "jazz", "computer", "castle", "chip"]

# --- Load words in word.txt file ---
try:
  here = os.path.dirname(__file__)
  with open(os.path.join(here, "words.txt"), "r", encoding="utf-8") as f:
    extra_words = [w.strip().lower() for w in f if w.strip()]
  WORD_LIST += extra_words #merges both word lists
  print(f"Loaded {len(extra_words)} words from Word File")
  print(f"Total Word List Size: {len(WORD_LIST)}")
except FileNotFoundError:
  pass



chosen_word = list(random.choice(WORD_LIST))

blank = "_" * len(chosen_word)
blank_list = list(blank)

update_display = 0


# --- Game Loop ---
print(hangman_pics[update_display])
guess = input(f"Welcome to hangman.\n{blank} \nMake a guess! ")
making_a_guess()
print (hangman_pics[update_display])
print(''.join(blank_list))
while update_display < 6:
  if blank_list == chosen_word:
    print("YOU WIN!")
    print(f"The word was: {chosen_word}")
    break
  guess = input("Make another guess! ")
  making_a_guess()
  print(hangman_pics[update_display])
  print(''.join(blank_list))
if update_display == 6:
  print("GAME OVER.")
  print(f"The word was: {chosen_word}")
