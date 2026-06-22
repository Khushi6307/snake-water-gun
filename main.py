# importing random
import random

# Game encoding: snake=1, water=-1, gun=0
computer = random.choice([1, -1, 0])

# Get player input
youstr = input("Enter your choice (s/w/g): ")

# Map input letters to numeric values
youDic = {"s": 1, "w": -1, "g": 0}

# Map numeric values back to names for display
reverse_dic = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDic[youstr]

print(f"You chose {reverse_dic[you]}")
print(f"Computer chose {reverse_dic[computer]}")

# Check result
if computer == you:
    print("It's a draw!")

else:
    # Water vs Snake → Snake wins
    if computer == -1 and you == 1:
        print("You Win!")

    # Water vs Gun → Gun loses
    elif computer == -1 and you == 0:
        print("You Lose!")

    # Snake vs Water → Snake wins
    elif computer == 1 and you == -1:
        print("You Lose!")

    # Snake vs Gun → Gun wins
    elif computer == 1 and you == 0:
        print("You Win!")

    # Gun vs Snake → Gun wins
    elif computer == 0 and you == 1:
        print("You Lose!")

    # Gun vs Water → Water wins
    elif computer == 0 and you == -1:
        print("You Win!")

    else:
        print("Something went wrong!")
    
