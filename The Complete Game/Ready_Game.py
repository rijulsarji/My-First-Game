import pygame
pygame.init()
win=pygame.display.set_mode((852,480))
pygame.display.set_caption('hello world')

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
time=pygame.time.Clock()
milsec=pygame.time.get_ticks()
score=0

b_sound=pygame.mixer.Sound('bullet.wav')
h_sound=pygame.mixer.Sound('hit.wav')
s_sound=pygame.mixer.Sound('shout.wav')
d_sound=pygame.mixer.Sound('ah_shitt.wav')

#music=pygame.mixer.music.load('bg_music.mp3')
#pygame.mixer.music.play(-1)

class player:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=10
        self.left=False
        self.right=False
        self.jump=False
        self.jumpcount=9
        self.walkcount=0
        self.standing=True
        self.hitbox=(self.x+20,self.y+12,22,55)
        
    def background(self):
        if self.walkcount+1>=27:
            self.walkcount=0
        if self.standing==False:
            if man.left==True:
                win.blit(walkLeft[self.walkcount//3],(man.x,man.y))
                self.walkcount+=1
            elif man.right==True:
                win.blit(walkRight[self.walkcount//3],(man.x,man.y))
                self.walkcount+=1
        else:
            if self.right==True:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+20,self.y+12,22,55)
        #pygame.draw.rect(win,(0,0,0),(self.x+20,self.y+12,self.width,self.height),2)

    def hit(self):
        self.jump=False
        self.jumpcount=9
        self.x=100
        self.y=400
        self.walkcount=0
        font1=pygame.font.SysFont('comicsans',25)
        font3=pygame.font.SysFont('comicsans',25)
        text=font1.render('-3',1,(255,0,0))
        text1=font3.render('YOU GOT HIT, YOU DUMBASS',1,(255,0,0))
        win.blit(text,(765,110))
        win.blit(text1,(280,110))
        pygame.display.update()
        d_sound.play()

        i=0
        while i<200:
            pygame.time.delay(10)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()

class enemy:
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.walkcount=0
        self.path=[self.x,self.end]
        self.vel=3
        self.hitbox=(self.x+20,self.y+5,47,750)
        self.health=10
        self.visible=True

    def draw(self):
        self.move()
        if self.visible==True:
            if self.walkcount+1>=33:
                self.walkcount=0

            if self.vel>0:
                win.blit(self.walkRight[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            else:
                win.blit(self.walkLeft[self.walkcount//3],(self.x,self.y))
                self.walkcount+=1
            self.hitbox=(self.x+20,self.y+5,47,750)
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-5,35,-5))
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-5,35-(35/9*(9-self.health)),-5))
            #pygame.draw.rect(win,(0,0,0),(self.x+20,self.y+5,self.width,self.height),2)


    def move(self):
        if self.vel>0:
            if self.x+self.vel<self.path[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkcount=0
        else:
            if self.x-self.vel>self.path[0]:
                self.x+=self.vel
            else:
                self.vel=self.vel*-1
                self.walkcount=0

    def hit(self):
        global score
        tem=0
        if self.health>0:
            self.health-=1
            score+=1
        else:
            self.visible=False
        
class motion:
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=20*facing

    def b_shape(self):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

def window():
    win.blit(bg,(0,0))
    sc_text=sc_font.render('Score: '+ str(score),1,(0,0,0))
    hit_text=hit_font.render('HIT!!',1,(0,0,0))
    #win.blit(hit_font,(420,70))
    win.blit(sc_text,(700,80))
    man.background()
    dushman.draw()
    for bullet in bullets:
        bullet.b_shape()
    pygame.display.update()

sc_font=pygame.font.SysFont('comicsans',30)
hit_font=pygame.font.SysFont('algerian',50,True)
man=player(100,400,22,55)
dushman=enemy(450,407,15,47,750)
shoot=0
temp=0
bullets=[]
run=True

while run==True:
    
    time.tick(30)
    
    if man.hitbox[1]<dushman.hitbox[1]+dushman.hitbox[3] and man.hitbox[1]+man.hitbox[3]>dushman.hitbox[1]:
        if man.hitbox[0]+man.hitbox[2]>dushman.hitbox[0] and man.hitbox[0]<dushman.hitbox[0]+dushman.hitbox[2]:
            if dushman.visible==True:
                man.hit()
                score-=3
                

    if shoot>0:
        shoot+=1
    if shoot>3:
        shoot=0
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    keys=pygame.key.get_pressed()

    for bullet in bullets:
        if bullet.y-bullet.radius<dushman.hitbox[1]+dushman.hitbox[3] and bullet.y+bullet.radius>dushman.hitbox[1]:
            if bullet.x+bullet.radius>dushman.hitbox[0] and bullet.x-bullet.radius<dushman.hitbox[0]+dushman.hitbox[2]:
                dushman.hit()
                if dushman.visible==True:
                    bullets.pop(bullets.index(bullet))
                if dushman.visible==True:
                    h_sound.play()
                elif dushman.visible==False and temp==0:
                    s_sound.play() #insert shout
                    temp+=1
                    
        if bullet.x<850 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
    


    if keys[pygame.K_SPACE] and shoot==0:
        b_sound.play()
        if man.left==True:
            facing=-1
        else:
            facing=1
            
        if len(bullets)<3:
            bullets.append(motion(round(man.x+20+man.width//2),round(man.y+17+man.height//2),8,(255,100,0),facing))
        shoot=1

    if keys[pygame.K_LEFT] and man.x>0:
        man.x-=man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif keys[pygame.K_RIGHT] and man.x<780:
        man.x+=man.vel
        man.left=False
        man.right=True
        man.standing=False
    else:
        man.standing=True

    if not(man.jump):
        if keys[pygame.K_UP]:
            man.jump=True
    else:
        if man.jumpcount>=-9:
            neg=1
            if man.jumpcount<=0:
                neg=-1
            man.y-=(man.jumpcount**2)*0.5*neg
            man.jumpcount-=1
        else:
            man.jump=False
            man.jumpcount=9
    window()
            
pygame.quit()
