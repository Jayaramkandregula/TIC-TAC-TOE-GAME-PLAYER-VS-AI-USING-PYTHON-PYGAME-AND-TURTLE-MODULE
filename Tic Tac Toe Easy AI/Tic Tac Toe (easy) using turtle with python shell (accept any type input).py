import random
from turtle import *
from turtle import Screen
#turtle board
Xcolor="light green";Ocolor="skyblue";strikecolor="red"
bgcolor("black");pensize(8);setup(650,650);speed(100);hideturtle()
title("TIC TAC TOE (Player vs AI)")
def drawboard():
    color("white")
    up();goto(-300,100);down();forward(600)
    up();goto(-300,-100);down();forward(600)
    up();goto(-100,300);down();setheading(270);forward(600)
    up();goto(100,300);down();setheading(270);forward(600)
def pos1(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(-270,270);down();setheading(315);forward(200)
        up();goto(-270,130);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(-270,200);down();setheading(270);circle(70)
def pos2(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(-70,270);down();setheading(315);forward(200)
        up();goto(-70,130);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(-70,200);down();setheading(270);circle(70)
def pos3(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(130,270);down();setheading(315);forward(200)
        up();goto(130,130);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(130,200);down();setheading(270);circle(70)
def pos4(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(-270,70);down();setheading(315);forward(200)
        up();goto(-270,-70);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(-270,0);down();setheading(270);circle(70)
def pos5(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(-70,70);down();setheading(315);forward(200)
        up();goto(-70,-70);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(-70,0);down();setheading(270);circle(70)
def pos6(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(130,70);down();setheading(315);forward(200)
        up();goto(130,-70);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(130,0);down();setheading(270);circle(70)
def pos7(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(-270,-130);down();setheading(315);forward(200)
        up();goto(-270,-270);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(-270,-200);down();setheading(270);circle(70)
def pos8(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(-70,-130);down();setheading(315);forward(200)
        up();goto(-70,-270);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(-70,-200);down();setheading(270);circle(70)
def pos9(ch):
    if(ch=='X'):
        color(Xcolor);up();goto(130,-130);down();setheading(315);forward(200)
        up();goto(130,-270);down();setheading(45);forward(200)
    elif(ch=='O'):
        color(Ocolor);up();goto(130,-200);down();setheading(270);circle(70)
def strike(combo):
    pencolor(strikecolor)
    pensize(20)
    if(combo==0):up();goto(-300,200);down();setheading(0);forward(600)
    elif(combo==1):up();goto(-300,0);down();setheading(0);forward(600)
    elif(combo==2):up();goto(-300,-200);down();setheading(0);forward(600)
    elif(combo==3):up();goto(-200,300);down();setheading(270);forward(600)
    elif(combo==4):up();goto(0,300);down();setheading(270);forward(600)
    elif(combo==5):up();goto(200,300);down();setheading(270);forward(600)
    elif(combo==6):up();goto(-300,300);down();setheading(315);forward(850)
    elif(combo==7):up();goto(300,300);down();setheading(225);forward(850)
def chooseposition(row,col,choice):
    if(row==0 and col==0):pos1(choice)
    elif(row==0 and col==1):pos2(choice)
    elif(row==0 and col==2):pos3(choice)
    elif(row==1 and col==0):pos4(choice)
    elif(row==1 and col==1):pos5(choice)
    elif(row==1 and col==2):pos6(choice)
    elif(row==2 and col==0):pos7(choice)
    elif(row==2 and col==1):pos8(choice)
    elif(row==2 and col==2):pos9(choice)
#User
def displaytictactoe(ttt):
    print("\nTICTACTOE :")
    print("-------------")
    for i in range(3):
        print("| ",end='')
        for j in range(3):
            print(ttt[i][j],end=' | ')
        print("\n-------------")
    print()
def checktictactoe(ttt):
    check=[[ttt[0][0],ttt[0][1],ttt[0][2]],[ttt[1][0],ttt[1][1],ttt[1][2]],[ttt[2][0],ttt[2][1],ttt[2][2]],
           [ttt[0][0],ttt[1][0],ttt[2][0]],[ttt[0][1],ttt[1][1],ttt[2][1]],[ttt[0][2],ttt[1][2],ttt[2][2]],
           [ttt[0][0],ttt[1][1],ttt[2][2]],[ttt[0][2],ttt[1][1],ttt[2][0]]]
    if((['X','X','X'] in check)or(['O','O','O'] in check)):
        if(['X','X','X'] in check):return 1,check.index(['X','X','X'])
        elif(['O','O','O'] in check):return 1,check.index(['O','O','O'])
    else:
        return 0,0
def checkposition(row,col,ttt):
    while((row>'3' or col>'3' or row<'1' or col<'1' or len(row)>1 or len(col)>1) or (ttt[int(row)-1][int(col)-1]=='X' or ttt[int(row)-1][int(col)-1]=='O')):
        if(row>'3' or col>'3' or row<'1' or col<'1' or len(row)>1 or len(col)>1):
            print("Enter valid row and column :")
            row=(input("-->Enter row : "))
            col=(input("-->Enter column : "))
        elif(ttt[int(row)-1][int(col)-1]=='X' or ttt[int(row)-1][int(col)-1]=='O'):
            print("\nThat position is already occupied")
            displaytictactoe(ttt)
            print("Enter other position : ")
            row=(input("-->Enter row : "))
            col=(input("-->Enter column : "))
    return int(row),int(col)
#forAI
def unoccupiedpositionforAI(row,col,ttt):
    while(ttt[row-1][col-1]=='X' or ttt[row-1][col-1]=='O'):
        row=random.randint(1,3)
        col=random.randint(1,3)
    return row,col

#main block
ttt=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
myAI="JET"
P=input("Enter Name of the player : ")
choice=['X','O']
Pchoice=input("Enter player choice(either X or O) : ").upper()
while(Pchoice not in choice):
    print("Invalid choice!Now",end=' ')
    Pchoice=input("Enter valid choice i.e,either X or O : ").upper() 
print("%s's choice is : %s"%(P,Pchoice))
choice.remove(Pchoice)
AIchoice=choice[0]
print("%s AI's choice is : %s"%(myAI,AIchoice))
displaytictactoe(ttt)
drawboard()
for n in range(9):
    if(n%2==0):
        print("%s's chance :"%(P))
        Prow=(input("-->Enter row : "))
        Pcol=(input("-->Enter column : "))
        Prow,Pcol=checkposition(Prow,Pcol,ttt)
        ttt[Prow-1][Pcol-1]=Pchoice
        displaytictactoe(ttt)
        chooseposition(Prow-1,Pcol-1,Pchoice)
        check,comboposition=checktictactoe(ttt)
        if(check==1):
            strike(comboposition)
            print("--Congratulations--",P," You have won the match")
            break
    else:
        print("%s's chance :"%(myAI))
        AIrow=random.randint(1,3)
        AIcol=random.randint(1,3)
        AIrow,AIcol=unoccupiedpositionforAI(AIrow,AIcol,ttt)
        print("-->Inserted row : %d"%(AIrow))
        print("-->Inserted column : %d"%(AIcol))
        ttt[AIrow-1][AIcol-1]=AIchoice
        displaytictactoe(ttt)
        chooseposition(AIrow-1,AIcol-1,AIchoice)
        check,comboposition=checktictactoe(ttt)
        if(check==1):
            strike(comboposition)
            print("MY AI %s has won the match"%(myAI))
            print("Better luck next time|")
            break
else:
    print("---The match is drawn---")

enter=input()
