import random

# Prompt the user to choose the game mode
mode = input("You want to play in which mode? (P_Vs_P / P_Vs_C) ").strip()

# Snakes: key is the start point, value is the end point
snakes = {
    95: 7,
    99: 75,
    92: 88,
    89: 68,
    74: 53,
    64: 60,
    62: 19,
    49: 11,
    46: 25,
    16: 6
}

# Ladders: key is the start point, value is the end point
ladders = {
    1: 38,
    4: 40,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 69,
    71: 91,
    80: 98,
    87: 94
}

def PlayerVsComp():
    # Initialize scores
    player_score = 0
    comp_score = 0
    max_score = 100

    while True:
        # Prompt to roll the dice
        dice_roll = input("Roll the dice (y/n)? ").strip().lower()

        if dice_roll == "y":
            # Roll dice for player and computer
            x = random.randint(1, 6)
            player_score += x

            y = random.randint(1, 6)
            comp_score += y
            
            print("Player rolled: " + str(x))
            print("Computer rolled: " + str(y))
            print(" ")
            
            # Check for snakes and ladders for the player
            if player_score in snakes:
                player_score = snakes[player_score]
                print("Player was hit by a snake and is now at " + str(player_score))
                print(" ")

            elif player_score in ladders:
                player_score = ladders[player_score]
                print("Player climbed a ladder and is now at " + str(player_score))
                print(" ")

            # Check for snakes and ladders for the computer
            if comp_score in snakes:
                comp_score = snakes[comp_score]
                print("Computer was hit by a snake and is now at " + str(comp_score))
                print(" ")

            elif comp_score in ladders:
                comp_score = ladders[comp_score]
                print("Computer climbed a ladder and is now at " + str(comp_score))
                print(" ")

            print("Player's Score: " + str(player_score))
            print("Computer's Score: " + str(comp_score))
            print(" ")

            if player_score >= max_score:
                print("You win")
                quit()
            elif comp_score >= max_score:
                print("Computer wins")
                quit()

        else:
            print("You lost")
            quit()

def PlayerVsPlayer():
    # Get player names
    name_1 = input("First person's name: ").strip()
    name_2 = input("Second person's name: ").strip()
    player_1_score = 0
    player_2_score = 0
    max_score = 100

    while True:
        # Prompt to roll the dice
        dice_roll = input("Roll the dice (y/n)? ").strip().lower()

        if dice_roll == "y":
            # Roll dice for both players
            x = random.randint(1, 6)
            player_1_score += x

            y = random.randint(1, 6)
            player_2_score += y
            
            print(name_1 + " rolled: " + str(x))  
            print(name_2 + " rolled: " + str(y))
            print(" ")

            # Check for snakes and ladders for player 1
            if player_1_score in snakes:
                player_1_score = snakes[player_1_score]
                print(name_1 + " was hit by a snake and is now at " + str(player_1_score))
                print(" ")

            elif player_1_score in ladders:
                player_1_score = ladders[player_1_score]
                print(name_1 + " climbed a ladder and is now at " + str(player_1_score))
                print(" ")

            # Check for snakes and ladders for player 2
            if player_2_score in snakes:
                player_2_score = snakes[player_2_score]
                print(name_2 + " was hit by a snake and is now at " + str(player_2_score))
                print(" ")

            elif player_2_score in ladders:
                player_2_score = ladders[player_2_score]
                print(name_2 + " climbed a ladder and is now at " + str(player_2_score))
                print(" ")

            print(name_1 + " score: " + str(player_1_score))
            print(name_2 + " score: " + str(player_2_score))
            print(" ")

            if player_1_score >= max_score:
                print(name_1 + " Wins")
                quit()
            elif player_2_score >= max_score:
                print(name_2 + " Wins")
                quit()

        else:
            print("Thanks for Playing.")
            quit()

# Check game mode and start the appropriate function
if mode == "P_Vs_P":
    PlayerVsPlayer()
elif mode == "P_Vs_C":
    PlayerVsComp()
else:
    print("Invalid mode selected. Please restart the game and choose a valid mode.")