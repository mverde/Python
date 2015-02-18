import sys, pygame, random, time
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'

pygame.init()
random.seed()

size = (width, height) = (640, 480)
screen = pygame.display.set_mode(size)
blocks = []
blockValues = [((640, 0, 30, 150), (640, 300, 30, 180)), ((640, 0, 30, 75), (640, 225, 255))]
black = (0,0,0)
goingUp = False
fallVel = 5
score = 48
defFont = pygame.font.get_default_font()
font = pygame.font.Font(defFont, 36)

bird = [70, 120, 20, 20]

def move(player, velocity):
    if velocity > 0:    #going down
        if player[1] < 470:
            player[1] = player[1] + (velocity/100)
        else:
            player[1] = 470
    elif velocity < 0:  #going up
        if player[1] > 10:
            player[1] = player[1] + (velocity/60)
        else:
            player[1] = 10
            velocity = 0
    else:
        velocity = 200

def genBlock():
    rand = random.randint(0, 1)
    print rand
    block = [[blockValues[rand][0][0], blockValues[rand][0][1], blockValues[rand][0][2], blockValues[rand][0][3]], [blockValues[rand][1][0], blockValues[rand][1][1], blockValues[rand][1][2], blockValues[rand][1][3]]]
    blocks.insert(0, block)

def drawScore():
    text = font.render(chr(score), 0, (255, 255, 255))
    textpos = text.get_rect(centerx=screen.get_width()/2)
    screen.blit(text, textpos)

def drawBlocks():
    if blocks[0][0][0] < -30:
        blocks.pop()
    if not blocks:
        genBlock()
        
    blocks[0][0][0] = blocks[0][0][0] - 1
    blocks[0][1][0] = blocks[0][1][0] - 1
    pygame.draw.rect(screen, (0, 255, 0), (blocks[0][0][0] - 1, blocks[0][0][1], blocks[0][0][2], blocks[0][0][3]), 3)
    pygame.draw.rect(screen, (0, 255, 0), (blocks[0][1][0] - 1, blocks[0][1][1], blocks[0][1][2], blocks[0][1][3]), 3)

temp = False

while 1:
    screen.fill(black)

    if bird[1] == 470:
        print 'You lose! score:', chr(score)
        pygame.quit()
        sys.exit()

    if temp == False:
        temp = True
        genBlock()
        
    pygame.draw.rect(screen, (255, 0, 0), (bird[0], bird[1], bird[2], bird[3]), 3)
    drawScore()
    drawBlocks()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            goingUp = True
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()

    move(bird, fallVel)
    
    if goingUp == True:
        fallVel = -350
        goingUp = False
    else:
        fallVel = fallVel + 10
        
    time.sleep(.0075)
    pygame.display.flip()
    
        
