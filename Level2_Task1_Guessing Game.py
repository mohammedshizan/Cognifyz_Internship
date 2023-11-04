import random
randNumber=random.randint(1,100)
userguess=None
guesses=0


while(userguess!=randNumber):
      userguess=int(input("Enter your guess:"))
      guesses+=1
      if(userguess==randNumber):
         print("You guessed it write!")
      else:
        if(userguess>randNumber):
             print("Too High")
        else:
             print("Too Low")

print(f"You guessed the number in {guesses} guesses")


           
           
                  
      