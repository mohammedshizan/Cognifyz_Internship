import random
randGuess=random.randint(1,20)
userguess=None
guesses=0

while(userguess!=randGuess):
      userguess=int(input("Enter the guess:"))
      if(userguess==randGuess):
            print("You guess the right number!")
      else:
          if(userguess>randGuess):
                print("It's wrong! Your guess is too high")
          else:
                print("It's wrong! Your guess is too low")
                


print("Thank you! For playing it") 
 
                          