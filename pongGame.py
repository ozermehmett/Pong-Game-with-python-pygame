import pygame, sys, random

pygame.init()

W, H= 600,600
b = 250

dxL = 280
dxR = 300
dyU = 280
dyD = 300
ball_dx = -1/8
ball_dy = -1/8

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
PURPLE = (148,0,211)

screen = pygame.display.set_mode((W,H))

pygame.draw.line(screen,GREEN,[250,500],[350,500],10)
pygame.display.update()

def sol(x):
    pygame.draw.line(screen,GREEN,[x,500],[x+100,500],10)
    pygame.display.update()

def sag(x):
    pygame.draw.line(screen,GREEN,[x,500],[x+100,500],10)
    pygame.display.update()

def Ball():#280e280 den dx*dy lik kare içine
    global dxL, dxR, dyU, dyD, b, ball_dx, ball_dy
    pygame.draw.ellipse(screen,BLACK,[dxL,dyU,20,20],0)
    if dxL < 0:
        dxL += 1/2
        ball_dx = -ball_dx
        
    if dxR > 560:
        dxR -= 1/2
        ball_dx = -ball_dx
        
    if dyU < 0:
        dyU += 1/2
        ball_dy = -ball_dy
        
    if dyD > 600:
        dyU -= 1/2
        ball_dy = -ball_dy
        
    if dyD > 455 and dxL > b and dxR < b+100:
        ball_dy = -ball_dy

    dyU += ball_dy
    dxL += ball_dx
    dxR = dxL-20
    dyD = dyU-20
    pygame.draw.ellipse(screen,PURPLE,[dxL,dyU,20,20],0)
    pygame.display.update()
    



Ball()
while True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    

    if keys[pygame.K_LEFT]:
        pygame.draw.line(screen,BLACK,[b,500],[b+100,500],10)
        b -= 1/2
        if b < 0:
            b = 0
        else:
            sol(b)
            Ball()
    elif keys[pygame.K_RIGHT]:
        pygame.draw.line(screen,BLACK,[b,500],[b+100,500],10)
        b += 1/2
        if b+100 > 600:
            b = 500
        else:
            sag(b)
            Ball()
    else:
        Ball()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
