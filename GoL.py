# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
import random

x = y = 35
population = [[0 for n in range(x)] for m in range(y)]
# population = [[1,0,0,1,1],[0,1,1,0,0],[1,1,0,0,0],[1,0,1,1,0],[0,0,1,1,0]]
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def initPopulation():
    for n in range(x):
        for m in range(y):
            population[n][m] = random.randint(0,1)
 
def displayPopulation():
    for n in range(x):
        for m in range(y):
            if(population[n][m] == 1):
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print("")

def countLiveNeighbout(cx,cy):
    liveNeighbour = 0
    if(cx-1>=0 and cy-1>=0):
        liveNeighbour += population[cx-1][cy-1]
        # print("a",liveNeighbour)
    
    if(cx-1>=0):
        liveNeighbour += population[cx-1][cy]
        # print("b",liveNeighbour)
    
    if(cx-1>=0 and cy+1<y):
        liveNeighbour += population[cx-1][cy+1]
        # print("c",liveNeighbour)

    if(cy-1>=0):
        liveNeighbour += population[cx][cy-1]
        # print("d",liveNeighbour)

    if(cy+1<y):
        liveNeighbour += population[cx][cy+1]
        # print("e",liveNeighbour)

    if(cx+1<x and cy-1>=0):
        liveNeighbour += population[cx+1][cy-1]
        # print("f",liveNeighbour)

    if(cx+1<x):
        liveNeighbour += population[cx+1][cy]
        # print("g",liveNeighbour)
    
    if(cx+1<x and cy+1<y):
        liveNeighbour += population[cx+1][cy+1]
        # print("h",liveNeighbour)

    return liveNeighbour

def runIteration():
    for n in range(x):
        for m in range(y):
            liveNeighbour = 0
            liveNeighbour = countLiveNeighbout(n,m)
            # print(liveNeighbour, end = " ")
            if(population[n][m] == 1):
                if(liveNeighbour<2):
                    population[n][m] = 0
                elif(liveNeighbour == 2 or liveNeighbour == 3):
                    population[n][m] = 1
                else:
                    population[n][m] = 0
            else:
                if(liveNeighbour == 3):
                    population[n][m] = 1
        # print("")                

initPopulation()
# displayPopulation()
# countLiveNeighbout(1,0)
# runIteration()
while (1):
    clear()
    runIteration()
    displayPopulation()