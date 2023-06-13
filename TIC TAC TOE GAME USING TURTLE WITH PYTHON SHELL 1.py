import random
from turtle import *
from turtle import Screen
#turtle board
Xcolor="light green";Ocolor="skyblue";strikecolor="red"
bgcolor("black");pensize(20);setup(650,700);speed(100);hideturtle()
title("TIC TAC TOE GAME")
def drawboard():
    color("white");pensize(10)
    up();goto(-300,100);down();forward(600)
    up();goto(-300,-100);down();forward(600)
    up();goto(-100,300);down();setheading(270);forward(600)
    up();goto(100,300);down();setheading(270);forward(600)
    pensize(8)
    color("red")
    up();goto(-290,290);down();write(11);up();goto(-90,290);down();write(12);up();goto(110,290);down();write(13)
    up();goto(-290,80);down();write(21);up();goto(-90,80);down();write(22);up();goto(110,80);down();write(23)
    up();goto(-290,-120);down();write(31);up();goto(-90,-120);down();write(32);up();goto(110,-120);down();write(33)
def pos1(ch):
    if(ch=='X'):color(Xcolor);up();goto(-270,270);down();setheading(315);forward(200);up();goto(-270,130);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(-270,200);down();setheading(270);circle(70)
def pos2(ch):
    if(ch=='X'):color(Xcolor);up();goto(-70,270);down();setheading(315);forward(200);up();goto(-70,130);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(-70,200);down();setheading(270);circle(70)
def pos3(ch):
    if(ch=='X'):color(Xcolor);up();goto(130,270);down();setheading(315);forward(200);up();goto(130,130);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(130,200);down();setheading(270);circle(70)
def pos4(ch):
    if(ch=='X'):color(Xcolor);up();goto(-270,70);down();setheading(315);forward(200);up();goto(-270,-70);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(-270,0);down();setheading(270);circle(70)
def pos5(ch):
    if(ch=='X'):color(Xcolor);up();goto(-70,70);down();setheading(315);forward(200);up();goto(-70,-70);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(-70,0);down();setheading(270);circle(70)
def pos6(ch):
    if(ch=='X'):color(Xcolor);up();goto(130,70);down();setheading(315);forward(200);up();goto(130,-70);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(130,0);down();setheading(270);circle(70)
def pos7(ch):
    if(ch=='X'):color(Xcolor);up();goto(-270,-130);down();setheading(315);forward(200);up();goto(-270,-270);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(-270,-200);down();setheading(270);circle(70)
def pos8(ch):
    if(ch=='X'):color(Xcolor);up();goto(-70,-130);down();setheading(315);forward(200);up();goto(-70,-270);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(-70,-200);down();setheading(270);circle(70)
def pos9(ch):
    if(ch=='X'):color(Xcolor);up();goto(130,-130);down();setheading(315);forward(200);up();goto(130,-270);down();setheading(45);forward(200)
    elif(ch=='O'):color(Ocolor);up();goto(130,-200);down();setheading(270);circle(70)
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
####
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
##FOR AI
def combospaceindex(ci,si):
    combospacedic={0:{0:[0,0],1:[0,1],2:[0,2]},1:{0:[1,0],1:[1,1],2:[1,2]},2:{0:[2,0],1:[2,1],2:[2,2]},
                   3:{0:[0,0],1:[1,0],2:[2,0]},4:{0:[0,1],1:[1,1],2:[2,1]},5:{0:[0,2],1:[1,2],2:[2,2]},
                   6:{0:[0,0],1:[1,1],2:[2,2]},7:{0:[0,2],1:[1,1],2:[2,0]}}
    return combospacedic[ci][si][0],combospacedic[ci][si][1]
def middlechoice():
    middle={2:[0,1],4:[1,0],6:[1,2],8:[2,1]}
    x=random.choice(list(middle.keys()))
    return middle[x][0],middle[x][1]
def cornerchoice():
    corner={1:[0,0],3:[0,2],7:[2,0],9:[2,2]}
    x=random.choice(list(corner.keys()))
    return corner[x][0],corner[x][1]
##Hard AI
def HardAI(ttt,chance,Pchoice,AIchoice):
    check=[[ttt[0][0],ttt[0][1],ttt[0][2]],[ttt[1][0],ttt[1][1],ttt[1][2]],[ttt[2][0],ttt[2][1],ttt[2][2]],
           [ttt[0][0],ttt[1][0],ttt[2][0]],[ttt[0][1],ttt[1][1],ttt[2][1]],[ttt[0][2],ttt[1][2],ttt[2][2]],
           [ttt[0][0],ttt[1][1],ttt[2][2]],[ttt[0][2],ttt[1][1],ttt[2][0]]]
    if(chance==1):
        if(ttt[1][1]==' '):
            return 1,1
        elif(ttt[1][1]=='X' or ttt[1][1]=='O'):
            corner={1:[0,0],3:[0,2],7:[2,0],9:[2,2]}
            x=random.choice(list(corner.keys()))
            return corner[x][0],corner[x][1]
    elif(chance>1):
        for combo in check:
            if(combo.count(AIchoice)==2 and combo.count(' ')==1):
                row,col=combospaceindex(check.index(combo),combo.index(' '))
                return row,col
        for combo in check:
            if(combo.count(Pchoice)==2 and combo.count(' ')==1):
                row,col=combospaceindex(check.index(combo),combo.index(' '))
                return row,col
        for combo in check[6:]:  #***
            if(chance==2 and (combo.count(Pchoice)==2 and combo.count(AIchoice)==1)):
                comboindex=check.index(combo)
                n=random.randint(1,2)
                if(combo==[Pchoice,Pchoice,AIchoice] or combo==[AIchoice,Pchoice,Pchoice]):
                    if(comboindex==6):
                        if(n==1):return 2,0
                        elif(n==2):return 0,2
                    elif(comboindex==7):
                        if(n==1):return 0,0
                        elif(n==2):return 2,2
        if(chance==2):
            corner={1:[0,0],3:[0,2],7:[2,0],9:[2,2]}
            middle={2:[0,1],4:[1,0],6:[1,2],8:[2,1]}
            if(check[6]==[Pchoice,AIchoice,Pchoice] or check[7]==[Pchoice,AIchoice,Pchoice]):
                row,col=middlechoice();return row,col
            elif(check[1]==[Pchoice,AIchoice,Pchoice] or check[4]==[Pchoice,AIchoice,Pchoice]):
                row,col=cornerchoice();return row,col
            else:
                for cor in list(corner.values()):
                    for mid in list(middle.values()):
                        if(ttt[cor[0]][cor[1]]==Pchoice and ttt[mid[0]][mid[1]]==Pchoice):
                            if(mid[1]==1):return mid[0],cor[1]
                            else:return cor[0],mid[1]
                else:
                    for i in [2,8]:
                        if(ttt[middle[i][0]][middle[i][1]]==Pchoice and ttt[middle[4][0]][middle[4][1]]==Pchoice):return corner[i-1][0],corner[i-1][1]
                        elif(ttt[middle[i][0]][middle[i][1]]==Pchoice and ttt[middle[6][0]][middle[6][1]]==Pchoice):return corner[i+1][0],corner[i+1][1]
        elif(chance>2):
            for combo in check:
                if(combo.count(Pchoice)==1 and combo.count(AIchoice)==1 and combo.count(' ')==1):
                    row,col=combospaceindex(check.index(combo),combo.index(' '))
                    return row,col
    
##Medium AI
def MediumAI(ttt,chance,Pchoice,AIchoice):
    check=[[ttt[0][0],ttt[0][1],ttt[0][2]],[ttt[1][0],ttt[1][1],ttt[1][2]],[ttt[2][0],ttt[2][1],ttt[2][2]],
           [ttt[0][0],ttt[1][0],ttt[2][0]],[ttt[0][1],ttt[1][1],ttt[2][1]],[ttt[0][2],ttt[1][2],ttt[2][2]],
           [ttt[0][0],ttt[1][1],ttt[2][2]],[ttt[0][2],ttt[1][1],ttt[2][0]]]
    if(chance==1):
        if(ttt[1][1]==' '):
            n=random.choice([1,2,3])
            for combo in check:
                if(combo.count(Pchoice)==1):
                    row1,col1=combospaceindex(check.index(combo),combo.index(Pchoice))
            if(n==1):return 1,1
            elif(n==2):
                row,col=middlechoice()
                while(row==row1 and col==col1):
                    row,col=middlechoice()
                return row,col
            elif(n==3):
                row,col=cornerchoice()
                while(row==row1 and col==col1):
                    row,col=cornerchoice()
                return row,col
        elif(ttt[1][1]=='X' or ttt[1][1]=='O'):
            n=random.choice([1,2])
            if(n==1):row,col=middlechoice();return row,col
            elif(n==2):row,col=cornerchoice();return row,col
    elif(chance>1):
        if(chance==2 or chance==3):
            for combo in check:
                if(combo.count(AIchoice)==2 and combo.count(' ')==1):row,col=combospaceindex(check.index(combo),combo.index(' '));return row,col
            for combo in check:
                if(combo.count(Pchoice)==2 and combo.count(' ')==1):row,col=combospaceindex(check.index(combo),combo.index(' '));return row,col
        for combo in check[6:]:
            if(chance==2 and (combo.count(Pchoice)==2 and combo.count(AIchoice)==1)):
                comboindex=check.index(combo)
                if(combo==[Pchoice,Pchoice,AIchoice] or combo==[AIchoice,Pchoice,Pchoice]):
                    row,col=middlechoice();return row,col
        if(chance>=2 and ttt[1][1]==' '):
            return 1,1   
        if(chance==2):
            if(check[6]==[Pchoice,AIchoice,Pchoice] or check[7]==[Pchoice,AIchoice,Pchoice]):
                row,col=middlechoice();return row,col
            elif(check[1]==[Pchoice,AIchoice,Pchoice] or check[4]==[Pchoice,AIchoice,Pchoice]):
                row,col=cornerchoice();return row,col
        if(chance>=2):
            for combo in check:
                if(combo.count(Pchoice)==1 and combo.count(AIchoice)==1 and combo.count(' ')==1):
                    row,col=combospaceindex(check.index(combo),combo.index(' '))
                    return row,col
            for combo in check:
                if(combo.count(' ')==2 and (combo.count(Pchoice)==1 or combo.count(AIchoice)==1)):
                    row,col=combospaceindex(check.index(combo),combo.index(' '))
                    return row,col
##Easy AI    
def EasyAI(row,col,ttt):
    while(ttt[row-1][col-1]=='X' or ttt[row-1][col-1]=='O'):
        row=random.randint(1,3)
        col=random.randint(1,3)
    return row,col               
##player vs player
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
#to take valid input from user
def take_user_input(P,Pchoice,ttt):
    print("%s's chance :"%(P))
    Prow=(input("-->Enter row : "))
    Pcol=(input("-->Enter column : "))
    Prow,Pcol=checkposition(Prow,Pcol,ttt)
    ttt[Prow-1][Pcol-1]=Pchoice
    return Prow,Pcol
####main block
ttt=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
myAI="JET"
####
while(1):
    print("MODE : ")
    print("1.Player vs Player\n2.Player vs %s AI"%(myAI))
    mode=input("Choose mode : ");print()
    if(mode=='1' or mode=='2'):
        break
drawboard()
pensize(20)
if(mode=='1'):
    title("TIC TAC TOE(PLAYER VS PLAYER)")
    P1=input("Enter Name of the player1 : ")
    P2=input("Enter Name of the player2 : ")
    title("TIC TAC TOE(%s VS %s)"%(P1,P2))
    choice=['X','O']
    P1choice=input("Enter player1 choice(either X or O) : ").upper()
    while(P1choice not in choice):
        print("Invalid choice!Now",end=' ')
        P1choice=input("Enter valid choice i.e,either X or O : ").upper() 
    print("%s's choice is : %s"%(P1,P1choice))
    choice.remove(P1choice)
    P2choice=choice[0]
    print("%s's choice is : %s"%(P2,P2choice))
    displaytictactoe(ttt)
    for n in range(9):
        if(n%2==0):
            P1row,P1col=take_user_input(P1,P1choice,ttt)
            displaytictactoe(ttt)
            chooseposition(P1row-1,P1col-1,P1choice)
            check,comboposition=checktictactoe(ttt)
            if(check==1):
                strike(comboposition)
                print("--Congratulations--",P1," You have won the match")
                break
        else:
            P2row,P2col=take_user_input(P2,P2choice,ttt)
            displaytictactoe(ttt)
            chooseposition(P2row-1,P2col-1,P2choice)
            check,comboposition=checktictactoe(ttt)
            if(check==1):
                strike(comboposition)
                print("--Congratulations--",P2," You have won the match")
                break
    else:
        print("---The match is drawn---")
if(mode=='2'):
    title("TIC TAC TOE(PLAYER VS %s AI)"%(myAI))
    while(1):
        print("Level of hardness of %s AI"%(myAI))
        print("1.Easy\n2.Medium\n3.Hard")
        level=input("Choose Level of Hardness : ");print()
        if(level=='1' or level=='2' or level =='3'):
            break
    P=input("Enter Your Name : ")
    choice=['X','O']
    Pchoice=input("Enter Your choice(either X or O) : ").upper()
    while(Pchoice not in choice):
        print("Invalid choice!Now",end=' ')
        Pchoice=input("Enter valid choice i.e,either X or O : ").upper() 
    print("%s's choice is : %s"%(P,Pchoice))
    choice.remove(Pchoice)
    AIchoice=choice[0]
    print("%s AI choice is : %s"%(myAI,AIchoice))
    displaytictactoe(ttt)
    chance=0
    if(level=='1'):
        title("TIC TAC TOE(PLAYER VS %s AI(Easy))"%(myAI))
        for n in range(9):
            if(n%2==0):
                Prow,Pcol=take_user_input(P,Pchoice,ttt)
                displaytictactoe(ttt)
                chooseposition(Prow-1,Pcol-1,Pchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    print("--Congratulations--",P," You have won the match")
                    break
            else:
                print("%s's chance :"%(myAI))
                eAIrow=random.randint(1,3)
                eAIcol=random.randint(1,3)
                eAIrow,eAIcol=EasyAI(eAIrow,eAIcol,ttt)
                print("-->Inserted row : %d"%(eAIrow))
                print("-->Inserted column : %d"%(eAIcol))
                ttt[eAIrow-1][eAIcol-1]=AIchoice
                displaytictactoe(ttt)
                chooseposition(eAIrow-1,eAIcol-1,AIchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    print("MY AI %s has won the match"%(myAI))
                    print("Better luck next time|")
                    break
        else:
            print("---The match is drawn---")
    elif(level=='2'):
        title("TIC TAC TOE(PLAYER VS %s AI(Medium))"%(myAI))
        for n in range(9):
            if(n%2==0):
                Prow,Pcol=take_user_input(P,Pchoice,ttt)
                displaytictactoe(ttt)
                chooseposition(Prow-1,Pcol-1,Pchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    print("--Congratulations--",P," You have won the match")
                    break
            else:
                print("%s AI's chance :"%(myAI))
                chance=chance+1
                mAIrow,mAIcol=MediumAI(ttt,chance,Pchoice,AIchoice)
                print("-->Inserted row : %d"%(mAIrow+1))
                print("-->Inserted column : %d"%(mAIcol+1))
                ttt[mAIrow][mAIcol]=AIchoice
                displaytictactoe(ttt)
                chooseposition(mAIrow,mAIcol,AIchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    print("MY AI %s has won the match"%(myAI))
                    print("Better luck next time|")
                    break
        else:
            print("---The match is drawn---")
    elif(level=='3'):
        title("TIC TAC TOE(PLAYER VS %s AI(Hard))"%(myAI))
        for n in range(9):
            if(n%2==0):
                Prow,Pcol=take_user_input(P,Pchoice,ttt)
                displaytictactoe(ttt)
                chooseposition(Prow-1,Pcol-1,Pchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    print("--Congratulations--",P," You have won the match")
                    break
            else:
                print("%s AI's chance :"%(myAI))
                chance=chance+1
                hAIrow,hAIcol=HardAI(ttt,chance,Pchoice,AIchoice)
                print("-->Inserted row : %d"%(hAIrow+1))
                print("-->Inserted column : %d"%(hAIcol+1))
                ttt[hAIrow][hAIcol]=AIchoice
                displaytictactoe(ttt)
                chooseposition(hAIrow,hAIcol,AIchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    print("MY AI %s has won the match"%(myAI))
                    print("Better luck next time|")
                    break
        else:
            print("---The match is drawn---")
enter=input()
