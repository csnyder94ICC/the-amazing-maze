import pickle

# Rooms and scenarios with choices for the maze in list format

rooms = {
    'start': {
        'description': 'Welcome to the Amazing Maze! The goal is to find the treasure and escape before it is too late...do you wish to enter?',
        'choices': ['Enter the maze.', 'Exit game.']
    },
    'room1': {
        'description': 'You stumble into a room and on the wall is written a riddle. I am an odd number. Take away a letter and I become even. What number am I? Each door has an answer. On the left door it says 23. On the middle door it says 7. And the right door says 1. Choose wisely.',
        'choices': ['Go through the left door.', 'Go through the middle door.', 'Go through the right door.']
    },
    'room2': {
        'description': 'Ahh. You have chosen incorrectly. I guess we will take the long way. Decide which way you should go.',
        'choices': ['Go left.', 'Go right.', 'Go back to the riddle room.']
    },
    'treasure_room': {
        'description': 'You made it! Grab some treasure and be on your way.',
        'choices': ['Take some treasure.']
    },
    'dead_end': {
        'description': 'You are in an empty room. This was the wrong choice and there is nothing here.',
        'choices': ['Go back.']
    },
    'exit': {
        'description': "It seems you have found the treasure. Congratulations, you may now exit the maze!",
        'choices': ['Exit game.']
    }
}

# Initialize game state
current_room = 'start'
game_over = False

# Function to save the game state to a file
def save_game_state(game_state):
    with open('game_state.pkl', 'wb') as file:  #Open a binary file for writing
        pickle.dump(game_state, file)  #Serialize and save the game state using pickle

# Define a function to load the game state from a file
def load_game_state():
    try:
        with open('game_state.pkl', 'rb') as file:  # Open a binary file for reading
            return pickle.load(file)  # Deserialize and return the game state stored in the file
    except FileNotFoundError:
        return 'start'  # If the file doesn't exist, start the game from the beginning

# Game loop
while not game_over:
    room = rooms[current_room]

    # Displays room descriptions and choices
    print(room['description'])
    for i, choice in enumerate(room['choices']):
        print(f'{i + 1}. {choice}')

    # Input for player choice
    choice_num = input('Enter your choice: ')

    # Decision structure to handle player choice
    if choice_num.isdigit():
        choice_num = int(choice_num)
        if 1 <= choice_num <= len(room['choices']):
            choice = room['choices'][choice_num - 1]
            if choice == 'Exit game.':
                confirm = input("Are you sure you want to exit the game? (yes/no): ").lower()
                if confirm == 'yes':
                    print("Thank you for playing! Goodbye!")
                    game_over = True
                else:
                    print("Returning to the game.")
            elif current_room == 'start':
                if choice == 'Enter the maze.':
                    current_room = 'room1'
            elif current_room == 'room1':
                if choice == 'Go through the left door.':
                    current_room = 'room2'
                elif choice == 'Go through the middle door.':
                    current_room = 'treasure_room'
                elif choice == 'Go through the right door.':
                    current_room = 'room2'
            elif current_room == 'room2':
                if choice == 'Go left.':
                    current_room = 'dead_end'
                elif choice == 'Go right.':
                    current_room = 'treasure_room'
                elif choice == 'Go back to the riddle room.':
                    current_room = 'room1'
            elif current_room == 'treasure_room':
                if choice == 'Take some treasure.':
                    current_room = 'exit'
            elif current_room == 'dead_end':
                if choice == 'Go back.':
                    current_room = 'room2'
            elif current_room == 'exit':
                if choice == 'Exit game.':
                    game_over = True
        else:
            print("Invalid choice number. Please choose a valid option.")
    else:
        print("Invalid input. Please enter a valid choice number.")

#Saves the game before exiting
save_game_state(current_room)
