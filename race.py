import pygame
import time
import random
pygame.init()
gray=(119,118,110)
black=(0,0,0)
dis_width=800
dis_height=600
gamedisplay=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
carImg=pygame.image.load("car1.png")
carImg=pygame.transform.scale(carImg, (100, 180))
bgImg=pygame.image.load("road1way.jpg")
car_width=100

red=(255,0,0)

def score_system(noOfCars,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed"+str(noOfCars),True,black)
    score=font.render("score"+str(noOfCars),True,red)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))


def obstacle(obs_startX,obs_startY,obs):
    if obs==0:
        obs_pic=pygame.image.load("car1.png")
    elif obs==1:
        obs_pic=pygame.image.load("car2.png")   
    elif obs==2:
        obs_pic=pygame.image.load("car3.png")   
    elif obs==3:
        obs_pic=pygame.image.load("car4.png")   

    obs_pic=pygame.transform.scale(obs_pic, (80, 150))
    gamedisplay.blit(obs_pic,(obs_startX,obs_startY))

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()


def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",70)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((dis_width/2),(dis_height/2))
    gamedisplay.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display("You Crashed!!!")


def bg():
    gamedisplay.blit(bgImg,(110,0))
    gamedisplay.blit(bgImg,(110,200))
    gamedisplay.blit(bgImg,(110,400))
    gamedisplay.blit(bgImg,(310,0))
    gamedisplay.blit(bgImg,(310,200))
    gamedisplay.blit(bgImg,(310,400))
    gamedisplay.blit(bgImg,(510,0))
    gamedisplay.blit(bgImg,(510,200))
    gamedisplay.blit(bgImg,(510,400))


def car(x,y):
    gamedisplay.blit(carImg,(x,y))

def game_loop():
    x=(dis_width*0.45)
    y=(dis_height*0.6)
    x_change=0
    #obstacles
    obst_speed=9
    obs=0
    y_change=0
    obs_startX=random.randrange(200,(dis_width-200))
    obs_startY=-750
    obs_width=80
    obs_height=125
    #score and level
    noOfCars=0
    level=0
    score=0
    y2=7

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                #bumped=True
                quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-5
            if event.key==pygame.K_RIGHT:
                x_change=5
            if event.key==pygame.K_UP:
                obst_speed=2
            if event.key==pygame.K_DOWN:
                obst_speed=-2      
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_change=0

        x+=x_change
        #obs_startY+=obst_speed
        gamedisplay.fill(gray)

        bg()
        obs_startY-=(obst_speed/4)
        obstacle(obs_startX,obs_startY,obs)
        obs_startY+=obst_speed
        car(x,y)
        score_system(noOfCars,score)
        if x>710-car_width or x<100:
            crash()
        if x>dis_width-(car_width+100) or x<100:
            crash()
        if obs_startY>dis_height:
            obs_startY=0-obs_height
            obs_startX=random.randrange(170,(dis_width-170))
            obs=random.randrange(0,4)
            noOfCars+=1
            score=noOfCars+1
            if int(noOfCars%10)==0:
                level+=1
                obst_speed+=2
                largetext=pygame.font.Font("freesansbold.ttf",70)
                textsurf,textrect=text_objects("level"+str(level),largetext)
                textrect.center=((dis_width/2),(dis_height/2))
                gamedisplay.blit(textsurf,textrect)
                pygame.display.update()
                time.sleep(2)


        if y < obs_startY+obs_height:
            if x > obs_startX and x < obs_startX+obs_width-10 or x+car_width > obs_startX and x+car_width < obs_startX+obs_width:
                crash()     

            
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()                