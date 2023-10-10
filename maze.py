import pickle

# Define scenarios I would recommend using dictionaries. Samantha, Do you want to do the dialogue for the rooms and choices? Keep room names the same though. 
rooms = {
    'start': {
        'description': 'Welcome to the Amazing Maze! The goal is to find the treasure and escape before it is too late...do you wish to enter?',
        'choices': ['Enter the maze.', 'Exit game']
    },
    'room1': {
        'description': 'You stumble into a room and on the wall is written a riddle. I am an odd number. Take away a letter and I become even. What number am I? Each door has an answer. On the left door it says 23. On the middle door it says 7. And the right door says 1. Choose wisely.',
        'choices': ['Go through the left door.', 'Go through the middle door.', 'Go through the right door.', 'Go back.']
    },
    'room2': {
        'description': 'Ahh. You have chosen incorrectly. I guess we will take the long way. Decide which way you should go.',
        'choices': ['Go left.', 'Go right.', 'Go back.']
    },
    'treasure_room': {
        'description': 'You made it! Grab some treasure and be on your way.',
        'choices': ['Take some treasure.', 'Leave the treasure room.', 'Go back']
    },
    'exit': {
        'description': "It seems you have made it out with the treasure. Congratulations!",
        'choices': ['Exit game.']
    }
}

#Game initialization below (Reference material: https://codereview.stackexchange.com/questions/159818/save-and-load-the-state-of-a-role-playing-game-using-pickle) 

# Initialize game state
current_room = 'start'
game_over = False

#Function to save the game state to a file
def save_game_state(game_state):
    with open('game_state.pkl', 'wb') as file:  #Open a binary file for writing
        pickle.dump(game_state, file)  #Serialize and save the game state using pickle

#Define a function to load the game state from a file
def load_game_state():
    try:
        with open('game_state.pkl', 'rb') as file:  #Open a binary file for reading
            return pickle.load(file)  #Deserialize and return the game state stored in the file
    except FileNotFoundError:
        return 'start'  #If the file doesn't exist, start the game from the beginning

# Define the game loop below here

# Game loop
while not game_over:
    room = rooms[current_room]

    # Displays Samanthas room Descriptions and choices
    print(room['description'])
    for i, choice in enumerate(room['choices']):
        print(f'{i + 1}. {choice}')

    # What the player chooses
    choice_num = input('Enter your choice: ')

    # Code to handle player choice
    if choice_num.isdigit():
        choice_num = int(choice_num)
        if 1 <= choice_num <= len(room['choices']):
            choice = room['choices'][choice_num - 1]
            if choice == 'Exit game':
                game_over = True
            elif current_room == 'start' and choice == 'Enter the maze':
                current_room = 'room1'
            elif current_room == 'room1':
                if choice == 'Go through the left door':
                    current_room = 'room2'
                elif choice == 'Go through the middle door':
                    current_room = 'treasure_room'
                elif choice == 'Go through the right door':
                    current_room = 'room2'
                elif choice == 'Go back':
                    current_room = 'start'
            elif current_room == 'room2':
                if choice == 'Go left':
                    current_room = 'exit'
                elif choice == 'Go right':
                    current_room = 'treasure_room'
                elif choice == 'Go back':
                    current_room = 'room1'
            elif current_room == 'treasure_room':
                if choice == 'Take some treasure':
                    current_room = 'room2'
                elif choice == 'Leave the treasure room':
                    current_room = 'room1'
                elif choice == 'Go back':
                    current_room = 'room1'
            elif current_room == 'exit':
                if choice == 'Exit game':
                    game_over = True
    else:
            print("Invalid choice number. Please choose a valid option.")
else:
    print("Invalid input. Please enter a valid choice number.")
    print("What you expected to happen didn't happen.")
        
#Saves the game before exiting
save_game_state(current_room)



