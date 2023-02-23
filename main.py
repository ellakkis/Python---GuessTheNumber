#Number Guessing Game Objectives:
import random
from art import logo 

# Include an ASCII art logo.

play_another_game = True
user_guessed_correctly = False


def play_game():
  user_guess = 0
  print(logo)
  lives = 5
  secret_number = random.randint(1,101)
  print("\n\nWelcome to the guessing number game!\nAm thinking of a number between 1 and 100")
  
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
  dificulity_level = input("Chose dificulity level. Type E for easy or H for hard: ").lower()
  if dificulity_level == "h":
    lives = 5
  else:
    lives = 10

  print(f"You have {lives} attempts remaining to guess the number")
  
  
  
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
  while user_guess != secret_number and lives != 0:
    # Allow the player to submit a guess for a number between 1 and 100.
    user_guess = int(input("Make a guess: "))
    # If they got the answer correct, show the actual answer to the player.
    if user_guess == secret_number:
      user_guessed_correctly == True
      print(f"Your guess is correct! The secret number is {secret_number} You Win!")
    elif user_guess > secret_number:
      lives -= 1 # Track the number of turns remaining.
      if lives != 0:
        print("Go lower...")
    elif user_guess < secret_number:
      lives -= 1
      if lives != 0:
        print("Go higher...")
    
    


# If they run out of turns, provide feedback to the player. 
  if lives == 0 and user_guessed_correctly == False:
    print(f"You did not guess right! The secret number is {secret_number}")
    print("Game over!")

play_game()