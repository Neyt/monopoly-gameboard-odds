
def monop(finish,games): #finish is the number of rolls, and games the # of games
    

    #Im commenting this out so I can simplify code and input directly the finish and games:

    #finish = 10**finish_order #10 elevated to this number
    #games = 10**games_order #10 elevated to this number
     
    import random #imports code to be able to make randome choices.
    from random import shuffle
    print "line 9"#for debuging 
    squares = [] #creates and empty list to hold some numberes called squares
    runs_counter = 0 #I create a counter for the number of games before entering the loop
    while len(squares) < 40:# as long as this list is less than 40
        squares.append(0) #it will add at the end of the list 0 each time
     
    # roll values are values from a six by six grid for all dice rolls
    rollvalues = [2,3,4,5,6,7,3,4,5,6,7,8,4,5,6,7,8,9,5,6,7,8,9,10,6,7,8,9,10,11,7,8,9,10,11,12]
     
    games_finished = 0 #creates a counter for times the games finishes
     
    while games_finished < games: #as long as the counter is is less than what it was deffine initially in "games" (which is basically 10 elevate to the second variable)
         
        master_chest = [0,40,40,40,40,10,40,40,40,40,40,40,40,40,40,40] #creates a list called master chest. not sure why he uses those numbers
        chest = [i for i in master_chest] # creates al list called "chest" that will lookin into each number in "master chest"
        shuffle(chest) #then it shuffles the list "chest"
         
        master_chance = [0,24,11,'U','R',40,40,'B',10,40,40,5,39,40,40,40]
        chance = [i for i in master_chance]
        shuffle(chance)
         
        doubles = 0
         
        position = 0
         
        gos = 0

        runs_counter +=1 #everytime one finishes its counted
        print str(runs_counter)+" runs finished" #we turn the number into a text and then we printed in the screen 

        while gos < finish:
             
            diceroll = int(36*random.random())
             
            if diceroll in [0,7,14,21,28,35]:    # these are the dice index values for double rolls
                doubles += 1
            else:
                doubles = 0
            if doubles >= 3:
                position = 10
            else:
                 
                position = (position + rollvalues[diceroll])%40
                 
                if position in [7,22,33]:  # Chance
                    chance_card = chance.pop(0)
                    if len(chance) == 0:
                        chance = [i for i in master_chance]
                        shuffle(chance)
                    if chance_card != 40:
                         
                        if isinstance(chance_card,int):
                            position = chance_card
                        elif chance_card == 'U':
                            while position not in [12,28]:
                                position = (position + 1)%40
                        elif chance_card == 'R':
                            while position not in [5,15,25,35]:
                                position = (position + 1)%40
                        elif chance_card == 'B':
                            position = position - 3
                             
                elif position in [2,17]:  # Community Chest
                    chest_card = chest.pop(0)
                    if len(chest) == 0:
                        chest = [i for i in master_chest]
                        shuffle(chest)
                    if chest_card != 40:
                        position = chest_card
                         
                if position == 30: # Go to jail
                    position = 10
                     
                     
            squares.insert(position,(squares.pop(position)+1))
             
            gos += 1
         
        games_finished += 1
     

    print squares
    return squares
monop(60000,100) #put in here #of throws, and number of games
