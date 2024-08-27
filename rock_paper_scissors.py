import random

rock = int("0")
paper = int("1")
scissors = int("2")

user_chocie = int(input("What do you choose? Type 0 for rock, Type 1 for paper or Type 2 for scissors.\n"))
computer_choice = random.randint(0, 2)

print(f"You chose {user_chocie}")
print (f"Computer chose {computer_choice}")

if user_chocie == 0 and computer_choice == 1:
    print ("Paper beats Rock! Computer wins")
elif user_chocie == 0 and computer_choice == 2:
    print ("Rock beats Scissors! You win.")
elif user_chocie == 1 and computer_choice == 0:
    print ("Paper beats Rock! You win.")
elif user_chocie == 1 and computer_choice == 2:
    print("Scissors beats Paper! Computer wins.")
elif user_chocie == 2 and computer_choice == 0:
    print ("Rock beats Scissors! Computer wins.")
elif user_chocie == 2 and computer_choice == 1:
    print("Scissors beats Paper! You win.")
elif user_chocie == computer_choice:
    print("It's a draw")
else:
    print ("You typed an invalid number. Game Over!")