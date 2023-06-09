# OS means output stream / operating system 
import os 

def wordChecker(secretWordTwo, correctLetter):
  for x in secretWordTwo:
    if x not in correctLetter:
      return False
  

# Camel Case
secretWord = input("Please input the secret word\n")
secretWord = secretWord.lower()

# category/topic/hint
hint = input("What's the topic of the secret word\n")

lives = 10 

os.system('clear')

print("If you would like to see a hint type 'hint!'")

correctLetters = []
correctLetters.append(secretWord)
incorrectLetters = []

correct = False 

while correct is False or lives != 0:
  
  guess = input("Please guess a letter\n") 
  if guess == "hint!":
    print("The hint is", hint)
    continue

  if guess == secretWord:
    print("You guessed the word correctly, You win!\n")
    break
  else:
    print("Sorry that was not the secret word\n")
    lives = lives - 10
    continue

  if guess in secretWord:
    print("You got one of the letters correct!")
    correctLetters.append(guess)

  elif guess not in secretWord:
    print("Sorry, that letter is not in our secret word")
    incorrectLetters.append(guess)
    lives =- 1

  elif guess in correctLetters:
    print("You already guessed that letter and it was correct")

  elif guess in incorrectLetters:
    print("You already guessed that letter and it was incorrect")

  if wordChecker(secretWord, correctLetters) != False:
    print("You guessed the word correctly!\n")
    print("You win!\n")
    break
    
  
