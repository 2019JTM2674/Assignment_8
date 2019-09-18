#!/usr/bin/python3
import math
#tic tac code

#function for calculation
def evaluate(matrix):
    sum_row1=0 
    sum_col2=0 
    sum_col1=0 
    sum_col3=0
    sum_row2=0 
    sum_dia1=0 
    sum_dia2=0
    sum_row3=0
    sum_row1+=matrix[0][0]+matrix[0][1]+matrix[0][2]  #finding sum of rows
    sum_row2+=matrix[1][0]+matrix[1][1]+matrix[1][2]
    sum_row3+=matrix[2][0]+matrix[2][1]+matrix[2][2]

    sum_col1+=matrix[0][0]+matrix[1][0]+matrix[2][0]  #finding sum of cols
    sum_col2+=matrix[0][1]+matrix[1][1]+matrix[2][1]
    sum_col3+=matrix[0][2]+matrix[1][2]+matrix[2][2]
        
    sum_dia1+=matrix[0][0]+matrix[1][1]+matrix[2][2] #finding sum of diagonals
    sum_dia2+=matrix[0][2]+matrix[1][1]+matrix[2][0]

    #checking condition
    if sum_col1>15 or sum_col2>15 or sum_col3>15 or sum_row1>15 or sum_row2>15 or sum_row3>15 or sum_dia1>15 or sum_dia2>15:
        print("Out of Range")
        print("Re enter")
        return 3
    elif sum_col1==15 or sum_col2==15 or sum_col3==15 or sum_row1==15 or sum_row2==15 or sum_row3==15 or sum_dia1==15 or sum_dia2==15:
        print("Game Over")
        return 1
    else:
        return 2


#function for taking input
def ticTakToe():
    matrix=[]
    change=3
    for col in range(1,4):
        row=[]
        for r in range(1,4):
            row.append(0)
        matrix.append(row)
    print(matrix)
    
    while 1 :
        print("Player 1's chance")
        pos,num=[int(x) for x in input("Enter the position and number to be entered:").split()]
        #exception handling
        if(num>9):
            print("Error: Range of number is 0-9")
            print("Re enter")
            continue
        #exception handling
        if(pos>9):
            print("Error: Range of position is 0-9")
            print("Re enter")
            continue
        #exception handling
        if(num%2==0):
            print("Invalid input. Enter a odd number")
            continue

        #forming a matrix
        if pos<4:
            y=math.floor((pos-1)/3)
            x=(pos-1)%3
            print(x,y)
            matrix[y][x]=num
        elif pos>3 and pos<7:
            y=math.floor((pos-1)/3)
            x=(pos-1)%3
            print(x,y)
            matrix[y][x]=num
        elif pos>6 and pos<10:
            y=math.floor((pos-1)/3)
            x=(pos-1)%3
            print(x,y)
            matrix[y][x]=num

        for mat in matrix:
            print(*mat)

        flag=evaluate(matrix)
        print(flag)
        if flag==1:
            print("Player1 won")
            break
        if flag==3:
            matrix[y][x]=0
            continue

        while change==3:
            
            print("Player 2’s chance")
            pos,num=[int(x) for x in input("Enter the position and number to be entered:").split()]
             #exception handling
            if(num>9):
                print("Error: Range of number is 0-9")
                print("Re enter")
                continue
             #exception handling
            if(pos>9):
                print("Error: Range of position is 0-9")
                print("Re enter")
                continue
             #exception handling
            if(num%2!=0):
                print("Invalid input. Enter a even number")
                continue
            #forming a matrix
            if pos<4:
                y=math.floor((pos-1)/3)
                x=(pos-1)%3
                print(x,y)
                matrix[y][x]=num
            elif pos>3 and pos<7:
                y=math.floor((pos-1)/3)
                x=(pos-1)%3
                print(x,y)
                matrix[y][x]=num
            elif pos>6 and pos<10:
                y=math.floor((pos-1)/3)
                x=(pos-1)%3
                print(x,y)
                matrix[y][x]=num

            for mat in matrix:
                print(*mat)
        
            flag2=evaluate(matrix)
            if flag2==2 or flag2==1:
                break
            print(flag)
            if flag2==3:
                matrix[y][x]=0
                change=3
                continue
        if flag2==1:
            print("Player 2 won")
            break



#main function
print("Welcome to the Game")
score=ticTakToe()
