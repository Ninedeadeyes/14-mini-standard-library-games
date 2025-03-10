# There is an explanation of what a dictionary and nested dictionary are at the very bottom. 

def showInstructions():
    print('''
                    The Haunted House

Escape the house with its riches but beware of the evil undead !!  

Commands:  

  use [item] eg: use key 
  
  shoot[monster] eg: shoot zombie
   
  go [direction] eg: go south
  
  get [item] eg: get bandage
  
  commands ( To view a list of commands) 

''')
    
health= 100

def showStatus():

  print('You are in the ' + currentRoom)
  print (rooms[currentRoom]['desc'])
  print("Inventory : " + str(inventory))
  print("Your health is",health)
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

inventory = []

monster=[]

rooms = {

            'Hall' : {'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  "north":"Bed Room",
                  'item'  : 'shotgun',
                  'monster'  : '', "desc":"No one has been here for a while",
                },        

            'Kitchen' : { 'north' : 'Hall',
                  "item":"golden_crown",
                  'monster'  : 'zombie',"desc":"Dead bodies scatter the floor",                        
                },
                
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'key',
                  'monster'  : 'zombie',"desc":"Old painting hangs on the wall",    
                },
                
            'Garden' : { 'north' : 'Dining Room',
            'monster'  : '', "desc": "There is a locked gate here",
                },

        'Bed Room' : {'south' : 'Hall',
            'item'  : 'bandage',
            'monster'  : 'ghoul',"desc":"There is blood all over the bed ",  
              },        
         }

currentRoom = 'Hall'

showInstructions()

while True:

  showStatus()                  # Everytime it refresh it will show you up to date status 

  move = ''
  while move == '':  
    move = input('>')           # If you click enter with no command it will just ask for input  
    
  move = move.lower().split()   # lower case everything and split will turn a string into a list hence  ' get shotgun' = move =[get,shotgun]

  if move[0]=="shoot":    # acquire the value from index 0 of the list of 'move'. In this case if it is shoot 

      if "monster"in rooms[currentRoom] and move[1] in rooms[currentRoom]['monster'] and "shotgun" in inventory :
          del rooms[currentRoom]['monster']
          print( "you killed the", move[1])
          rooms[currentRoom].update({"monster":"dead"},)  #update merge dictionary with an iterable of key value pair
        
      else:
          print("you cannot attack " )
          
  if move[0]=="use":
      
      if "bandage" in inventory and move[1]== "bandage":
          heal=40
          health=min(100,health+heal)
          inventory.remove("bandage")
          print("you recovered 40 health (max 100)")

      elif "key" in inventory and move[1]== "key" and "golden_crown" in inventory and currentRoom=="Garden":     
         print("you escape with the loot, you retire in style, you win!!  ")
         input("Press Enter to Exit")
         break    
              
          
      elif "key" in inventory and move[1]== "key" in inventory and currentRoom=="Garden":
         print("you escape the house but die a pauper, you lose ")
         input("Press Enter to Exit")
         break

      else:
          print("can't use that")

  if move[0] == 'go':
      if move[1] in rooms[currentRoom]:
          currentRoom = rooms[currentRoom][move[1]]    # acquire the new room (the nested value) from the 'direction'(the nested key) 
                                                       #eg rooms[Dining room][west] return value Hall  because   'Dining Room' : { 'west'  : 'Hall', within rooms dictionary   hence currentRoom=Hall
      else:
          print('You can\'t go that way!')

  if move[0] == 'get':
    if 'item' in rooms[currentRoom] and rooms[currentRoom]['item'] == move[1]:  # move[1] is whatever you type  '== move[1]'  make sure you are typing correctly before gaining the item. 
        inventory += [rooms[currentRoom]['item']]
        print(rooms[currentRoom]['item'] + ' got!')
        del rooms[currentRoom]['item']
    else:
        print("Can't get that")
  
  if move[0] == 'commands':
    print('''
Commands:  

  use [item] eg: use key 
  
  shoot[monster] eg: shoot zombie
   
  go [direction] eg: go south
  
  get [item] eg: get bandage
  
  commands ( To view a list of commands) 

''')
        
  if 'zombie' in rooms[currentRoom]['monster']:
      print("A zombie attacks you !!!")
      health=health-30

  if 'ghoul' in rooms[currentRoom]['monster']:
      print('A ghoul attacks you !!!')
      health=health-20
  

  if health <= 0:
      print("you are dead")
      input("Press Enter to Exit")
      break



#            MAP LAYOUT 

#            BedRoom
#              ^
#             Hall     >        Dining Room
#              v                   v
#            Kitchen   ||        Garden  


 # A Dictionary will have a value and a key and you will be able to 'extract the 'value from the key.  

#computer = {
#"brand": "NES",
#"model": "Blue",
#"year": 1994 }

#print computer[model]  will print 'Blue'  so in conclusion  dictionary[key] to extract the value 

# Nested Dictionary 

# You can also have a Dictionary within a Dictionary and that is called a 'Nested Dictionary 
# For example within the above game if you are if current Room is in 'Hall' and you instruct to 'go north' current Room will change to Bed Room 
# because the code currentRoom = rooms[currentRoom][move[1]]  will equate to rooms[Hall][north] and the 'value' of the nested key 'north' is 'Bed Room
# hence currentRoom becomes 'Bed Room'. So in conclusion  dictionary[key][nested key] to extract nested value 



#

#https://github.com/Ninedeadeyes/15-mini-python-games-
