import pygame as pg
import random
pg.init()
window=pg.display.set_mode((1080,2400))
pg.display.set_caption("TIC TAC TOE")
rect1=pg.Rect(94,754,292,292)
rect2=pg.Rect(394,754,292,292)
rect3=pg.Rect(694,754,292,292)
rect4=pg.Rect(94,1054,292,292)
rect5=pg.Rect(394,1054,292,292)
rect6=pg.Rect(694,1054,292,292)
rect7=pg.Rect(94,1354,292,292)
rect8=pg.Rect(394,1354,292,292)
rect9=pg.Rect(694,1354,292,292)
#color
bgcolor=(0,0,0)
boardcolor=(255,255,255)
xcolor=(135,206,235)
ocolor=(144,238,144)
textplayermodecolor=(120,120,120)
textplayerwhichmodecolor=(120,0,1)
textAIlevelcolor=(120,120,120)
textAIwhichlevelcolor=(120,0,1)
textwincolor=(120,80,12)
strikecolor=(205,25,26)

ttt=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
choice="X"
#texts
smallfont=pg.font.SysFont('Corbel',40)
bigfont=pg.font.SysFont('Corbel',80)
textplayermode=smallfont.render('MODE : ',True,textplayermodecolor)
textplayerwhichmode=smallfont.render('PLAYER vs JET AI',True,textplayerwhichmodecolor)
textAIlevel=smallfont.render('LEVEL : ',True,textAIlevelcolor)
textAIwhichlevel=smallfont.render('EASY',True,textAIwhichlevelcolor)
textwinnerisplayer=bigfont.render("YOU HAVE WON THE GAME",True,textwincolor)
textwinnerisAI=bigfont.render("JET AI HAVE WON THE GAME",True,textwincolor)
textmatchdrawn=bigfont.render("THE GAME IS DRAWN",True,textwincolor)
draw=[False,False,False,False,False,False,False,False,False]
run=True

count=0

def drawline(index):
    if index==0:pg.draw.line(window,strikecolor,[90,900],[990,900],10)
    elif index==1:pg.draw.line(window,strikecolor,[90,1200],[990,1200],10)
    elif index==2:pg.draw.line(window,strikecolor,[90,1500],[990,1500],10)
    elif index==3:pg.draw.line(window,strikecolor,[240,750],[240,1650],10)
    elif index==4:pg.draw.line(window,strikecolor,[540,750],[540,1650],10)
    elif index==5:pg.draw.line(window,strikecolor,[840,750],[840,1650],10)
    elif index==6:pg.draw.line(window,strikecolor,[90,750],[990,1650],10)
    elif index==7:pg.draw.line(window,strikecolor,[990,750],[90,1650],10)
    pg.display.update()
    
def checktictactoe():
    global count
    global run
    count=count+1
    check=[[ttt[0][0],ttt[0][1],ttt[0][2]],[ttt[1][0],ttt[1][1],ttt[1][2]],[ttt[2][0],ttt[2][1],ttt[2][2]],[ttt[0][0],ttt[1][0],ttt[2][0]],[ttt[0][1],ttt[1][1],ttt[2][1]],[ttt[0][2],ttt[1][2],ttt[2][2]],[ttt[0][0],ttt[1][1],ttt[2][2]],[ttt[0][2],ttt[1][1],ttt[2][0]]]
    if((['X','X','X'] in check)or(['O','O','O'] in check)):
        if(['X','X','X'] in check):
            drawline(check.index(['X','X','X']))
            window.blit(textwinnerisplayer,(150,1720))
            pg.display.update()
            pg.time.wait(10000)
            run=False
        elif(['O','O','O'] in check):
            drawline(check.index(['O','O','O']))
            window.blit(textwinnerisAI,(150,1720))
            pg.display.update()
            pg.time.wait(10000)
            run=False
    elif(count>=9):
        window.blit(textmatchdrawn,(200,1720))
        pg.display.update()
        pg.time.wait(10000)
        run=False
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
    pg.draw.rect(window,boardcolor,(90,750,900,900),20)
    pg.draw.line(window,boardcolor,[92,1050],[988,1050],20)
    pg.draw.line(window,boardcolor,[92,1350],[988,1350],20)
    pg.draw.line(window,boardcolor,[390,752],[390,1648],20)
    pg.draw.line(window,boardcolor,[690,752],[690,1648],20)
    pg.display.update()
drawboard()

def drawX(x,y):
    pg.draw.line(window,xcolor,[x,y],[x+240,y+240],30)
    pg.draw.line(window,xcolor,[x+240,y],[x,y+240],30)
    pg.display.update()
def drawO(x,y):
    pg.draw.circle(window,ocolor,[x,y],125,30)
    pg.display.update()

def chanceforAI():
    row=random.randint(0,2)
    col=random.randint(0,2)
    if(run==True):
        while(ttt[row][col]=='X' or ttt[row][col]=='O'):
            row=random.randint(0,2)
            col=random.randint(0,2)
        ttt[row][col]='O'
        if(row==0 and col==0):drawO(240,900);draw[0]=True
        elif(row==0 and col==1):drawO(540,900);draw[1]=True
        elif(row==0 and col==2):drawO(840,900);draw[2]=True
        elif(row==1 and col==0):drawO(240,1200);draw[3]=True
        elif(row==1 and col==1):drawO(540,1200);draw[4]=True
        elif(row==1 and col==2):drawO(840,1200);draw[5]=True
        elif(row==2 and col==0):drawO(240,1500);draw[6]=True
        elif(row==2 and col==1):drawO(540,1500);draw[7]=True
        elif(row==2 and col==2):drawO(840,1500);draw[8]=True
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
                drawX(120,780)
                ttt[0][0]='X'
                checktictactoe();chanceforAI()
            elif rect2.collidepoint(event.pos) and draw[1]==False:
                draw[1]=True
                drawX(420,780)
                ttt[0][1]='X'
                checktictactoe();chanceforAI()
            elif rect3.collidepoint(event.pos) and draw[2]==False:
                draw[2]=True
                drawX(720,780)
                ttt[0][2]='X'
                checktictactoe();chanceforAI()
            elif rect4.collidepoint(event.pos) and draw[3]==False:
                draw[3]=True
                drawX(120,1080)
                ttt[1][0]='X'
                checktictactoe();chanceforAI()
            elif rect5.collidepoint(event.pos) and draw[4]==False:
                draw[4]=True
                drawX(420,1080)
                ttt[1][1]='X'
                checktictactoe();chanceforAI()
            elif rect6.collidepoint(event.pos) and draw[5]==False:
                draw[5]=True
                drawX(720,1080)
                ttt[1][2]='X'
                checktictactoe();chanceforAI()
            elif rect7.collidepoint(event.pos) and draw[6]==False:
                draw[6]=True
                drawX(120,1380)
                ttt[2][0]='X'
                checktictactoe();chanceforAI()
            elif rect8.collidepoint(event.pos) and draw[7]==False:
                draw[7]=True
                drawX(420,1380)
                ttt[2][1]='X'
                checktictactoe();chanceforAI()
            elif rect9.collidepoint(event.pos) and draw[8]==False:
                draw[8]=True
                drawX(720,1380)
                ttt[2][2]='X'
                checktictactoe();chanceforAI()
    window.blit(textplayermode,(100,1670))
    window.blit(textplayerwhichmode,(210,1670))
    window.blit(textAIlevel,(800,1670))
    window.blit(textAIwhichlevel,(920,1670))
    pg.display.update()
        
            
