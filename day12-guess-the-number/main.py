#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("Welcome to the number guessing game! \nI am thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level == "easy":
  attempts = 10
else:
  attempts = 5

print(f"You have {attempts} attempts to guess the number.")

random_number = random.randint(1, 100)

while attempts > 0:
  player_guess = int(input("Make a guess: "))
  if player_guess > random_number:
    print("Too high.")
    attempts = attempts - 1
    if attempts > 0:
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif attempts == 0:
        print("You've run out of guesses, you lose.")
    
  elif player_guess < random_number:
    print("Too low.")
    attempts = attempts -1
    if attempts > 0:
      print("Guess again.")
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif attempts == 0:
      print("You've run out of guesses, you lose.")  
  elif player_guess == random_number:
    print(f"You got it! The answer was {random_number}")
    break

    
  

