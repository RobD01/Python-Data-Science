# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 20:02:42 2022

@author: medbz
"""
import random

welcome = "Let's play tic tac toe! You're X , and Computer is O ... "

move = [0,1,2,3,4,5,6,7,8]
available = move.copy()
tauntlist = [
        "Now dig on this",
        "You’re Trash Brock",
        "See ya chump",
        "I'm gonna put some dirt in your eye",
        "You want forgiveness? Get religion!",
        "Get me some milk. You got any with nuts? Go make me some",
        "I missed the part where thats my problem"
        ]



def game ():
    
    board = f"""
    |{move[0]}|{move[1]}|{move[2]}|
    |{move[3]}|{move[4]}|{move[5]}|
    |{move[6]}|{move[7]}|{move[8]}|
    
    """
    
    print (welcome)
    print (board)
    print (f"""
List of moves:  
       {move}
       """)
   
    
    while len(available) > 0:
        
        
        playermove()
        computermove()
        print (f"Move History: {move}")
        print (f"Available moves: {available}")
        
        board = f"""
    |{move[0]}|{move[1]}|{move[2]}|
    |{move[3]}|{move[4]}|{move[5]}|
    |{move[6]}|{move[7]}|{move[8]}|
    
    """
        
        print (board)
        winner()
    
    ending()
    
 
    

def playermove () :    
    try:
        if len(available) > 0:
            xmove = input('Enter a number 0-8 to make a move (or END to quit game) : ').upper()
            if xmove == 'END':
                    print (f'Ending Game... {random.choice(tauntlist)}')
                    available.clear()
        
            elif int(xmove) in available: 
                available.remove(int(xmove))
                print (f"""
You have moved to space # {xmove}""")
                move[int(xmove)] = "X"
                
        else:
            pass
    
    except:
        print ("Invalid move. Lost your turn! ")

def computermove():
    if len(available) > 0:
        omove = random.choice(available)
        taunt = random.choice(tauntlist)
        print (f'Computer has moved to space # {omove}')
        move[int(omove)] = "O"
        available.remove(int(omove))
        print (f"""Computer says: {taunt}
        """)
    else:
        pass

def winner ():
            
        row = [[move[0],move[1],move[2]],[move[3],move[4],move[5]],[move[6],move[7],move[8]]]
        col = [[move[0],move[3],move[6]],[move[1],move[4],move[7]],[move[2],move[5],move[8]]]
        diagonal= [[move[0],move[4],move[8]],[move[2],move[4],move[6]]]
        
        if len(set(row[0])) == 1 or len(set(row[1])) == 1 or len(set(row[2])) == 1 or \
        len(set(col[0])) == 1 or len(set(col[1])) == 1 or len(set(col[2])) == 1 or \
        len(set(diagonal[0])) == 1 or len(set(diagonal[1])) == 1:
            print("Winner!")
            available.clear()
        
        

def ending():
    print("""Game over. Thanks for playing.
          Here's a cat:
              .  .  .. ..  .  .. ..  .  .  .. ..  .  .  .. ..  .  .. ..  .  .  .. ..  .  .  .
  .. ..  .  .. ..  .  .  .. ..  .  .. ..  .  .  .. ..  .  .  .. ..  .  .. ..  . 
  .. ..  .  .. ..  .  .  .. ..  *&... ..  .  .  .. ..  .  .  .. ..  .  .. ..  . 
 .  .  .. ..  .  .. ..  .  .  .(&%&  .  .  .. ..  .  .. ..  .  .  .. ..  .  .. .
 .  .  .. ..  .  .  ..  .  .  %&%&&. .  .  .. ..  .  .. ..  .  .  .. ..  .  .  .
  .. ..  .  .. ..  .  .  .,/((((##&&. ..  .  .  .. ..  .  .  .. ..  .  .. ..  . 
  ..  .  . .,. ..  .  /*/*(###%%%%%%% ..  .  .  .. ..  .  .  .. ..  .  .. ..  . 
 .  .  .. ,&#####%%%#(/(###%((%&&&&%&&%..  .. ..  .  .. ..  .  .  .. ..  .  .  .
 .  .  .. ..%%%#(%%(*/(%%&&&%**(&@&&&&%#*  .. ..  .  .. ..  .  .  .. ..  .  .  .
  ..  .  .  ..(%%&#//(%%/&%#&(*/(////((#((.  .  .. ..  .  .  .. ..  .  .. ..  . 
  .. ..  .  .. ..@%((#%%%&&&#/**///(((((//// .  .. ..  .  .  .. ..  .  .. ..  . 
                  ///((###(((**/**//*/*//////(                  .               
 .  .  .. ..  .  ..**////////*,,***********///((  .  .. ..  .  .  .. ..  .  .. .
..  .  .. ..  .  .. ,,,,,,,,,,,***,,,*,*****////((.  .. ..  .  .  .. ..  .  .  .
  .. ..  .  .. ..  .,,,,,,,,,,,**,*******/////////(#.  .  .  .. ..  .  .. ..  . 
  .. ..  .  .. ..  . ,,,,,,***,,,,******////////////(  .  .  .. ..  .  .. ..  . 
..  .  .. ..  .  .. .**,*,,*************//////(/****/(* ..  .  .  .. ..  .  .  .
 .  .  .. ..  .  .. .*//((((////*****/*////(//(/*,**/(( ..  .  .  .. ..  .  .. .
  ..  .  .  .. ..  ../(#%###/(///****////////*/(/***/(((  .  .. ..  .  .. ..  . 
. .. ..  .  .. ..  .*/(#%#(#((///****,////////((***//((((*.  .. ..  .  .. ..  . 
 .  .  .. ..  .  . .,*//((((//*/(/******//(///((#/((((((((  .  .  .. ..  .  .  .
 .  .  .. ..  .  ..,**//(##**/*/*/*****/////(((((######(#.  .  .  .. ..  .  .  .
    """)        
            

game ()


