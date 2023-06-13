import random
from turtle import *
from turtle import Screen
#turtle board
Xcolor="light green";Ocolor="skyblue";strikecolor="red"
bgcolor("black");pensize(20);speed(100);hideturtle()
title("TIC TAC TOE GAME")
def drawboard():
    color("white");pensize(10)
    up();goto(-300,100);down();forward(600)
    up();goto(-300,-100);down();forward(600)
    up();goto(-100,300);down();setheading(270);forward(600)
    up();goto(100,300);down();setheading(270);forward(600)
    pensize(8)
    color("red")
    up();goto(-290,275);down();write(11,font=("calibri",3,"bold"));up();goto(-90,275);down();write(12,font=("calibri",3,"bold"));up();goto(110,275);down();write(13,font=("calibri",3,"bold"))
    up();goto(-290,75);down();write(21,font=("calibri",3,"bold"));up();goto(-90,75);down();write(22,font=("calibri",3,"bold"));up();goto(110,75);down();write(23,font=("calibri",3,"bold"))
    up();goto(-290,-125);down();write(31,font=("calibri",3,"bold"));up();goto(-90,-125);down();write(32,font=("calibri",3,"bold"));up();goto(110,-125);down();write(33,font=("calibri",3,"bold"))
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
##player
def checkvalidposition(position,P,ttt):
    while(1):
        if(position!=None):
            positionlist=list(position)
            for x in positionlist[:]:
                if(x==' '):
                    positionlist.remove(x)
            if(len(positionlist)==2):
                row,col=positionlist[0],positionlist[1]
                if(row<='3' and col<='3' and col>='1' and row>='1'):
                    if(ttt[int(row)-1][int(col)-1]!='X' and ttt[int(row)-1][int(col)-1]!='O'):
                        break
        position=textinput("%s's chance :"%(P),"Enter row and column : ")
    return int(row),int(col)
#to take valid input from user
def take_user_input(P,Pchoice,ttt):
    position=textinput("%s's chance :"%(P),"Enter row and column : ")
    Prow,Pcol=checkvalidposition(position,P,ttt)
    ttt[Prow-1][Pcol-1]=Pchoice
    return Prow,Pcol
####main block
ttt=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
myAI="JET"
####
while(1):
    mode=textinput("Choose mode","1.Player vs Player\n2.Player vs %s AI"%(myAI))
    if(mode=='1' or mode=='2'):
        break
drawboard()
pensize(20)
if(mode=='1'):
    title("TIC TAC TOE(PLAYER VS PLAYER)")
    while(1):
        P1=textinput("Player1","Enter The Name Of Player1 : ")
        if(P1!=None and P1!=''):
            break
    while(1):
        P2=textinput("Player2","Enter The Name Of Player2 : ")
        if(P1!=None and P2!=''):
            break
    title("TIC TAC TOE(%s VS %s)"%(P1,P2))
    choice=['X','O']
    while(1):
        P1choice=textinput("Choose X or O","X or O : ")
        if(P1choice!=None):
            P1choice=P1choice.upper()
            if(P1choice in choice):
                break
    choice.remove(P1choice.upper())
    P2choice=choice[0]
    for n in range(9):
        if(n%2==0):
            P1row,P1col=take_user_input(P1,P1choice,ttt)
            chooseposition(P1row-1,P1col-1,P1choice)
            check,comboposition=checktictactoe(ttt)
            if(check==1):
                strike(comboposition)
                up();goto(-300,320);down();color("gold");write("Congratulations %s!You have won the match"%(P1),font=("arial",4,"bold"))
                break
        else:
            P2row,P2col=take_user_input(P2,P2choice,ttt)
            chooseposition(P2row-1,P2col-1,P2choice)
            check,comboposition=checktictactoe(ttt)
            if(check==1):
                strike(comboposition)
                up();goto(-300,320);down();color("gold");write("Congratulations %s!You have won the match"%(P2),font=("arial",4,"bold"))
                break
    else:
        up();goto(-300,320);down();color("gold");write("The match is drawn!",font=("arial",4,"bold"))
if(mode=='2'):
    title("TIC TAC TOE(PLAYER VS %s AI)"%(myAI))
    while(1):
        level=textinput("Choose Level of Hardness : ","1.Easy\n2.Medium\n3.Hard");print()
        if(level=='1' or level=='2' or level =='3'):
            break
    while(1):
        P=textinput("Name","Enter Your Name : ")
        if(P!=None and P!=''):
            break
    choice=['X','O']
    while(1):
        Pchoice=textinput("Choose X or O","X or O : ")
        if(Pchoice!=None):
            Pchoice=Pchoice.upper()
            if(Pchoice in choice):
                break
    choice.remove(Pchoice)
    AIchoice=choice[0]
    chance=0
    if(level=='1'):
        title("TIC TAC TOE(%s VS %s AI(Easy))"%(P,myAI))
        for n in range(9):
            if(n%2==0):
                Prow,Pcol=take_user_input(P,Pchoice,ttt)
                chooseposition(Prow-1,Pcol-1,Pchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    up();goto(-300,320);down();color("gold");write("Congratulations %s!You have won the match"%(P),font=("arial",4,"bold"))
                    break
            else:
                eAIrow=random.randint(1,3)
                eAIcol=random.randint(1,3)
                eAIrow,eAIcol=EasyAI(eAIrow,eAIcol,ttt)
                ttt[eAIrow-1][eAIcol-1]=AIchoice
                chooseposition(eAIrow-1,eAIcol-1,AIchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    up();goto(-300,320);down();color("gold");write("MY AI %s has won the match"%(myAI),font=("arial",4,"bold"))
                    break
        else:
            up();goto(-300,320);down();color("gold");write("The match is drawn!",font=("arial",4,"bold"))
    elif(level=='2'):
        title("TIC TAC TOE(%s VS %s AI(Medium))"%(P,myAI))
        for n in range(9):
            if(n%2==0):
                Prow,Pcol=take_user_input(P,Pchoice,ttt)
                chooseposition(Prow-1,Pcol-1,Pchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    up();goto(-300,320);down();color("gold");write("Congratulations %s!You have won the match"%(P),font=("arial",4,"bold"))
                    break
            else:
                chance=chance+1
                mAIrow,mAIcol=MediumAI(ttt,chance,Pchoice,AIchoice)
                ttt[mAIrow][mAIcol]=AIchoice
                chooseposition(mAIrow,mAIcol,AIchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    up();goto(-300,320);down();color("gold");write("MY AI %s has won the match"%(myAI),font=("arial",4,"bold"))
                    break
        else:
            up();goto(-300,320);down();color("gold");write("---The match is drawn!---",font=("arial",4,"bold"))
    elif(level=='3'):
        title("TIC TAC TOE(%s VS %s AI(Hard))"%(P,myAI))
        for n in range(9):
            if(n%2==0):
                Prow,Pcol=take_user_input(P,Pchoice,ttt)
                chooseposition(Prow-1,Pcol-1,Pchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    up();goto(-300,320);down();color("gold");write("Congratulations %s!You have won the match"%(P),font=("arial",4,"bold"))
                    break
            else:
                chance=chance+1
                hAIrow,hAIcol=HardAI(ttt,chance,Pchoice,AIchoice)
                ttt[hAIrow][hAIcol]=AIchoice
                chooseposition(hAIrow,hAIcol,AIchoice)
                check,comboposition=checktictactoe(ttt)
                if(check==1):
                    strike(comboposition)
                    up();goto(-300,320);down();color("gold");write("MY AI %s has won the match"%(myAI),font=("arial",4,"bold"))
                    break
        else:
            up();goto(-300,320);down();color("gold");write("---The match is drawn!---",font=("arial",4,"bold"))
exitonclick()
