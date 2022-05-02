import random
def main():
  a=random.randrange(1,4)
  #print(a)  
  value = input("\nEnter a move: ")
 
  #print(f'{value}')

  if(a==1):
   b="Scissors"
   print(b)
  elif(a==2):
   b="Paper"
   print(b)
  else:
   b="Rock"
   print(b)  

  if(b==value):
    print("It's a draw!")

  #With Scissors  
  elif(value=="Scissors" and b=="Paper"):
    print("You win!")
  elif(value=="Scissors" and b=="Rock"):
    print("You lose!")

  #With Paper
  elif(value=="Paper" and b=="Scissors"):
    print("You lose!")  
  elif(value=="Paper" and b=="Rock"):
    print("You win!")

  #With Rock
  elif(value=="Rock" and b=="Scissors"):
    print("You win!")
  else:
    print("You lose!")



   
      

if __name__=="__main__":
    main()