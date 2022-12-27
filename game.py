import random
l = ["rock","paper","scissor"]

'''
rock vs paper = paper wins
paper vs scissor = scissor wins
scissor vs rock = rock
'''

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
    Game Start.......
    1. yes
    2. No || Exit     
       ''' ))
    if (uc == 1):
         for a in range(1,6):
            userInput= int(input('''
            
1.Rock
2.Paper
3.Scissor        
'''))
            if userInput == 1:
                  uchoice = "rock"            
            elif userInput == 2:
                  uchoice ="paper"
            elif userInput == 3:
                  uchoice = "scissor"
            Cchoice = random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User value",uchoice)
                print("Game Draw")
                ucount = ucount + 1
                ccount = ccount + 1
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("Userchoice",uchoice)
                print("Computer Choise",Cchoice)
                print("You Win")
                ucount = ucount+1
            else:
                print("Computer choice",Cchoice)
                print("User choice",uchoice)
                print("Computer Win")
                ccount=ccount+1
         if ucount == ccount:
           print("*****##>>>...Final Game Draw .................***")
           print("Computer Chount",ccount)
           print("User count",ucount)

         elif ucount < ccount:
            print("*****......Computer Win The GAME .................***")
            print("Computer Chount",ccount)
            print("User count",ucount)
    

         elif  ucount > ccount:
           print("******......User Win The Game .................***")
           print("Computer Chount",ccount)
           print("User count",ucount)
    else:
        break