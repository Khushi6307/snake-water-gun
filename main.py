
import random

'''
1 for snake
-1 for water
0 for gun
'''

computer=random.choice([1,-1,0])
youstr = input("Enter your choice : ")
youDic = {"s":1, "w":-1, "g":0}
reverse_dic={1:"snake", -1 :"water", 0 :"Gun"}
you = youDic[youstr]

print(f"You chose {reverse_dic[you]}\nComputer chose {reverse_dic[computer]}")

if(computer == you):
    print("It's a draw")

else:
    
    """if(computer == -1 and you == 1):#-2
      print("You Win!")

    elif(computer==-1 and you==0):#-1
     print("You lose!")

    elif(computer==1 and you==-1):#2
     print("You lose!")

    elif(computer==1 and you==0):#1
     print("You Win!")

    elif(computer==0 and you==1):#-1
     print("You lose!")

    elif(computer==0 and you==-1):#1
     print("You Win!")

    else:
     print("Something went wrong!")"""

    if((computer-you)==-1 or(computer-you)==2 ):
      print("You lose!")
    else:
      print("You Win!")
