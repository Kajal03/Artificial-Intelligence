import random

def printSolution(board,n):
    
    print("\n{}-Queen Solution:: \n".format(n))
    for i in range(0,n):
        for j in range(0,n):
            if j==board[i]:
                print(1,end=' ')
            else:
                print(0,end=' ')
        print()        
    
def getScore(board,i,n):
    score=0
    for j in range(0,n):
        if i==j:
            continue
        if board[i]==board[j]:
            score+=1
            continue
        if abs(board[i]-board[j])==abs(i-j):
            score+=1
            continue
    return score

def getBoardScore(board,n):
    score=0
    for i in range(0,n-1):
        score+=getScore(board,i,n)
    return score

def searchBoardHeuristic(board,n):
    #boardScore = getBoardScore(board,n)
    newBoard=[ [0]*n ]*n
    for i in range(0,n):
        newBoard[i]=board[i]
        
    for i in range(0,n):
        choice=[]
        choice.append(newBoard[i])
        temp=newBoard[i]
        score=getScore(newBoard,i,n)
        
        for j in range(0,n):
            newBoard[i]=j
            k=getScore(newBoard,i,n)
            if k==score:
                choice.append(j)
            if k<score:
                choice=[]
                choice.append(j)
                score=k
        newBoard[i] = choice[ random.randint(0,len(choice)-1) ]

    return newBoard     

def findNextState(board,n):
    mainScore=getBoardScore(board,n)
    tempBoard=searchBoardHeuristic(board,n)

    if getBoardScore(tempBoard,n)<mainScore:
        for i in range(n):
            board[i]=tempBoard[i]
        return True

    return False        

def makeRandomBoard(board,n):
    for i in range(n):
        board[i] = random.randint(0,n-1)

def NQueenHillClimbing(n):
    board=[ [0]*n ]*n
    makeRandomBoard(board,n)

    while getBoardScore(board,n)!=0:
        if findNextState(board,n)==False:
            makeRandomBoard(board,n)

    printSolution(board,n)
    

try:
    n=int(input("Enter value of N: "))
    if n<4:
        raise Exception
    else:
        NQueenHillClimbing(n)
        
except(Exception):
    print("\nThere is no solution for N less than 4")
