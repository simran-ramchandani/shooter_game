import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("MY FIRST GAME YAYYYY!!!!")

icon=pygame.image.load("space_Shooter_game/img/alien4.png")
pygame.display.set_icon(icon)

# score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=20
def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

# game over
overfont=pygame.font.Font("freesansbold.ttf",52)
retry_font=pygame.font.Font("freesansbold.ttf",32)
def game_over_text():
    over_text=overfont.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(250,150))
    retry_text=retry_font.render("RETRY",True,(255,255,255))
    end_text=retry_font.render("END GAME",True,(255,255,255))
    retry_rect = retry_text.get_rect(topleft=(200, 300))
    end_rect = end_text.get_rect(topleft=(450, 300))

    # Add some padding for the squircles
    padding = 20
    retry_squircle = pygame.Rect(
        retry_rect.left - padding//2,
        retry_rect.top - padding//2,
        retry_rect.width + padding,
        retry_rect.height + padding)
    end_squircle = pygame.Rect(
        end_rect.left - padding//2,
        end_rect.top - padding//2,
        end_rect.width + padding,
        end_rect.height + padding
    )

    pygame.draw.rect(screen, (255,255,255), retry_squircle, width=2, border_radius=15)
    pygame.draw.rect(screen, (255,255,255), end_squircle, width=2, border_radius=15)

    screen.blit(retry_text, retry_rect.topleft)
    screen.blit(end_text, end_rect.topleft)
    return retry_squircle,end_squircle

#spaceship
spaceship=pygame.image.load("space_Shooter_game/img/spaceship.png")
spaceX=390
spaceY=530
spaceX_change=0
spaceY_change=0

def player(x,y):
    screen.blit(spaceship,(x,y))


#bullet
bullet=pygame.image.load("space_Shooter_game/img/bullet.png")
bulletX=390
bulletY=530
bulletX_change=0
bulletY_change=0.4
state=False

def fire_bullet(x,y):
    global state
    screen.blit(bullet,(x+22,y+10))
    state=True

#alien

alien1=pygame.image.load("space_Shooter_game/img/alien1.png")  
alien2=pygame.image.load("space_Shooter_game/img/alien2.png")  
alien3=pygame.image.load("space_Shooter_game/img/alien3.png")  
alien4=pygame.image.load("space_Shooter_game/img/alien4.png")  
alien5=pygame.image.load("space_Shooter_game/img/alien5.png")  
num_of_aliens=5
alien_list=[alien1,alien2,alien3,alien4,alien5]
alienX=[]
alienY=[]
alienX_change=[]
alienY_change=[]

for i in range(num_of_aliens):
    alienX.append(random.randint(20,737))
    alienY.append(random.randint(30,130))
    alienX_change.append(random.uniform(0.005,0.8))
    alienY_change.append(0)
    
    def alien(x,y):
        screen.blit(alien_list[i],(x,y))    

#explosions
explosion1=pygame.image.load("space_Shooter_game/img/exp1.png")
explosion2=pygame.image.load("space_Shooter_game/img/exp2.png")
explosion3=pygame.image.load("space_Shooter_game/img/exp3.png")
explosion4=pygame.image.load("space_Shooter_game/img/exp4.png")
explosion5=pygame.image.load("space_Shooter_game/img/exp5.png")

def explode(x,y):
    screen.blit(explosion1,(x,y))
    screen.blit(explosion2,(x,y))
    screen.blit(explosion3,(x,y))
    screen.blit(explosion4,(x,y))
    screen.blit(explosion5,(x,y))



running=True
while running:    
    screen.fill((138, 154, 91))
    show_score(textX,textY)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                spaceX_change=-0.5
            elif event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                spaceX_change=0.5
            #elif event.key==pygame.K_UP or event.key==pygame.K_w:
            #    spaceY_change=-0.5
            #elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
            #    spaceY_change=0.5
            elif event.key==pygame.K_SPACE:
                bulletX=spaceX
                fire_bullet(bulletX,bulletY)
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_a or event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                spaceX_change=0
            #elif event.key==pygame.K_UP or event.key==pygame.K_w or event.key==pygame.K_DOWN or event.key==pygame.K_s:
                #spaceY_change=0
        
        
        
    # explode
    for i in range(num_of_aliens):
        dist=((bulletX-alienX[i])**2 +(bulletY-alienY[i])**2)**0.5
        
        if dist<50:
            explode(bulletX,bulletY)
            score_value+=100
            alienX[i]=random.randint(20,737)
            alienY[i]=100
            bulletX=390
            bulletY=530
            state=False
    
        
    # spaceship boundaries
    if spaceX<50:
        spaceX=50
    if spaceX>750:
        spaceX=750
    if spaceY<20:
        spaceY=20
    if spaceY>580:
        spaceY=580
    
    # alien motion
    for i in range(num_of_aliens):
        if alienX[i]<=0:
            alienX_change[i]=0.2
            alienY[i]+=30
        elif alienX[i]>=738:
            alienX_change[i]=-0.2
            alienY[i]+=30
        alienY[i]+=alienY_change[i]
        alienX[i]+=alienX_change[i]
        alien(alienX[i],alienY[i])
    

    
    # spaceship motion
    spaceX+=spaceX_change
    spaceY+=spaceY_change
    player(spaceX,spaceY)       
    
    # bullet motion
    
    if state==True:
        bulletY-=bulletY_change
        fire_bullet(bulletX,bulletY)
    if bulletY<=0:
        bulletY=530
        state=False
        
    # bullet s[eed
    if score_value>1000:
        bulletY_change=0.6
    elif score_value>5000:
        bulletY_change=0.8
    elif score_value>10000:
        bulletY_change=1
        
        
     # game lost
    for i in range(num_of_aliens):
        if alienY[i]>=450:
            for j in range(num_of_aliens):
                alienY[j]=2000
            retry_rect, end_rect = game_over_text()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if retry_rect.collidepoint(mx, my):
                        
                        score_value = 0
                        # Reset positions, etc.
                    elif end_rect.collidepoint(mx, my):
                        running = False 
    
    pygame.display.update()