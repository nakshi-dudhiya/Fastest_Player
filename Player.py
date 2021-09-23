""" This file consists of Assignment 1A
- Nakshi Dudhiya
  Mohawk College
Date: Sept 22, 2021
"""

import numpy as np
import time

def play():
    """This function collects the name of the players and the number of time intervals the player wants to play.
    It calculates the timing for each interval for each player. Later it displays the mean time, the fastest time interval and the slowest time interval"""

    #creating a set
    lst= set()

    #number of players for list
    count= int(input("How many players: "))

    #number of time intervals
    interval= int(input("How many time intervals:"))

    #Entering names in the list
    i=0
    print("Enter ",count," names for the players:")
    while i < count:
        name= str(input()).strip().capitalize()
        if name in lst:
            print(name," already exists. Enter again")
            continue
        elif(len(name)== 0):
            print("Name cant be empty. Enter again.")
            continue
        else:
            lst.add(name)
            i +=1
    print("Let's Play")

    # Creating a 2D array to store the time interval
    timeslot = np.ones((count, interval))

    #calculating the time interval for each player
    y= 0
    for i in lst:
        print(i,"'s turn. Press enter quickly:")
        x= 0
        timelst=[]
        while x< interval:
            input()
            time1 = time.time()
            input()
            time2 = time.time()
            x +=1
            timelst.append(time2 - time1)
        timeslot[y]= timelst
        y+=1


    #Converting the list to array
    lst = list(set(lst))
    players = np.array(lst)

    # Displaying the parallel arrays alphabetically
    s= players.argsort()
    players = players[s]
    print(players)
    timeslot = timeslot[s,]
    print(timeslot)


    #Output of the program
    print("Mean Times:", timeslot.mean(axis=1))
    avg =timeslot.mean(axis=1)
    print("Fastest average time: ", round(avg.min(),3) ," by ",players[avg.argmin()]  )
    print("Slowest average time: ", round(avg.max(),3) ," by ",players[avg.argmax()] )
    print("Fastest Single time: ", round(timeslot.min(),3), " by ", players[np.where(timeslot == timeslot.min())[0]])
    print("Slowest Single time: ", round(timeslot.max(),3), " by ", players[np.where(timeslot == timeslot.max())[0]])


