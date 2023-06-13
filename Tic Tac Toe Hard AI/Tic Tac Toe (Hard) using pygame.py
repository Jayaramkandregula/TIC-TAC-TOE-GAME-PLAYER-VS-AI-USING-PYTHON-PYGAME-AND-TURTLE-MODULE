import pygame as pg
import random
pg.init()
window=pg.display.set_mode((600,700))
pg.display.set_caption("TIC TAC TOE")
rect1=pg.Rect(4,4,192,192)
rect2=pg.Rect(204,4,192,192)
rect3=pg.Rect(404,4,192,192)
rect4=pg.Rect(4,204,192,192)
rect5=pg.Rect(204,204,192,192)
rect6=pg.Rect(404,204,192,192)
rect7=pg.Rect(4,404,192,192)
rect8=pg.Rect(204,404,192,192)
rect9=pg.Rect(404,404,192,192)
#color
bgcolor=(0,0,0)
boardcolor=(255,255,255)
xcolor=(255,255,255)
ocolor=(255,255,255)
textplayermodecolor=(120,120,120)
textplayerwhichmodecolor=(120,0,1)
textAIlevelcolor=(120,120,120)
textAIwhichlevelcolor=(120,0,1)
textwincolor=(120,80,12)
strikecolor=(205,25,26)

ttt=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
choice="X"
count=0
#texts
smallfont=pg.font.SysFont('Corbel',17)
bigfont=pg.font.SysFont('Corbel',50)
textplayermode=smallfont.render('MODE : ',True,textplayermodecolor)
textplayerwhichmode=smallfont.render('PLAYER vs JET AI',True,textplayerwhichmodecolor)
textAIlevel=smallfont.render('LEVEL : ',True,textAIlevelcolor)
textAIwhichlevel=smallfont.render('HARD',True,textAIwhichlevelcolor)
textwinnerisplayer=bigfont.render("YOU HAVE WON THE GAME",True,textwincolor)
textwinnerisAI=bigfont.render("JET AI HAVE WON THE GAME",True,'light green')
textmatchdrawn=bigfont.render("THE GAME IS DRAWN",True,textwincolor)


Pchoice='X';AIchoice='O'
chance=1
draw=[False,False,False,False,False,False,False,False,False]
run=True

def drawline(index):
    if index==0:pg.draw.line(window,strikecolor,[0,100],[600,100],10)
    elif index==1:pg.draw.line(window,strikecolor,[0,300],[600,300],10)
    elif index==2:pg.draw.line(window,strikecolor,[0,500],[600,500],10)
    elif index==3:pg.draw.line(window,strikecolor,[100,0],[100,600],10)
    elif index==4:pg.draw.line(window,strikecolor,[300,0],[300,600],10)
    elif index==5:pg.draw.line(window,strikecolor,[500,0],[500,600],10)
    elif index==6:pg.draw.line(window,strikecolor,[0,0],[600,600],10)
    elif index==7:pg.draw.line(window,strikecolor,[600,0],[0,600],10)
    pg.display.update()
    
def checktictactoe():
    global count
    global run
    count=count+1
    check=[[ttt[0][0],ttt[0][1],ttt[0][2]],[ttt[1][0],ttt[1][1],ttt[1][2]],[ttt[2][0],ttt[2][1],ttt[2][2]],[ttt[0][0],ttt[1][0],ttt[2][0]],[ttt[0][1],ttt[1][1],ttt[2][1]],[ttt[0][2],ttt[1][2],ttt[2][2]],[ttt[0][0],ttt[1][1],ttt[2][2]],[ttt[0][2],ttt[1][1],ttt[2][0]]]
    if((['X','X','X'] in check)or(['O','O','O'] in check)):
        if(['X','X','X'] in check):
            run=False
            drawline(check.index(['X','X','X']))
            window.blit(textwinnerisplayer,(10,630))
            pg.display.update()
        elif(['O','O','O'] in check):
            run=False
            drawline(check.index(['O','O','O']))
            window.blit(textwinnerisAI,(10,630))
            pg.display.update()
    elif(count>=9):
        run=False
        window.blit(textmatchdrawn,(10,630))
        pg.display.update()
            
def drawboard():
    pg.draw.rect(window,boardcolor,rect1,1)
    pg.draw.rect(window,boardcolor,rect2,1)
    pg.draw.rect(window,boardcolor,rect3,1)
    pg.draw.rect(window,boardcolor,rect4,1)
    pg.draw.rect(window,boardcolor,rect5,1)
    pg.draw.rect(window,boardcolor,rect6,1)
    pg.draw.rect(window,boardcolor,rect7,1)
    pg.draw.rect(window,boardcolor,rect8,1)
    pg.draw.rect(window,boardcolor,rect9,1)
    pg.draw.rect(window,boardcolor,(0,0,600,600),10)
    pg.draw.line(window,boardcolor,[0,200],[600,200],10)
    pg.draw.line(window,boardcolor,[0,400],[600,400],10)
    pg.draw.line(window,boardcolor,[200,0],[200,597],10)
    pg.draw.line(window,boardcolor,[400,0],[400,597],10)
    pg.display.update()
drawboard()

def drawX(x,y):
    pg.draw.line(window,xcolor,[x,y],[x+170,y+170],15)
    pg.draw.line(window,xcolor,[x+170,y],[x,y+170],15)
    pg.display.update()
def drawO(x,y):
    pg.draw.circle(window,ocolor,[x,y],85,15)
    pg.display.update()

def combospaceindex(ci,si):
    combospacedic={0:{0:[0,0],1:[0,1],2:[0,2]},1:{0:[1,0],1:[1,1],2:[1,2]},2:{0:[2,0],1:[2,1],2:[2,2]},
                   3:{0:[0,0],1:[1,0],2:[2,0]},4:{0:[0,1],1:[1,1],2:[2,1]},5:{0:[0,2],1:[1,2],2:[2,2]},
                   6:{0:[0,0],1:[1,1],2:[2,2]},7:{0:[0,2],1:[1,1],2:[2,0]}}
    return combospacedic[ci][si][0],combospacedic[ci][si][1]
def AI(chance):
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
        for combo in check:
            if(chance>2 and combo.count(Pchoice)==1 and combo.count(AIchoice)==1 and combo.count(' ')==1):
                row,col=combospaceindex(check.index(combo),combo.index(' '))
                return row,col
    if(chance==2):
        corner={1:[0,0],3:[0,2],7:[2,0],9:[2,2]}
        middle={2:[0,1],4:[1,0],6:[1,2],8:[2,1]}
        if(check[6]==[Pchoice,AIchoice,Pchoice] or check[7]==[Pchoice,AIchoice,Pchoice]):
            x=random.choice(list(middle.keys()))
            return middle[x][0],middle[x][1]
        elif(check[1]==[Pchoice,AIchoice,Pchoice] or check[4]==[Pchoice,AIchoice,Pchoice]):
            x=random.choice(list(corner.keys()))
            return corner[x][0],corner[x][1]
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
def chanceforhardAI():
    global chance
    if chance<=4:
        row,col=AI(chance)
        ttt[row][col]='O'
        if(row==0 and col==0):drawO(100,100);draw[0]=True
        elif(row==0 and col==1):drawO(300,100);draw[1]=True
        elif(row==0 and col==2):drawO(500,100);draw[2]=True
        elif(row==1 and col==0):drawO(100,300);draw[3]=True
        elif(row==1 and col==1):drawO(300,300);draw[4]=True
        elif(row==1 and col==2):drawO(500,300);draw[5]=True
        elif(row==2 and col==0):drawO(100,500);draw[6]=True
        elif(row==2 and col==1):drawO(300,500);draw[7]=True
        elif(row==2 and col==2):drawO(500,500);draw[8]=True
    checktictactoe()
    chance=chance+1
                    

def mouseclicked():
    if rect1.collidepoint(pg.mouse.get_pos()) and draw[0]==False:
        draw[0]=True
        drawX(15,15)
        ttt[0][0]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect2.collidepoint(pg.mouse.get_pos()) and draw[1]==False:
        draw[1]=True
        drawX(215,15)
        ttt[0][1]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect3.collidepoint(pg.mouse.get_pos()) and draw[2]==False:
        draw[2]=True
        drawX(415,15)
        ttt[0][2]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect4.collidepoint(pg.mouse.get_pos()) and draw[3]==False:
        draw[3]=True
        drawX(15,215)
        ttt[1][0]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect5.collidepoint(pg.mouse.get_pos()) and draw[4]==False:
        draw[4]=True
        drawX(215,215)
        ttt[1][1]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect6.collidepoint(pg.mouse.get_pos()) and draw[5]==False:
        draw[5]=True
        drawX(415,215)
        ttt[1][2]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect7.collidepoint(pg.mouse.get_pos()) and draw[6]==False:
        draw[6]=True
        drawX(15,415)
        ttt[2][0]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect8.collidepoint(pg.mouse.get_pos()) and draw[7]==False:
        draw[7]=True
        drawX(215,415)
        ttt[2][1]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
    elif rect9.collidepoint(pg.mouse.get_pos()) and draw[8]==False:
        draw[8]=True
        drawX(415,415)
        ttt[2][2]='X'
        checktictactoe()
        if(run==True):chanceforhardAI()
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.MOUSEBUTTONDOWN:
            mouseclicked()
    window.blit(textplayermode,(10,610))
    window.blit(textplayerwhichmode,(70,610))
    window.blit(textAIlevel,(470,610))
    window.blit(textAIwhichlevel,(530,610))
    pg.display.update()
    
                
            
