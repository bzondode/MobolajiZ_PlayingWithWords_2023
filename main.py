### Setup Section ###

# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")

# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):

  # Loop through each index/position 
  for index in range(6):

    # Grab the letter from the guess
    letter = guess[index]

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
    if(letter in actual):         

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
      if(letter == actual[index]):

        # Then print it out with a green background
        printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
      else:

        # ...so we'll print it out with a yellow background
        print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")
        
    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      print(Back.RED + Fore.WHITE + f" {letter} ", end="")
      
    # Don't worry about the line of code below, it works. It just handles the transition between colors
    print(Style.RESET_ALL + " ", end="")

# TO-DO: Write a Function that takes in a six-lettered word from the user

# Create a function that takes in a six-lettered word from user
def getSixLetterInput():

  # Get input from user
  #while(True):
  wordInput = input("Please enter a six-lettered word: ")
  while(len(wordInput) != 6):
    
    # Prompt user for valid input again
    wordInput = input("Invalid Input. Please enter a six-lettered word: ")

    # Return word as a string  
  return wordInput

 
# This marks the end of the function definitions, below this is where the program will actually start!

### Main Program ###

# TO-DO: Write the logic of the game here!


# Display a welcome message and friendly title
print(r"""_______   __                      __                            __       __  __    __      __              __       __                            __            __ 
|       \ |  \                    |  \                          |  \  _  |  \|  \  |  \    |  \            |  \  _  |  \                          |  \          |  \
| $$$$$$$\| $$  ______   __    __  \$$ _______    ______        | $$ / \ | $$ \$$ _| $$_   | $$____        | $$ / \ | $$  ______    ______    ____| $$  _______ | $$
| $$__/ $$| $$ |      \ |  \  |  \|  \|       \  /      \       | $$/  $\| $$|  \|   $$ \  | $$    \       | $$/  $\| $$ /      \  /      \  /      $$ /       \| $$
| $$    $$| $$  \$$$$$$\| $$  | $$| $$| $$$$$$$\|  $$$$$$\      | $$  $$$\ $$| $$ \$$$$$$  | $$$$$$$\      | $$  $$$\ $$|  $$$$$$\|  $$$$$$\|  $$$$$$$|  $$$$$$$| $$
| $$$$$$$ | $$ /      $$| $$  | $$| $$| $$  | $$| $$  | $$      | $$ $$\$$\$$| $$  | $$ __ | $$  | $$      | $$ $$\$$\$$| $$  | $$| $$   \$$| $$  | $$ \$$    \  \$$
| $$      | $$|  $$$$$$$| $$__/ $$| $$| $$  | $$| $$__| $$      | $$$$  \$$$$| $$  | $$|  \| $$  | $$      | $$$$  \$$$$| $$__/ $$| $$      | $$__| $$ _\$$$$$$\ __ 
| $$      | $$ \$$    $$ \$$    $$| $$| $$  | $$ \$$    $$      | $$$    \$$$| $$   \$$  $$| $$  | $$      | $$$    \$$$ \$$    $$| $$       \$$    $$|       $$|  \
 \$$       \$$  \$$$$$$$ _\$$$$$$$ \$$ \$$   \$$ _\$$$$$$$       \$$      \$$ \$$    \$$$$  \$$   \$$       \$$      \$$  \$$$$$$  \$$        \$$$$$$$ \$$$$$$$  \$$
                        |  \__| $$              |  \__| $$                                                                                                          
                         \$$    $$               \$$    $$                                                                                                          
                          \$$$$$$                 \$$$$$$                                                                                                           """)
print("Welcome to 'Playing with words'!")
print("There is a secret word to guess. You will have six tries to guess this word and for each correct guess entered, the letters will be highlighted a specific color based on whether or not they are part of the secret word.")
print("The color codings are as follows:")
print("  * A letter will have a green background if it is both in the word and in the correct place.")
print("  * A letter will have a yellow background if the letter is in the word but not in the correct place in that word")
print("  * A letter will have a red background if the letter is not in the word at al")
print()


actual = "poetry"
tries = 6

# Repeat the player's turn until they either run out of tries or guess the word correctly
while tries > 0:
    # Print remaining tries and guesses
    print(f"You have {tries} tries left.")
    
    # On each turn, take in a word, and show them how accurate it was
    guess = getSixLetterInput()
    # Check if guess is correct
    if guess == actual:
      printColorfulLetter(guess, True, True)
      print("Congratulations! You guessed the secret word!")
      break
    else:
      
      printGuessAccuracy(guess, actual)
      tries -= 1

# When they have run out of tries, tell them if they won or lost
if tries == 0:
    print(f"Sorry, you ran out of tries. The secret word was {actual}. Better luck next time!")