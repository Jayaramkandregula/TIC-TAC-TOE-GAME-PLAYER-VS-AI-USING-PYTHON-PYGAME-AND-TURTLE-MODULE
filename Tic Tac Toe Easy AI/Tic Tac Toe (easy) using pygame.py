import pygame as pg
import random
pg.init()
window=pg.display.set_mode((600,670))
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
#texts
smallfont=pg.font.SysFont('Corbel',17)
bigfont=pg.font.SysFont('Corbel',40)
textplayermode=smallfont.render('MODE : ',True,textplayermodecolor)
textplayerwhichmode=smallfont.render('PLAYER vs AI',True,textplayerwhichmodecolor)
textAIlevel=smallfont.render('LEVEL : ',True,textAIlevelcolor)
textAIwhichlevel=smallfont.render('EASY',True,textAIwhichlevelcolor)
textwinnerisplayer=bigfont.render("YOU HAVE WON THE GAME",True,textwincolor)
textwinnerisAI=bigfont.render("MY AI HAVE WON THE GAME",True,textwincolor)
textmatchdrawn=bigfont.render("THE GAME IS DRAWN",True,textwincolor)
draw=[False,False,False,False,False,False,False,False,False]
run=True

count=0

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

def chanceforAI():
    row=random.randint(0,2)
    col=random.randint(0,2)
    if(run==True):
        while(ttt[row][col]=='X' or ttt[row][col]=='O'):
            row=random.randint(0,2)
            col=random.randint(0,2)
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

'''
def mouseclicked():
    if rect1.collidepoint(
    '''
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.MOUSEBUTTONDOWN:
            if rect1.collidepoint(event.pos) and draw[0]==False :
                draw[0]=True
                drawX(15,15)
                ttt[0][0]='X'
                checktictactoe();chanceforAI()
            elif rect2.collidepoint(event.pos) and draw[1]==False:
                draw[1]=True
                drawX(215,15)
                ttt[0][1]='X'
                checktictactoe();chanceforAI()
            elif rect3.collidepoint(event.pos) and draw[2]==False:
                draw[2]=True
                drawX(415,15)
                ttt[0][2]='X'
                checktictactoe();chanceforAI()
            elif rect4.collidepoint(event.pos) and draw[3]==False:
                draw[3]=True
                drawX(15,215)
                ttt[1][0]='X'
                checktictactoe();chanceforAI()
            elif rect5.collidepoint(event.pos) and draw[4]==False:
                draw[4]=True
                drawX(215,215)
                ttt[1][1]='X'
                checktictactoe();chanceforAI()
            elif rect6.collidepoint(event.pos) and draw[5]==False:
                draw[5]=True
                drawX(415,215)
                ttt[1][2]='X'
                checktictactoe();chanceforAI()
            elif rect7.collidepoint(event.pos) and draw[6]==False:
                draw[6]=True
                drawX(15,415)
                ttt[2][0]='X'
                checktictactoe();chanceforAI()
            elif rect8.collidepoint(event.pos) and draw[7]==False:
                draw[7]=True
                drawX(215,415)
                ttt[2][1]='X'
                checktictactoe();chanceforAI()
            elif rect9.collidepoint(event.pos) and draw[8]==False:
                draw[8]=True
                drawX(415,415)
                ttt[2][2]='X'
                checktictactoe();chanceforAI()
    window.blit(textplayermode,(10,610))
    window.blit(textplayerwhichmode,(70,610))
    window.blit(textAIlevel,(470,610))
    window.blit(textAIwhichlevel,(530,610))
    pg.display.update()
        
            
