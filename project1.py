'''
gun = 0
water = -1
snak = 1

'''
import random

# Dictionaries to map choices to numerical values and back
dict = {
    "g": 0,
    "w": -1,
    "s": 1
}
reverse_dict = {
    0: "Gun",
    -1: "Water",
    1: "Snake"
}

# Randomly select computer's choice
computer = random.choice([-1, 0, 1])

# Prompt user for their choice
choice = input("Enter your choice (g for Gun, w for Water, s for Snake): ").lower()

# Check if the input is valid
if choice in dict:
    user = dict[choice]

    # Display choices
    print(f"You chose {reverse_dict[user]}\nComputer chose {reverse_dict[computer]}")

    # Determine and display the result
    if user == computer:
        print("It's a tie!")
    elif  (user == 1 and computer == -1) or (user==-1 and computer==0) or (user==0 and computer ==1 ):
        print("You win!")
    else:
        print("You lose! Try again.")
else:
    print("Invalid choice. Please enter 'g', 'w', or 's'.")