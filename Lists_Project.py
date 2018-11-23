import random

def shopping():
    total_items = []
    while 1==1:
        current_item = input("What item would you like to add to the shopping cart:")
        total_items.append(current_item)
        keep_shopping = input("type 1 to keep shopping, type 2 to checkout: ")
        if int(keep_shopping) == 2:  #has a simple while loop that repeats forever
            print("You Bought")      #adds whatever you type to a list
            for x in total_items:    #prints the list through an if statement if the user wants to leave
                print(x)
            break

def is_prime(n):
    list = []
    for x in range(1,n+1):                  #two for loops, one looks through every number including and less than n
       is_prime = 0                         #the other looks through every number lower than all the numbers lower than n
       for y in range(1,x+1):               #the if statement checks if the y divides into x evenly
           if float(x)%float(y) == 0.0:     #because this includes 1 and itself if its prime it will be true twice
               is_prime += 1                #thats why is_prime exists
       if is_prime == 2:                    #if is_prime is equal to two than x is saved to list.
           list.append(x)
    return list

def roll_dice(n):
   r1 = 0
   r2 = 0
   r3 = 0
   r4 = 0           #six variables for each player
   r5 = 0
   r6 = 0
   for x in range(0,n):
       roll = random.randint(1,6)               #randomly chooses a player and adds one to that player variable
       if roll == 1:
           r1 += 1
       elif roll == 2:
           r2 += 1
       elif roll == 3:
           r3 += 1
       elif roll == 4:
           r4 += 1
       elif roll == 5:
           r5 += 1
       elif roll == 6:
           r6 += 1
   print("1 was rolled " + str(r1) + " times")
   print("2 was rolled " + str(r2) + " times")
   print("3 was rolled " + str(r3) + " times")      #prints out the end value of every variable
   print("4 was rolled " + str(r4) + " times")
   print("5 was rolled " + str(r5) + " times")
   print("6 was rolled " + str(r6) + " times")

def pivotList(inList, number):
   inList.sort()
   new_list = []
   for x in range(0,len(inList)):           #first sorts the list and then runs a for loop as many times as the list is long
       if inList[x] < number:               #checks every number in the list, if it is lower than the set number than adds that number to a new list
           new_list.append(inList[x])
   return new_list                      #returns list

def largestValue(inList):
   inList.sort()                    #sorts the list from highest to lowest and then returns the last number in the list
   return inList[len(inList)-1]

def mergeList(list1,list2):
   list3 = list1 + list2             #first adds the list into one larger list
   index_number = 0
   for x in range(1,max(list3) + 1):        #creates two for loops, one cycles through every number from 1 to the highest number in the list
       for y in range(0,len(list3)):        #the other cycles as many times as the list in long. if x ever equals y it will delete the number that is
           if x == list3[y]:                #already there and put in the new number. by going over the entire list it should re order them
               del list3[y]
               list3.insert(index_number,x)         #index number inceases by one so numbers that have already been checked arent rechecked or deleted.
               index_number += 1
   return list3

def dice():
    p1 = []
    p2 = []
    p3 = []
    p4 = []
    player_info = [p1,p2,p3,p4]
    input("Would you like to begin the game: ")
    while 1 == 1:
        print("The dice has rolled for all players")
        p1.append(random.randint(1,7))
        p2.append(random.randint(1,7))
        p3.append(random.randint(1,7))
        p4.append(random.randint(1,7))
        print("p1 role history is " + str(player_info[0]))
        print("p2 role history is " + str(player_info[1]))
        print("p3 role history is " + str(player_info[2]))
        print("p4 role history is " + str(player_info[3]))
        if input("Would you like to start again: ") == "yes":
            print()
        else:
            break
def tic_tac_toe():
    player1 = 0
    player2 = 0
    board = ["~","~","~"],["~","~","~"],["~","~","~"]

    print("INSTRUCTIONS: ")
    print("The Goal is to get 3 across, down, or diagonaly")
    print("You will input 2 numbers with no spaces")
    print("the first number is rows, the second number is columns")
    print("for example: 23 wich would be the middle right square")
    print("p1 is X's. p2 is O's")

    for x in range(0,9):
        player1 = str(input("Input square for player 1: "))
        player2 = str(input("Input square for player 2: "))
        board.instert([int(player1[0])][int(player1[1])],"X")
        board.instert([int(player2[0])][int(player2[1])], "O")
        print("the current board is: ")
        print(board[0][0],board[0][1],board[0][2],"\n" + board[1][0],board[1][1],board[1][2],"\n" + board[2][0],board[2][1],board[2][2])

shopping()
print(is_prime(34))
roll_dice(6)
print(pivotList([1,4,6,7,3,6,3,5,7], 5))
print(largestValue([1,5,3,3,5,6,4,4,6,7,72,12]))
print(mergeList([23,45,21,57,23],[23,54,12,6,32]))
dice()