#!/usr/bin/python3
"""
   1.The PRC game has Hall, Kitchen, Library, Dinning Room, Garden rooms
   2.Every room can enter the neighbour room by command [go direction]
   3.Every room has their own item, like key, sword, portion, books, monster, 
   4.Collect all books in Library will win, or escape the house with key and portion will win, or you have a sowrd
     to defeat the monster possibly.  
   5.Kitchen has monster in it. If you have a sword when you meet monster, you will have two option: 
    a. fight: You can select a hero, system would ramdon generate a mosnter to combat with you. 
        There will be health and damge value calculation to determin if you defeat or die
        you also can select run, there also be a function to determin if you successfully escape or failed.
    b. Run Away: You can select 1 in 4 doors to escpae, but be careful, the wrong selection will make you died. 
   
   Enjoy the game!!!!
   """
import random
import sys

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('Your current location is ' + currentRoom)
    print(roomDescriptions[currentRoom]) # Added room description

    # print what the player can see in each direction
    for direction in rooms[currentRoom]:
        if direction != 'description' and direction != 'item':
            print('To the ' + direction + ' is ' + roomDescriptions[rooms[currentRoom][direction]])

    # print what the player is carrying
    print('Inventory:', inventory)

    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ',  rooms[currentRoom]['item'])

    print('Your total move is ', move_count)
    print("---------------------------")

#the player has collected all the books in the Library.
def win():
    global books  # declare books as global
    if set(books) <= set(inventory):
        print('You collected all the books! You win!')
        return True
    else:
        return False

# allows the player to flee from the monster.
def runAway():
    """Player runs away from the monster"""
    global currentRoom  # declare currentRoom as global
    print("You run away from the monster and hide in the nearest room.")
    # move the player to a random neighboring room
    if diabolical_puzzle(): 
        directions = [d for d in rooms[currentRoom].keys() if d not in ['description', 'item']]
        currentRoom = rooms[currentRoom][random.choice(directions)]
    else: 
        sys.exit(0)

def diabolical_puzzle():
    print("Welcome to the diabolical puzzle!")
    print("You are trapped in a room with four doors.")
    print("Only one door will lead you to safety, the others lead to certain doom.")
    
    # Generate a random number between 1 and 4
    correct_door = random.randint(1, 4)
    
    # Get the player's guess
    guess = input("Which door do you choose (1, 2, 3, or 4)? ")
    guess = int(guess)
    
    # Check if the guess is correct
    if guess == correct_door:
        print("Congratulations! You have chosen the correct door and escaped to safety.")
        return True
    else:
        print("Oh no! You have chosen the wrong door and fallen into a pit of spikes. You are dead.")
        return False

# Monster class definiation    
class Monster:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.damage = damage
        self.speed = speed

# Plyaer class definition
class Player:
    def __init__(self, name, max_health, damage, level, speed):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.damage = damage
        self.level = level
        self.speed = speed
    
    def attack(self, monster):
        damage = random.randint(1, self.damage)
        print(f"{self.name} attacks {monster.name} for {damage} damage!")
        monster.health -= damage
        if monster.health <= 0:
            self.level_up(monster)
            return True
        else:
            return False
    
    def take_damage(self, monster):
        damage = random.randint(1, monster.damage)
        print(f"{monster.name} attacks {self.name} for {damage} damage!")
        self.health -= damage
        if self.health <= 0:
            return True
        else:
            return False
    
    def level_up(self, monster):
        print(f"{self.name} has defeated {monster.name} and gained {monster.speed} speed!")
        self.speed += monster.speed
        if self.speed >= 100:
            self.level += 1
            self.speed = self.speed - 100
            self.max_health += 5
            self.damage += 2
            print(f"{self.name} has leveled up! You are now level {self.level}.")
            print(f"Max Health: {self.max_health}, Damage: {self.damage}")
            self.health = self.max_health


def generate_player():
    name = input("Please select your favorite hero from this list \n \"Iron Man\",\"Captain America\", \"Thor\",\"Black Widow\",\"Hulk\" \n")
    name = name.title()
    if name in players.keys():
        max_health =  players[name]['health']
        damage =  players[name]['damage']
        level = players[name]['level']
        speed = players[name]['speed']
        return Player(name, max_health, damage, level, speed)
    else:
        generate_player()

def generate_monster():
    monster_names = ['Goblin', 'Orc', 'Troll', 'Dragon']
    name = random.choice(monster_names)
    max_health = random.randint(30, 80)
    damage = random.randint(3, 12)
    speed = random.randint(15, 25)
    return Monster(name, max_health, damage, speed)
    

def combat():
    player = generate_player()
    monster = generate_monster()
    print(f"A wild {monster.name} appears!")
    while True:
        action = input("What will you do? (attack/run) ").lower()
        if action == "attack":
            if player.attack(monster):
                print(f"{player.name} has defeated {monster.name}!")
                break
            if player.take_damage(monster):
                print(f"{player.name} has been defeated by {monster.name}!")
                return False
        elif action == "run":
            if random.randint(1, 2) == 1:
                print(f"{player.name} has successfully fled from {monster.name}!")
                return True
            else:
                print(f"{player.name} could not escape from {monster.name}!")
                if player.take_damage(monster):
                    print(f"{player.name} has been defeated by {monster.name}!")
                    return False
        else:
            print("Invalid command!")

# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
books = ['book']

rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                },

            'Kitchen' : {
                  'south' : 'Library',
                  'north' : 'Hall',
                  'item'  : 'monster',
                },

            'Library': {
                'north': 'Kitchen',
                'item': books,
            },            

            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
               },

            'Garden' : {
                  'north' : 'Dining Room',
                  'item' : 'sword'
            },
        }

roomDescriptions = {
    'Hall': ' the hall. There are doors to the south and east.',
    'Kitchen': ' the kitchen. You can go north to the hall, go south to Library.',
    'Library': ' the Library, You can go north to the Kitchen.',
    'Dining Room': ' the dining room. There are doors to the west and south.',
    'Garden': ' the garden. You can go north to the dining room.'
}

#Heroes dictionary
players = {
    'Iron Man': {'name': 'Iron Man', 'health': 100, 'damage': 20, 'level' : 15, 'speed': 20},
    'Captain America': {'name': 'Captain America', 'health': 122, 'level' : 18, 'speed': 10},
    'Thor': {'name': 'Thor', 'health': 150, 'damage': 25, 'level' : 10, 'speed': 15},
    'Hulk': {'name': 'Hulk', 'health': 200, 'damage': 30, 'level' : 5, 'speed': 5},
    'Black Widow': {'name': 'Black Widow', 'health': 80, 'damage': 10, 'level' : 20, 'speed': 25}
}

# start the player in the Hall
currentRoom = 'Hall'
move_count = 0;

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()
    move_count += 1

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        
        if move[1] in rooms[currentRoom] :
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
                print("There's a monster blocking your path!")
                action = input("Do you want to (f)ight or (r)un? ")
                if action == 'f':
                    if 'sword' in inventory:
                        combat()
                        print("You defeat the monster with your trusty sword!")
                        del rooms[currentRoom]['item']
                    else:
                        print("You don't have anything to fight with! The monster kills you. GAME OVER!")
                        break
                elif action == 'r':
                    runAway()
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get':
        # check if there is an item in the room
        if 'item' in rooms[currentRoom]:
            # check if the item is the monster
            if 'monster' in rooms[currentRoom]['item']:
                print("There's a monster blocking your path!")
                action = input("Do you want to (f)ight or (r)un? ")
                if action == 'f':
                    if 'sword' in inventory:
                        combat()
                        print("You defeat the monster with your trusty sword!")
                        del rooms[currentRoom]['item']
                    else:
                        print("You don't have anything to fight with! The monster kills you. GAME OVER!")
                        break
                elif action == 'r':
                    runAway()
            else:
                # check if the item matches the player's request
                if move[1] in rooms[currentRoom]['item']:
                    # add the item to the player's inventory
                    inventory.append(move[1])
                    # remove the item from the room
                    del rooms[currentRoom]['item']
                    print(move[1] + ' got!')
                else:
                    print("There's no such item here.")
        else:
            print("There's no item in this room.")


    
    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    #alternative win or lose scenario
    if win():
        break
