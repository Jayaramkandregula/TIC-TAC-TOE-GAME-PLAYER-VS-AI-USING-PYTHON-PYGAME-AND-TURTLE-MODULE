import random
#player
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
        return 1
    else:
        return 0
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
#medium AI
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
def mediumAI(ttt,chance,Pchoice,AIchoice):
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
        for combo in check[6:]:  #***
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
chance=0
for n in range(9):
    if(n%2==0):
        print("%s's chance :"%(P))
        Prow=(input("-->Enter row : "))
        Pcol=(input("-->Enter column : "))
        Prow,Pcol=checkposition(Prow,Pcol,ttt)
        ttt[Prow-1][Pcol-1]=Pchoice
        displaytictactoe(ttt)
        if(checktictactoe(ttt)==1):
            print("--Congratulations--",P," You have won the match")
            break
    else:
        print("%s AI's chance :"%(myAI))
        chance=chance+1
        AIrow,AIcol=mediumAI(ttt,chance,Pchoice,AIchoice)
        print("-->Inserted row : %d"%(AIrow+1))
        print("-->Inserted column : %d"%(AIcol+1))
        ttt[AIrow][AIcol]=AIchoice
        displaytictactoe(ttt)
        if(checktictactoe(ttt)==1):
            print("MY AI %s has won the match"%(myAI))
            print("Better luck next time|")
            break
else:
    print("---The match is drawn---")

enter=input()
