import random
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
    check=[[ttt[0][0],ttt[0][1],ttt[0][2]],[ttt[1][0],ttt[1][1],ttt[1][2]],[ttt[2][0],ttt[2][1],ttt[2][2]],[ttt[0][0],ttt[1][0],ttt[2][0]],[ttt[0][1],ttt[1][1],ttt[2][1]],[ttt[0][2],ttt[1][2],ttt[2][2]],[ttt[0][0],ttt[1][1],ttt[2][2]],[ttt[0][2],ttt[1][1],ttt[2][0]]]
    if((['X','X','X'] in check)or(['O','O','O'] in check)):
        return 1
    else:
        return 0
def checkposition(row,col,ttt):
    while((row>'3' or col>'3' or row<'1' or col<'1' or len(row)>1 or len(col)>1) or (ttt[int(row)-1][int(col)-1]=='X' or ttt[int(row)-1][int(col)-1]=='O')):
        if(row>'3' or col>'3' or row<'1'or col<'1' or len(row)>1 or len(col)>1):
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
for n in range(9):
    if(n%2==0):
        print("%s's chance :"%(P))
        Prow=(input("-->Enter row : "))
        Pcol=(input("-->Enter column : "))
        Prow,Pcol=checkposition(Prow,Pcol,ttt)
        ttt[Prow-1][Pcol-1]=Pchoice
        displaytictactoe(ttt)
        if(checktictactoe(ttt)==1):
            print("--Congratulations--",P,"has won the match")
            break
    else:
        print("%s's chance :"%(myAI))
        AIrow=random.randint(1,3)
        AIcol=random.randint(1,3)
        AIrow,AIcol=unoccupiedpositionforAI(AIrow,AIcol,ttt)
        print("-->Inserted row : %d"%(AIrow-1))
        print("-->Inserted column : %d"%(AIcol-1))
        ttt[AIrow-1][AIcol-1]=AIchoice
        displaytictactoe(ttt)
        if(checktictactoe(ttt)==1):
            print("MY AI %s has won the match"%(myAI))
            print("Better luck next time")
            break
else:
    print("---The match is drawn---")

enter=input()
