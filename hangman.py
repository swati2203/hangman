import string
from words import choose_word
from images import IMAGES
def ifvalid(user_input):
      if len(user_input)!=1:
            return False
      if not user_input.isalpha():
            return False
      return False


# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_gussed):
      if secret_word==get_guessed_word(secret_word,letters_gussed):
            return True
      return False

def get_guessed_word(secret_word, letters_gussed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_gussed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letter_guessed):
    import string
    letters_left = string.ascii_lowercase
    for i in letter_guessed:
          letters_left=letters_left.replace(i," ")
    return letters_left

def get_hint(secret_word,letters_guessed):
      import random
      letter_not_guessed=[]
      for i in secret_word:
            if i not in letters_guessed:
                  if i not in letter_not_guessed:
                        
                        letter_not_guessed.append(i)
                    
      return random.choice(letter_not_guessed)

reamaining_lives=8
total_lives=ramaining_lives=8
def hangman(secret_word):
      print("welcome to the game,hangman")
      print(secret_word,"secret_word")
      print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
      print("")
      letters_guessed = []
      level=input("enter the level you want to play:\n (a)easy\n""(b)medium\n""(c)difficult:")
      total_lives=remaining_lives=8
      images_selection_last_indices=[0,1,2,3,4,5,6,7]
      if level=="b":
            total_lives=remaining_lives=6
            image_selection=[0,2,3,5,6,7]
      elif level=="c":
            total_lives=remaining_lives=4
            image_selection=[1,3,5,7]
      elif level=="a":
            total_lives=remaining_lives=8
            image_selection=[0,1,2,3,4,5,6,7]
      else:
        if level!="a":
              print("your choice is invalid")

      while remaining_lives>0:
            available_letters = get_available_letters(letters_guessed)
            print("Available letters: " , available_letters)
            guess = input("Please guess a letter: ")
            letter = guess.lower()
            if letter=="hint":
                  print("your hint for secret word is",get_hint(secret_word,letters_guessed))
            # elif (not ifvalid(letter)):
                  # print("invalid")
            elif letter in secret_word:
                  letters_guessed.append(letter)
                  print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                  print("")
                  if is_word_guessed(secret_word, letters_guessed) == True:
                        print(" * * Congratulations, you won! * * ")
                        print("")
                        break
                  # else:
                  #       print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                  #       letters_guessed.append(letter)
            else:
                  print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                  letters_guessed.append(letter)
                  print(IMAGES[image_selection[total_lives-remaining_lives]])
                  remaining_lives-=1
                  print("remaining lives :"+str(remaining_lives))
                  print("")
            # elif (not ifvalid(letter)):
            #       print("invalid")
      else:
            print("sorry you run out of the guess,the word was"+str(secret_word)+".")
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)

   