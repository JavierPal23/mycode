#!/usr/bin/env/ python3
""" TLG | Javier Palacios
    Camping Simulator"""


def showInstructions():

  #print a main menu, map and the commands
  print('''
Camping Simulator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Map:
          ----------
          |Hill-Top|
          ---------- 
               ^
               |                           north
------    -----------    ------              ^
|Lake|<---|Camp-Site|--->|Cave|              |
------    -----------    ------      west<---|--->east
               ^                             |
               |                           south
          -----------    -----
          |Tree-Line|<---|Car|
          -----------    -----
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Commands:
  hike [direction]
  get [item]
  build [object]
  tear down [object]
''')

def showStatus():

  #print the camper's current status
  print('---------------------------')
  print('You are at the ' + currentSite)

  #print the current inventory
  print('Inventory : ' + str(inventory))

  #print an item if there is one
  if "item" in sites[currentSite]:
    print('You see a ' + sites[currentSite]['item'])
  print("---------------------------")

  #print an object if there is one
  if "object" in sites[currentSite]:
    print('You see a ' + sites[currentSite]['object'])
  print("---------------------------")


# an inventory, which is initially empty
inventory = []

## A dictionary linking a site to other sites
sites = {

            'Car' : {
                  'west'   : 'Tree-Line',
                  'item'   : ['gun','lighter','food'],
                  'object' : 'tent',
                },
            'Tree-Line' : {
                  'east' : 'Car',
                  'north': 'Camp-Site',
                  'item' : 'fire-wood',
                },
            'Camp-Site' : {
                  'south' : 'Tree-Line',
                  'west'  : 'Lake',
                  'east'  : 'Cave',
                  'north' : 'Hill-Top',
                  'item'  : '550 cord',
                  'object': 'camp-fire',
               },
            'Lake' : {
                  'east' : 'Camp-Site',
                  'item' : 'fishing pole',
               },
            'Cave' : {
                  'west' : 'Camp-Site',
               },
            'Hill-Top': {
                  'south': 'Camp-Site',
                  'item' : 'binoculars',
               },
         }

#start the camper in the car
currentSite = 'Car'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
