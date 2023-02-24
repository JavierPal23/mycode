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
''')

def showStatus():

  #print the camper's current status
  print('---------------------------')
  print('You are at the ' + currentSite)

  #print the current inventory
  print('inventory : ' + str(inventory))

  #print an item if there is one
  if "item" in sites[currentSite]:
    print('You see a ', sites[currentSite]['item'])
  print("---------------------------")

  #print an object if there is one
  if "object" in sites[currentSite]:
    print('You see a ', sites[currentSite]['object'])
  print("---------------------------")


# an inventory, which is initially empty
inventory = []

## A dictionary linking a site to other sites
sites = {

            'Car' : {
                  'west'   : 'Tree-Line',
                  'item'   : 'gun',
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
                  'item' : 'bigfoot',
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
  move = move.lower().split(" ", 1)

  



  #if they type 'hike' first
  if move[0] == 'hike':

    #check that they are allowed wherever they want to go
    if move[1] in sites[currentSite]:

      #set the current site to the new site
      currentSite = sites[currentSite][move[1]]
    #there is no link to the new site
    else:
        print('You can\'t hike that way!')





#if they type 'get' first
  if move[0] == 'get' :

      #if the site contains an item, and the item is the one they want to get
    if "item" in sites[currentSite] and move[1] in sites[currentSite]['item']:


    #if the site contains an object, and the object is the one they want to get
      if "object" in sites[currentSite] and move[1] in sites[currentSite]['object']:

      #add the item/object to their inventory
        inventory += [move[1]]

      #display a helpful message
      print(move[1] + ' got!')

      #delete the item from the site
      del sites[currentSite]['item']

      #delete the object from the site
      del sites[currentSite]['object']

    #otherwise, if the item/object isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')





#if they type 'build'
  if move[0] == 'build' :

      #if object is in inventory then camper can use build command
   if "object" in inventory :

     #display message that object was built
     print(move[1] + ' built!')

     #remove object from their inventory
     inventory -= [move[1]]

 



## If camper shoots the mountain lion and fishes he wins the game
  if currentSite == 'Hill-Top' and 'gun' in inventory :
    print('You shot the mountain lion!')

  if currentSite == 'Lake' and 'fishing pole' in inventory :
    print('You caught dinner!')
    break

  ## If camper enters the cave with bigfoot
  elif 'item' in sites[currentSite] and 'bigfoot' in sites[currentSite]['item']:
    print('Play bigfoot Rock, Paper, Scissors to not become his dinner! ')
    




    break
