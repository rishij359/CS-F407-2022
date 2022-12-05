#!/usr/bin/env python3
from Agent import * # See the Agent.py file
from pysat.solvers import Glucose3

class BFSElement:
    def __init__(self, i, j):
        self.i = i
        self.j = j
#   Only the functions FindCurrentLocation(), PerceiveCurrentLocation() andTakeAction() should be used
#   1xy represents that there is a mine at [x,y]
#   3xy represents that there is gold at [x,y]
def CtoKb(Clauses):
    Kb = Glucose3()
    for i in range(len(Clauses)):
        Kb.add_clause(Clauses[i])
    
    return(Kb)

def CheckForGold(Clauses):              #This function checks if the position of gold can be infered from the current knowledge base
    count = 0                           # If gold is found then the position of gold is returned
    pos = [0,0]                         # If we can infer that there is no gold then return [6,6]
    for x in range(2,5):                # If we can not infer anything about gold then return [0,0]
        for y in range(2,5):
            clause = 300 + (10*x) + y
            if(ask(Clauses,clause)):
                pos = (x,y)
                print('Gold is present in room', pos)
                return(True)

            elif(not ask(Clauses,-clause)):
                count = count + 1

    if(count == 9):
        pos == [6,6]
        return(False)
    
    return(False)

def ask(Clauses,clause):
    query = CtoKb(Clauses)
    query.add_clause([-clause])
    A = query.solve()
    query.delete()
    return(not A)

def AddPercept(Clauses,per,loc):
    if(loc[0] == 1):
        
        if(loc[1] == 1): # For the Block [1,1]
            
            if(per == 0):
                Clauses.append([-112])
                Clauses.append([-121])
            
            elif(per == 1):
                Clauses.append([-112,-121])
                Clauses.append([112,121])
            
            elif(per == 2):
                Clauses.append([112])
                Clauses.append([121])

        elif(loc[1] == 5): # For the Block [1,5]

            if(per == 0):
                Clauses.append([-125])
                Clauses.append([-114])
            
            elif(per == 1):
                Clauses.append([-125,-114])
                Clauses.append([125,114])
            
            elif(per == 2):
                Clauses.append([125])
                Clauses.append([114])

        elif(loc[1] == 2 or loc[1] == 3 or loc[1] == 4): # for [1,2] to [1,4]
            U = 100 + (10*loc[0]) + (loc[1] + 1)
            D = 100 + (10*loc[0]) + (loc[1] - 1)
            R = 100 + (10*(loc[0] + 1)) + loc[1]
            
            if(per == 0):
                Clauses.append([-U])
                Clauses.append([-D])
                Clauses.append([-R])

            elif(per == 3):
                Clauses.append([U])
                Clauses.append([D])
                Clauses.append([R])

            elif(per == 1):
                Clauses.append([U,D,R])
                Clauses.append([-U,-R])
                Clauses.append([-U,-D])
                Clauses.append([-R,-D])
            
            elif(per == 2):
                Clauses.append([-U,-D,-R])
                Clauses.append([U,D])
                Clauses.append([U,R])
                Clauses.append([R,D])

        return(Clauses)

    elif(loc[0] == 5):

        if(loc[1] == 1): # For the Block [5,1]
            
            if(per == 0):
                Clauses.append([-152])
                Clauses.append([-141])
            
            elif(per == 1):
                Clauses.append([-152,-141])
                Clauses.append([152,141])
            
            elif(per == 2):
                Clauses.append([152])
                Clauses.append([141])

        elif(loc[1] == 5): # For the Block [5,5]

            if(per == 0):
                Clauses.append([-145])
                Clauses.append([-154])
            
            elif(per == 1):
                Clauses.append([-145,-154])
                Clauses.append([145,154])
            
            elif(per == 2):
                Clauses.append([-145])
                Clauses.append([-154])

        elif(loc[1] == 2 or loc[1] == 3 or loc[1] == 4): # for [5,2] to [5,4]
            U = 100 + (10*loc[0]) + (loc[1] + 1)
            D = 100 + (10*loc[0]) + (loc[1] - 1)
            L = 100 + (10*(loc[0] - 1)) + loc[1]
            
            if(per == 0):
                Clauses.append([-U])
                Clauses.append([-D])
                Clauses.append([-L])

            elif(per == 3):
                Clauses.append([U])
                Clauses.append([D])
                Clauses.append([L])

            elif(per == 1):
                Clauses.append([U,D,L])
                Clauses.append([-U,-L])
                Clauses.append([-U,-D])
                Clauses.append([-L,-D])
            
            elif(per == 2):
                Clauses.append([-U,-D,-L])
                Clauses.append([U,D])
                Clauses.append([U,L])
                Clauses.append([L,D])

        return(Clauses)

    elif(loc[1] == 1):                          # for [2,1] to [4,1]
        L = 100 + (10*(loc[0] - 1)) + loc[1]
        R = 100 + (10*(loc[0] + 1)) + loc[1]
        U = 100 + (10*loc[0]) + (loc[1] + 1)

        if(per == 0):
            Clauses.append([-U])
            Clauses.append([-L])
            Clauses.append([-R])

        elif(per == 3):
            Clauses.append([U])
            Clauses.append([L])
            Clauses.append([R])
        elif(per == 1):
            Clauses.append([U,L,R])
            Clauses.append([-U,-R])
            Clauses.append([-U,-L])
            Clauses.append([-R,-L])
        
        elif(per == 2):
            Clauses.append([-U,-L,-R])
            Clauses.append([U,L])
            Clauses.append([U,R])
            Clauses.append([R,L])

        return(Clauses)

    elif(loc[1] == 5):                           # for [2,5] to [4,5]
        L = 100 + (10*(loc[0] - 1)) + loc[1]
        R = 100 + (10*(loc[0] + 1)) + loc[1]
        D = 100 + (10*loc[0]) + (loc[1] - 1)

        if(per == 0):
            Clauses.append([-D])
            Clauses.append([-L])
            Clauses.append([-R])

        elif(per == 3):
            Clauses.append([D])
            Clauses.append([L])
            Clauses.append([R])
        elif(per == 1):
            Clauses.append([D,L,R])
            Clauses.append([-D,-R])
            Clauses.append([-D,-L])
            Clauses.append([-R,-L])
        
        elif(per == 2):
            Clauses.append([-D,-L,-R])
            Clauses.append([D,L])
            Clauses.append([D,R])
            Clauses.append([R,L])

        return(Clauses)

    else:                                      #for middle 3x3 matrix
        L = 100 + (10*(loc[0] - 1)) + loc[1]
        R = 100 + (10*(loc[0] + 1)) + loc[1]
        D = 100 + (10*loc[0]) + (loc[1] - 1)
        U = 100 + (10*loc[0]) + (loc[1] + 1)

        if(per == 0):
            Clauses.append([-D])
            Clauses.append([-L])
            Clauses.append([-R])
            Clauses.append([-U])

        elif(per == 1):
            Clauses.append([U,D,L,R])
            Clauses.append([-U,-D])
            Clauses.append([-U,-L])
            Clauses.append([-U,-R])
            Clauses.append([-D,-L])
            Clauses.append([-D,-R])
            Clauses.append([-L,-R])

        elif(per == 2):
            Clauses.append([U,D,L,R])
            Clauses.append([U,D,L,-R])
            Clauses.append([U,D,-L,R])
            Clauses.append([U,-D,L,R])
            Clauses.append([U,-D,-L,-R])
            Clauses.append([-U,D,L,R])
            Clauses.append([-U,D,-L,-R])
            Clauses.append([-U,-D,L,-R])
            Clauses.append([-U,-D,-L,R])
            Clauses.append([-U,-D,-L,-R])

        elif(per == 3):
            Clauses.append([-U,-D,-L,-R])
            Clauses.append([U,D])
            Clauses.append([U,L])
            Clauses.append([U,R])
            Clauses.append([D,L])
            Clauses.append([D,R])
            Clauses.append([L,R])

        return(Clauses)

def IsSafe(M,i,j,Clauses):                  # Check if i and j are in the bounds and that M[i][j] = 2(Safe and Unvisited)
    if((i>=0 and i < 5) and (j>=0 and j<5)):
        if(M[i][j] == 2):
            return(True)

        else:
            return(False)

    else:
        return(False)

def IsBound(a,b):                           # Check if a and b are in the bounds

    if((a>=0 and a<5) and(b>=0 and b<5)):
        return(True)
    
    else:
        return(False)

def Scan(Clauses, M):                       # Check if we can any new Safe and Unvisited blocks and mark them with 2
    for i in range(5):
        for j in range(5):
            clause = 100 + (10*(i+1)) + j+1
            if(ask(Clauses,-clause) and (M[i][j] == 0)):
                M[i][j] = 2

    return(M)

def Traverse(ag,M,loc,Clauses,path):
    
    M = Scan(Clauses, M)
    i = loc[0] - 1
    j = loc[1] - 1
    A = False
    B = False
    C = False
    D = False
    
    if(IsSafe(M,i+1,j,Clauses)):                    #For Moving the agent Right
        ag.TakeAction('Right')
        path.append('Left')
        loc = ag.FindCurrentLocation()
        percept = ag.PerceiveCurrentLocation()
        Clauses = AddPercept(Clauses, percept,loc)
        if((CheckForGold(Clauses))):
            return(True, M, path)
        M[loc[0] - 1][loc[1] - 1] = 1
        A, M, path = Traverse(ag,M,loc,Clauses,path)
        if(A):
            return(True, M, path)
    
    if(IsSafe(M,i-1,j,Clauses)):                    #For Moving the agent Left
        ag.TakeAction('Left')
        path.append('Right')
        loc = ag.FindCurrentLocation()
        percept = ag.PerceiveCurrentLocation()
        Clauses = AddPercept(Clauses, percept,loc)
        if((CheckForGold(Clauses))):
            return(True, M, path)
        M[loc[0] - 1][loc[1] - 1] = 1
        B, M, path = Traverse(ag,M,loc,Clauses,path)
        if(B):
            return(True, M, path)

    if(IsSafe(M,i,j+1,Clauses)):                    #For Moving the agent Up
        ag.TakeAction('Up')
        path.append('Down')
        loc = ag.FindCurrentLocation()
        percept = ag.PerceiveCurrentLocation()
        Clauses = AddPercept(Clauses, percept,loc)
        if((CheckForGold(Clauses))):
            return(True, M, path)
        M[loc[0] - 1][loc[1] - 1] = 1
        C, M, path = Traverse(ag,M,loc,Clauses,path)
        if(C):
            return(True, M, path)

    if(IsSafe(M,i-1,j,Clauses)):                    #For Moving the agent Down
        ag.TakeAction('Down')
        path.append('Up')
        loc = ag.FindCurrentLocation()
        percept = ag.PerceiveCurrentLocation()
        Clauses = AddPercept(Clauses, percept,loc)
        if((CheckForGold(Clauses))):
            return(True, M, path)
        M[loc[0] - 1][loc[1] - 1] = 1
        D, M, path = Traverse(ag,M,loc,Clauses,path)
        if(D):
            return(True,M,path)

    if(A or B or C or D):
        return(True, M, path)

    else:
        if(len(path) == 0):
            return(False, M, path)

        elif(IsBound(i+1,j)):   #for Right
            clause = 100 + (10*(i+2)) + (j+1)
            if((ask(Clauses,clause) == False) and (ask(Clauses,-clause) == False)):
                M[i][j] = 2
                ag.TakeAction(path[-1])
                loc = ag.FindCurrentLocation()
                del path[-1]
                return(False, M, path)

        elif(IsBound(i-1,j)):   #for Left
            clause = 100 + (10*(i)) + (j+1)
            if((ask(Clauses,clause) == False) and (ask(Clauses,-clause) == False)):
                M[i][j] = 2
                ag.TakeAction(path[-1])
                loc = ag.FindCurrentLocation()
                del path[-1]
                return(False, M, path)

        elif(IsBound(i,j+1)):   #for Up
            clause = 100 + (10*(i+1)) + (j+2)
            if((ask(Clauses,clause) == False) and (ask(Clauses,-clause) == False)):
                M[i][j] = 2
                ag.TakeAction(path[-1])
                loc = ag.FindCurrentLocation()
                del path[-1]
                return(False, M, path)

        elif(IsBound(i,j-1)):   #for Down
            clause = 100 + (10*(i+1)) + (j)
            if((ask(Clauses,clause) == False) and (ask(Clauses,-clause) == False)):
                M[i][j] = 2
                ag.TakeAction(path[-1])
                loc = ag.FindCurrentLocation()
                del path[-1]
                return(False, M, path)
        
        ag.TakeAction(path[-1])
        del path[-1]
        loc = ag.FindCurrentLocation()
        T, M, path = Traverse(ag,M,loc,Clauses,path)
        return(T, M, path)

        

        


def main():
    Clauses = []
    ag = Agent()
    Kb = Glucose3()
    
    # adding background knowledge to Knowledge Base
    # Kb is Knowledge Base
    
    Clauses.append([-111]) # there is no mine at [1,1]
    
    for x in range(2,5):                # Adding information about position of gold: 
        for y in range(2,5):            # 3xy <-> ( 1(x-1)y & 1(x+1)y & 1x(y-1) & 1x(y+1) ) where [x,y] is the position of gold.
            A = 300 + (10*x) + y
            B = 100 + (10*(x-1)) + y
            C = 100 + (10*(x+1)) + y
            D = 100 + (10*x) + (y-1)
            E = 100 + (10*x) + (y+1)
            Clauses.append([-A,B])
            Clauses.append([-A,C])
            Clauses.append([-A,D])
            Clauses.append([-A,E])
            Clauses.append([A,-B,-C,-D,-E])

    Clauses.append([-311])         # Adding, "Gold is not present at the boundaries", to the Knowledge Base
    Clauses.append([-315])
    Clauses.append([-351])
    Clauses.append([-355])
    for x in range(2,5):
        A = 310 + x
        B = 350 + x
        C = 300 + 10*x + 5
        D = 300 + 10*x + 1
        Clauses.append([-A])
        Clauses.append([-B])
        Clauses.append([-C])
        Clauses.append([-D])

    M = [[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] #1 - Visited, 0 - unsure, 2 - Unvisited but safe
    path = []
    Clauses = AddPercept(Clauses,ag.PerceiveCurrentLocation(),ag.FindCurrentLocation())
    X, M, path = Traverse(ag,M,ag.FindCurrentLocation(),Clauses,path)
    if(X == False):
        print("Gold could not be detected after visiting all the safe rooms.")


if __name__=='__main__':
    main()