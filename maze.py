import pickle

# Define scenarios I would recommend using dictionaries. Samantha, Do you want to do the dialogue for the rooms and choices? Keep room names the same though.
rooms = {
    'start': {
        'description': 
        'choices': 
    },
    'room1': {
        'description': 
        'choices': 
    },
    'room2': {
        'description': 
        'choices': 
    },
    'treasure_room': {
        'description': 
        'choices': 
    },
    'exit': {
        'description': 
        'choices': 
    }
}

#Game initialization below (Reference material: https://codereview.stackexchange.com/questions/159818/save-and-load-the-state-of-a-role-playing-game-using-pickle)

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

