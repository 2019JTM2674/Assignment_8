#!/usr/bin/python3
import math


def ticTakToe():
    matrix=[]
    sum_row=0
    sum_dia=0
    sum_col=0
    for col in range(1,4):
        row=[]
        for r in range(1,4):
            row.append(0)
        matrix.append(row)
    print(matrix)
    print("Player 1's chance")
    pos,num=[int(x) for x in input("Enter the position and number to be entered:").split()]
    while sum_col<15 or sum_dia<15 or sum_row<15 :

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

        sum_row=0
        sum_dia=0
        sum_col=0
        
        for i in range(0,3):
            for j in range(0,3):
                sum_row+=matrix[i][j]
                sum_col+=matrix[j][i]
                if(i==j):
                    sum_dia+=matrix[i][j]
        
        
        if sum_row>15:
            return sum_row
        elif sum_col>15:
            return sum_col
        elif sum_dia>15:
            return sum_dia
        print(sum_col,sum_dia,sum_dia)

        print("Player 2’s chance")
        pos,num=[int(x) for x in input("Enter the position and number to be entered:").split()]

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
        
        sum_row=0
        sum_dia=0
        sum_col=0
        for i in range(0,3):
            for j in range(0,3):
                sum_row+=matrix[i][j]
                sum_col+=matrix[j][i]
                if(i==j):
                    sum_dia+=matrix[i][j]

        print(sum_col,sum_dia,sum_dia)

        
        if sum_row>15:
            return sum_row
        elif sum_col>15:
            return sum_col
        elif sum_dia>15:
            return sum_dia
        else:
            continue









print("Welcome to the Game")
score=ticTakToe()
