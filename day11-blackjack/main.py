# Instructions

#Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
 
#Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random
from art import logo
from replit import clear

def deal_card(cards):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  
  return random.choice(cards)

def calculate_score(card_list):

  if len(card_list) == 2 and sum(card_list) == 21:
    return 0

  elif 11 in card_list and sum(card_list) > 21:
    card_list.remove(11)
    card_list.append(1)
    return sum(card_list)

  else:
    return sum(card_list)

def compare(user_score, computer_score):

  if computer_score == 0 and user_score == 0:
    print("You both got blackjack. It's a draw!")

  elif user_score == 0:
    print("You got a blackjack! You win!")

  elif user_score > 21:
    print("You went over. You lost!")

  elif computer_score == 0:
    print("The computer got blackjack. You lost!")

  elif computer_score > 21:
    print("The computer went over. You win!")

  elif computer_score > user_score:
    print("The computer won!")

  elif computer_score < user_score:
    print("You won!")

  elif computer_score == user_score:
    print("It's a draw!")



start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while start_game == "y":

  print(logo)

  user_cards = [deal_card(cards), deal_card(cards)]
  computer_cards = [deal_card(cards), deal_card(cards)]

  keep_playing = True

  while keep_playing:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"   Your cards: {user_cards}, Your score: {user_score}")
    print("   Computer's first card: ", computer_cards[0])

    next_move = input("Type 'y' to get another card, type 'n' to pass: ")

    if next_move == "y":
        
      user_cards.append(deal_card(cards))

      if calculate_score(user_cards) > 21:

        while computer_score < 17:
        
          computer_cards.append(deal_card(cards))
          computer_score = calculate_score(computer_cards)

        user_score = calculate_score(user_cards)
      
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You went over. You lost!")
        
        keep_playing = False

        start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

        if start_game == "y":
          clear()
          continue

        elif start_game == "n":
          clear()
          print("Game ended")

      else:
      
        continue

    elif next_move == "n":
      while computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

      user_score = calculate_score(user_cards)
    
      print(f"    Your final hand: {user_cards}, final score: {user_score}")
      print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

      compare(user_score, computer_score)

      keep_playing = False

      start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

      if start_game == "y":
        clear()
        continue

      elif start_game == "n":
        clear()
        print("Game ended")



