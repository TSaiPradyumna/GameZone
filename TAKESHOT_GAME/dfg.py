import pygame
from pygame import *
from pygame import mixer
import time
import os
import sys
import random
pygame.init()
# mixer.init()
# pygame.mixer.init()


# mixer.music.load("crunch.wav")
# mixer.music.load("Fruit Ninja - Theme Song.wav")
# mixer.music.load("kill_knife.wav")




r=g=b=255   
W,H=800,800
WIN=pygame.display.set_mode((W,H))
FPS=24
clock=pygame.time.Clock()
pygame.display.set_caption('TAKESHOT_GAME')
hitlist=[]

# importing images


player_image = pygame.image.load("download.png")
scaled_player_image=pygame.transform.scale(player_image,(100,90))
image_rect1=scaled_player_image.get_rect()

bullet_image = pygame.image.load("white rocket_3.jpg")
scaled_bullet_image=pygame.transform.scale(bullet_image,(20,20))
# rotated_bullet_image=pygame.transform.rotate(bullet_image,90)
image_rect2=scaled_bullet_image.get_rect()

mob_image= pygame.image.load("flying villian 3 left.png")
scaled_mob_image=pygame.transform.scale(mob_image,(60,50))
image_rect3=scaled_mob_image.get_rect()

mob1_image= pygame.image.load("flying villian 3 left.png")
scaled_mob1_image=pygame.transform.scale(mob1_image,(70,50))
image_rect4=scaled_mob1_image.get_rect()

mob2_image= pygame.image.load("flying villian 2 left.png")
scaled_mob2_image=pygame.transform.scale(mob2_image,(90,50))
image_rect5=scaled_mob2_image.get_rect()

mob3_image= pygame.image.load("flying villian 3.png")
scaled_mob3_image=pygame.transform.scale(mob3_image,(90,50))
image_rect6=scaled_mob3_image.get_rect()


Gmob_image= pygame.image.load("coin_1.jpg")
scaled_Gmob_image=pygame.transform.scale(Gmob_image,(60,50))
image_rect6=scaled_Gmob_image.get_rect()


image3 = pygame.image.load("saturn base.bmp")
scaled_image3=pygame.transform.scale(image3,(800,800))

f_1= pygame.image.load("black asteroid_1.png")
scaled_f1_image=pygame.transform.scale(f_1,(50,50))
image_f1=scaled_f1_image.get_rect()

f_2= pygame.image.load("black asteroid_3.png")
scaled_f2_image=pygame.transform.scale(f_2,(50,50))
image_f2=scaled_f2_image.get_rect()

f_3= pygame.image.load("black asteroid_5.png")
scaled_f3_image=pygame.transform.scale(f_3,(50,50))
image_f3=scaled_f3_image.get_rect()

f_4= pygame.image.load("black asteroid_6.png")
scaled_f4_image=pygame.transform.scale(f_4,(50,50))
image_f4=scaled_f4_image.get_rect()


lives_image = pygame.image.load("heart.png")
scaled_lives_image=pygame.transform.scale(lives_image,(100,90))
image_rectl1=scaled_lives_image.get_rect()


# importing font
font1_name=pygame.font.match_font("Forte")
font2_name=pygame.font.match_font("Forte")
# importing music
# shoot_song =pygame.mixer.Sound("new12.mp3")
# bullet_hittomob_song =pygame.mixer.Sound("jump.mp3")


def draw():
    
        WIN.fill((255, 0, 0))
        WIN.blit(scaled_image3, (0, 0))
        # WIN.blit(scaled_player_image,image_rect1)
        # WIN.blit(scaled_bullet_image,image_rect2)
        # WIN.blit(scaled_mob_image,image_rect3)

def draw_text(surface,text,size,x,y):
    font=pygame.font.Font(font1_name,size)
    text1=font.render(text,True,"WHITE")
    text_rect = text1.get_rect()
    text_rect.midtop =(x,y)
    surface.blit(text1,text_rect)


# def collison():
#     if pygame.sprite.spritecollide(player01,mobs,True):
#         os.system("python p3.py")

class Player01(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_player_image
        self.image.set_colorkey("BLACK")
        # self.image = pygame.Surface((70,50))
        # self.image.fill("YELLOW")
        self.rect=self.image.get_rect()
        self.rect.centerx=W/2
        # self.rect.centery=H/2
        self.rect.bottom = H -10
        self.speedx =0
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()


    def update(self):
        self.speedx=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_KP_ENTER]:
            self.shoot()
        if keystate[pygame.K_LEFT]:
            self.speedx=-8
        if keystate[pygame.K_RIGHT]:
            self.speedx=8
        self.rect.x+=self.speedx
        if self.rect.right>W:
            self.rect.right=W
        if self.rect.left<0:
            self.rect.left=0


    def shoot(self):
            bullet =Bullets(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot =now
            # shoot_song.play()

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_mob_image
        self.image.set_colorkey("WHITE")
        # self.radius=int(self.rect.width* .85 /2)
        # self.image = pygame.Surface((20,20))
        # self.image.fill("BLACK")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(W - self.rect.width)
        self.rect.y=random.randrange(-5,-4)
        self.speedy = random.randrange(1,15)
        self.speedx = random.randrange(-4,4)

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > H+10 or self.rect.left<-50 or self.rect.right>W+70:
            self.rect.x=random.randrange(W - self.rect.width)
            self.rect.y=random.randrange(-4,4)
            self.speedy = random.randrange(1,15)

class Mob1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_mob1_image
        self.image.set_colorkey("WHITE")
        # self.radius=int(self.rect.width* .85 /2)
        # self.image = pygame.Surface((20,20))
        # self.image.fill("BLACK")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(W - self.rect.width)
        self.rect.y=random.randrange(-5,-4)
        self.speedy = random.randrange(1,15)
        self.speedx = random.randrange(-4,4)

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > H+10 or self.rect.left<-50 or self.rect.right>W+70:
            self.rect.x=random.randrange(W - self.rect.width)
            self.rect.y=random.randrange(-4,4)
            self.speedy = random.randrange(1,15)


class Mob2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_mob2_image
        self.image.set_colorkey("WHITE")
        # self.radius=int(self.rect.width* .85 /2)
        # self.image = pygame.Surface((20,20))
        # self.image.fill("BLACK")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(W - self.rect.width)
        self.rect.y=random.randrange(-5,-4)
        self.speedy = random.randrange(1,15)
        self.speedx = random.randrange(-4,4)

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > H+10 or self.rect.left<-50 or self.rect.right>W+70:
            self.rect.x=random.randrange(W - self.rect.width)
            self.rect.y=random.randrange(-4,4)
            self.speedy = random.randrange(1,15)


class Mob3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_mob3_image
        self.image.set_colorkey("WHITE")
        # self.radius=int(self.rect.width* .85 /2)
        # self.image = pygame.Surface((20,20))
        # self.image.fill("BLACK")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(W - self.rect.width)
        self.rect.y=random.randrange(-5,-4)
        self.speedy = random.randrange(1,15)
        self.speedx = random.randrange(-4,4)

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > H+10 or self.rect.left<-50 or self.rect.right>W+70:
            self.rect.x=random.randrange(W - self.rect.width)
            self.rect.y=random.randrange(-4,4)
            self.speedy = random.randrange(1,15)


class GMob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_Gmob_image
        self.image.set_colorkey("WHITE")
        # self.image = pygame.Surface((20,20))
        # self.image.fill("WHITE")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(W - self.rect.width)
        self.rect.y=random.randrange(-5,-4)
        self.speedy = random.randrange(1,5)
        self.speedx = random.randrange(-2,2)

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > H+10:
            self.rect.x=random.randrange(W - self.rect.width)
            self.rect.y=random.randrange(-2,2)
            self.speedy = random.randrange(1,35)

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_bullet_image
        self.image.set_colorkey((255,255,255))
        # self.image = pygame.Surface((10,15))
        # self.image.fill("YELLOW")
        self.rect=self.image.get_rect()
        self.rect.bottom =y
        self.rect.centerx=x
        self.rect.centery=y
        self.speedy=-10

    def update(self):
        self.rect.y+=self.speedy
        # bullet_hittomob_song.play()
        if self.rect.bottom<0:
            self.kill()

class Lives(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_lives_image
        self.image.set_colorkey("WHITE")
        # self.image = pygame.Surface((20,20))
        # self.image.fill("WHITE")
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(W - self.rect.width)
        self.rect.y=random.randrange(-5,-4)
        self.speedy = random.randrange(1,15)
        self.speedx = random.randrange(-2,20)

    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top > H+10:
            self.rect.x=random.randrange(W - self.rect.width)
            self.rect.y=random.randrange(-2,20)
            self.speedy = random.randrange(1,15)

def show_gamestart():
    draw_text(WIN,"GAME TAKE_SHOT",60,W/2,H/2) 
    draw_text(WIN,"LEFT ARROW AND RIGHT ARROW ARE THERE TO MOVE THE SPACESHIP , ENTER BUTTON IS FOR FIRING",15,W/2,H/2) 
    draw_text(WIN,"Press any key to Start the Game",17,W/2,H*3/8) 
    pygame.display.flip()
    waiting =True
    while waiting:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.KEYUP:
                waiting =False

# def collison():
#     if pygame.sprite.groupcollide(bullets,mobs1,False):
#         score+=20 

game_start =True
game_over =True
running = True
while running:
    if game_start:
        show_gamestart()
        game_start =False
        all_sprites=pygame.sprite.Group()
        mobs=pygame.sprite.Group() 
        mobs1=pygame.sprite.Group() 
        mobs01=pygame.sprite.Group() 
        mobs02=pygame.sprite.Group() 
        mobs03=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        player01=Player01()
        lives01=pygame.sprite.Group()
        all_sprites.add(player01)
        lives1 =Lives()
        all_sprites.add(lives1)
        for i in range(2):
            m=Mob()
            all_sprites.add(m)
            mobs.add(m)
            score=0 
        for i in range(3):
            m1=GMob()
            all_sprites.add(m1)
            mobs1.add(m1)
        for i in range(4):
            m01=Mob1()
            all_sprites.add(m01)
            mobs01.add(m01)
        for i in range(2):
            m02=Mob2()
            all_sprites.add(m02)
            mobs02.add(m02)
        for i in range(3):
            m03=Mob3()
            all_sprites.add(m03)
            mobs03.add(m03)
        for i in range(3):
            l01=Lives()
            all_sprites.add(l01)
            lives01.add(l01)
        else:
            game_start = False
        all_sprites.update()

    clock.tick(FPS)
    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    all_sprites.update()

    # if bullet hits mob
    hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        score+=5
        m=Mob()
        all_sprites.add(m)
        mobs.add(m)
        # mixer.music.play()
    hits01=pygame.sprite.groupcollide(mobs01,bullets,True,True)
    for hit in hits:
        
        score+=5
        m01=Mob1()
        all_sprites.add(m01)
        mobs01.add(m01)
    hits02=pygame.sprite.groupcollide(mobs02,bullets,True,True)
    for hit in hits:
        score+=5
        m02=Mob2()
        all_sprites.add(m02)
        mobs02.add(m02)
    hits03=pygame.sprite.groupcollide(mobs03,bullets,True,True)
    for hit in hits:
        score+=5
        m03=Mob3()
        all_sprites.add(m03)
        mobs03.add(m03)
    Ghits=pygame.sprite.groupcollide(mobs1,bullets,True,True)
    for Ghit in Ghits:
        score+=100
        m1=GMob()
        all_sprites.add(m1)
        mobs1.add(m1)
    G01hits=pygame.sprite.groupcollide(lives01,bullets,True,True)
    for Ghit in Ghits:
        score+=100
        l01=Lives()
        all_sprites.add(l01)
        lives01.add(l01)





# hits supercollide
    # G_hits =pygame.sprite.spritecollide(bullets,mobs1,True) 
    B_hits =pygame.sprite.spritecollide(player01,mobs,True) 
    B01_hits =pygame.sprite.spritecollide(player01,mobs01,True) 
    B02_hits =pygame.sprite.spritecollide(player01,mobs02,True) 
    B03_hits =pygame.sprite.spritecollide(player01,mobs03,True) 

    l=len(hitlist)
    hitlist.extend(B_hits)
    hitlist.extend(B01_hits)
    hitlist.extend(B02_hits)
    hitlist.extend(B03_hits)
    if hitlist:
        if G01hits:
            hitlist.pop()
            G01hits.pop()
    if l>=3:
        running = False
        show_gamestart

        os.system("python takeshot_game_final.py")
        break

    draw()
    # collison()
    all_sprites.draw(WIN)

    draw_text(WIN,str(score),25,W/2,20)
    pygame.display.update()



