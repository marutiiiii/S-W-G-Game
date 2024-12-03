# snake water gun game

'''
1 snake
-1 water
0 gun
'''
import random

computer=random.choice([1,0,-1])                         #comp can choose random input
youstr=(input("enter your string"))
youdict={"s": 1,"w": -1, "g": 0}                        #here the key should be input 
reversedict={1:"snake",-1:"water",0:"gun"}
you=youdict[youstr]                                      #to assign the input to the you 



if(computer == you):
    print("draw")
else:
    if(computer==1 and you==-1):
        print("you lose")
    elif(computer==1 and you==0):
        print("you won")
    elif(computer==-1 and you==1):
        print("you win")   
    elif (computer==-1 and you==0):
        print("you lose")
    elif (computer==0 and you==-1):
        print("you win")
    elif (computer==0 and you==1):
        print("you lose")
    else:
        print("something went wrong")
            
            
             

