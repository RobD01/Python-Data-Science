# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:26:18 2022

@author: medbz
"""

import random
from hangman_words import words
import string 

def getvalidword(words):
    word = random.choice(words)
    while '_'in word or ' ' in word:
        word = random.choice(words)
                
    return word.upper()
    
def hangman ():
    word = getvalidword(words)
    wordletter = set(word) 
    alphabet = set(string.ascii_uppercase)
    usedletter = set()
    lives = 6
    while len(wordletter) > 0 and lives > 0:
        print('You have used the following letters: ',' '.join(usedletter) )
        wordlist = [letter if letter in usedletter else '-' for letter in word]
        print('Current word: ',' '.join(wordlist))
        print(f'Lives remaining: {lives}')
        userletter  = input('Guess a letter. (Enter END to end the game) : ').upper()
        if userletter == 'END':
            lives = 0
            print ('LOL, Wuss... Ending Game...')
            
        elif userletter == 'HELP':
            print (f'You\'re a cheater! The answer is: {word}')
        elif userletter in alphabet - usedletter:
            usedletter.add(userletter)
            
            if userletter in wordletter:
                wordletter.remove(userletter)
                print('That is a correct letter')
            else:
                print(f'That is not a correct letter')
                lives = lives - 1
        elif userletter in usedletter:
            print('You have already used this letter')

        else:
            print('Invalid character. Try again')

    if lives == 0:
         print(f'You died. X___X . The word was {word} ')
    else:
         print(f'You won! You guessed the word: {word} ')
        
    print("""
                                                                                          
             Thanks for playing: Here's a Doge:
                                                                   
               ...                                   */*                        
              (#((((/*      SUCH HANG               (((*                        
             .###(/////*                          ,((((/                        
             (##(((((((((/                      */((((//.     MUCH GAME         
             (((####(#(((#(//,.. .**////////*//*******/((                       
             ((((%%%%%##((##(((#///*******//////////********                    
              (((#%&&%#((((#%#////////*////////((//****,,,,*,,*,        
              ((/(#%&&@%(((#/*///////////////////(/***,,,,,***,,,,,,.    W      
             .(##(((#%&##(//*//*////////******////(//**,,**,***,,,,,,,.  O      
             *((((((((//****///////////*******,*/(////***//(%%#**,,,,*,  W      
           ,*/(##((//******/*///////*/***/*/*****///******&#&%&/*,....,,        
           */(##(//******/****/////((%@@&(#&((///**********%&&&(/,,....,        
           *///(///***********/**//#&&&&@@(/&&%#(/**,,,,***********......       
           //////************,,,,****/###%#%%(///***,*,,,,,,,,,,,*,......       
          ,////*******,,*,**,,,,,,*******////********,,,***//(((#(*.......      
         .***/********,,,,,,,,,,,,**********,******,,,,,*#&&@@@@@@&&&.......    
        ,****///*******,,,,,,,,,,,,,,,,,,,,,,,*****,,,,*/%&@@@@@@&&%(*...,...   
        ***//////*/**********,,,,,,,,,,,,,*********/*///*(%&@@@&@&&&#/*,,*,..   
       **/////////****************,*,**************/*//**/(#%&&&&&%%%(**,...    
       */////////////************************///***//////##%%%%&&@&&#/*,,..,    
      **//////////*******,,*****************//%%%##(///((%&&&&&&&&%%/,,,,,.     
     */////////////***************************/((#####%&%%%%%%%%%#/**,,,,,.     
     /////((((///////*/**************************///((/////(((((/****,,,.,      
    *//////((((((/////////******,**********////////*//*********,,*,*,,,,,.      
   ***//////((((#((/////********************/////**/***/**********,*,,,,,       
    ***///////((((((////////**********,****/////*//**//*****************,       
    ,******/////((((/(//***************//*/////////*******************,,,       
    .*************////////***//******///////////////*/*******//******,,,,,      
    .***********************************///////((/((/////////******,,,,,,,.     
    *************,,***,************//*******////////////////*****,*,,,,,,,,.    
    *****,,,,,,,****,,**,*****//************/**/////////**//******,,,,,....,    
                                                                                
                                                                                
          """)         

            
hangman()
