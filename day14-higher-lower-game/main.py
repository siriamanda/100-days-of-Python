from art import logo, vs
from game_data import data
import random
from replit import clear

def game():

  print(logo)
  
  random_selection_A = random.choice(data)
  random_selection_B = random.choice(data)
  if random_selection_A == random_selection_B:
    random_selection_B = random.choice(data)

  keep_playing = True
  player_score = 0

  previous_entries = []

  while keep_playing:

    print(f"Compare A: {random_selection_A['name']}, a {random_selection_A['description']}, from {random_selection_A['country']}")

    print(vs)

    print(f"Against B: {random_selection_B['name']}, a {random_selection_B['description']}, from {random_selection_B['country']}")

    player_selection = input("Who has more followers? Type 'A' or 'B': ")
  
    follower_count_A = random_selection_A['follower_count']
    follower_count_B = random_selection_B['follower_count']
  
    if (player_selection == "A" and follower_count_A > follower_count_B) or (player_selection == "B" and follower_count_B >  follower_count_A):
      
      player_score += 1

      previous_entries.append(random_selection_A)

      random_selection_A = random_selection_B
      random_selection_B = random.choice(data)

      while random_selection_A == random_selection_B or random_selection_B in previous_entries:
        random_selection_B = random.choice(data)

      clear()

      print(logo)
      print(f"You're right! Current score: {player_score}")
  
      continue
    
    elif (player_selection == "A" and follower_count_A < follower_count_B) or (player_selection == "B" and follower_count_B < follower_count_A):
    
      keep_playing = False

      clear()
    
      print(logo)
      print(f"Sorry, that's wrong. Final score: {player_score}")
      
      play_again = input("Do you want to play again? Type 'Y' or 'N': ")

      if play_again == "Y":
        keep_playing = True

        random_selection_A = random.choice(data)
        random_selection_B = random.choice(data)

        player_score = 0

        clear()
        print(logo)

        continue

      else:
        clear()
        print(logo)
        print("Goodbye! Game closed.")  

game()


                   