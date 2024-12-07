import pygame
import random
import math
import os 
import sys
pygame.init()
clock=pygame.time.Clock()
fps=100
width=394
height=448
win=pygame.display.set_mode((width,height))
back=pygame.image.load(r'E:\MAIN_INTERFACE\MINIMILITIA\junkyard.png')
pygame.display.set_caption("MINI MILITIA")
g=10
t=1/fps
# scaled_back=pygame.transform.scale(back,(width,height))



player_image = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\right.jpg")
scaled_player_image=pygame.transform.scale(player_image,(30,30))
rotated_right_player_image1=pygame.transform.rotate(scaled_player_image,0)
image_rect1=scaled_player_image.get_rect()
r_image_rect1=rotated_right_player_image1.get_rect()

player_image2 = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\left.png")
scaled_player_image2=pygame.transform.scale(player_image2,(30,30))
image_rect2=scaled_player_image2.get_rect()

bullet_image = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\bullet5.bmp")
scaled_bullet_image=pygame.transform.scale(bullet_image,(20,10))
# rotated_bullet_image=pygame.transform.rotate(bullet_image,90)
image_rect2=scaled_bullet_image.get_rect()

player_image3 = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\villan.jpg")
scaled_player_image3=pygame.transform.scale(player_image3,(30,30))
rotated_right_player_image3=pygame.transform.rotate(scaled_player_image3,0)
image_rect3=scaled_player_image3.get_rect()
r_image_rect3=rotated_right_player_image3.get_rect()

player_image4 = pygame.image.load(r"E:\MAIN_INTERFACE\MINIMILITIA\vil_left.png")
scaled_player_image4=pygame.transform.scale(player_image4,(30,30))
image_rect4=scaled_player_image4.get_rect()

up_walls_coord=[[(93,150),(200,150)],
[(200,175),(240,175)],
[(301,150),(350,150)],
[(122,305),(148,305)],
[(148,328),(192,315)],
[(192,305),(318,305)],
[(40,48),(350,48)]]
down_walls_coord=[[(96,101),(240,101)],
[(301,105),(350,105)],
[(122,258),(200,256)],
[(200,235),(240,235)],
[(241,256),(301,258)],
[(40,416),(350,416)]]
left_walls_coord=[[(240,105),(240,172)],
[(40,50),(40,414)],
[(301,260),(318,303)],
[(192,307),(192,313)],
[(240,237),(241,254)]]
right_walls_coord=[[(96,105),(96,148)],
[(301,107),(301,148)],
[(200,152),(200,173)],
[(200,240),(200,254)],
[(122,260),(122,303)],
[(148,307),(148,326)],
[(350,50),(350,414)]]


font1_name=pygame.font.match_font("Forte")
font2_name=pygame.font.match_font("Forte")


#----------------------------------classes------------------------------------# 
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=back
        self.rect=self.image.get_rect()


def draw_text(surface,text,size,x,y):
    font=pygame.font.Font(font1_name,size)
    text1=font.render(text,True,"WHITE")
    text_rect = text1.get_rect()
    text_rect.midtop =(x,y)
    surface.blit(text1,text_rect)

class Line(pygame.sprite.Sprite):
    def __init__(self,x,y,widthl,heightl):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((widthl,heightl))
        self.image.fill((255,0,0))
        self.image.set_colorkey((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=x[0]
        self.rect.y=x[1]


class Player01(pygame.sprite.Sprite):
    def __init__(self):
        global mode
        pygame.sprite.Sprite.__init__(self)
        self.image = rotated_right_player_image1
        self.rect=self.image.get_rect()
        self.rect.centerx=10
        self.rect.centery=448
        self.rect.bottom = 448
        self.speedy=3
        self.speedx =3
        mode = 1
        self.shoot_delay = 100
        self.last_shot = pygame.time.get_ticks()
        self.life=100
        self.fuel=100
    def update(self,up_walls,down_walls,left_walls,right_walls):
        global mode
        pygame.draw.rect(win,(255,255,255),(0,0,10,100),1)
        pygame.draw.rect(win,(255,0,0),(0,0,10,self.life))
        pygame.draw.rect(win,(255,255,255),(0,100,10,100),1)
        pygame.draw.rect(win,(0,0,255),(0,100,10,self.fuel))
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_KP_ENTER]:
            self.shoot()
        if keystate[pygame.K_UP] and self.fuel>0:
            if not pygame.sprite.spritecollide(self,up_walls,False):
                self.rect.y-=self.speedy
            self.fuel-=1
        elif not pygame.sprite.spritecollide(self,down_walls,False):
            self.speedy=self.speedy+(g*t)
            if self.speedy>=5:
                self.speedy=3
            self.rect.y+=self.speedy
            if self.fuel<100:
                self.fuel+=.1
        elif pygame.sprite.spritecollide(self,down_walls,False):
            if self.fuel<100:
                self.fuel+=.1
        if keystate[pygame.K_LEFT]:
            mode = 3
            if not pygame.sprite.spritecollide(self,left_walls,False):
                self.rect.x-=self.speedx
            self.image = scaled_player_image2
        if keystate[pygame.K_RIGHT]:
            mode = 1
            if not pygame.sprite.spritecollide(self,right_walls,False):
                self.rect.x+=self.speedx
            self.image = rotated_right_player_image1
        if self.rect.bottom>448:
            self.rect.bottom=448
        if pygame.sprite.spritecollide(self,bullets,True):
            self.life-=1
        if self.life==0:
            self.kill()
    def shoot(self):
        if mode == 1:
            bullet =Bullets(self.rect.right+10,self.rect.centery,mode)
        elif mode == 3:
            bullet =Bullets(self.rect.left-10,self.rect.centery,mode)
        
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot =now  
            all_sprites.add(bullet)
            bullets.add(bullet)
class Player02(pygame.sprite.Sprite):
    def __init__(self):
        global mode
        pygame.sprite.Sprite.__init__(self)
        self.image = rotated_right_player_image3
        self.rect=self.image.get_rect()
        self.rect.centerx=200
        self.rect.centery=20
        self.rect.bottom = 448
        self.speedy=3
        self.speedx =3
        mode = 1
        self.shoot_delay = 100
        self.last_shot = pygame.time.get_ticks()
        self.life=100
        self.fuel=100

    def update(self,up_walls,down_walls,left_walls,right_walls):
        global mode
        pygame.draw.rect(win,(255,255,255),(width-10,0,10,100),1)
        pygame.draw.rect(win,(255,0,0),(width-10,0,10,self.life))
        pygame.draw.rect(win,(255,255,255),(width-10,100,10,100),1)
        pygame.draw.rect(win,(0,0,255),(width-10,100,10,self.fuel))
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.shoot()
        if keystate[pygame.K_w] and self.fuel>0:
            if not pygame.sprite.spritecollide(self,up_walls,False):
                self.rect.y-=self.speedy
            self.fuel-=1
        elif not pygame.sprite.spritecollide(self,down_walls,False):
            self.speedy=self.speedy+(g*t)
            if self.speedy>=5:
                self.speedy=3
            self.rect.y+=self.speedy
            if self.fuel<100:
                self.fuel+=.1
        elif pygame.sprite.spritecollide(self,down_walls,False):
            if self.fuel<100:
                self.fuel+=.1
        if keystate[pygame.K_a]:
            mode = 3
            if not pygame.sprite.spritecollide(self,left_walls,False):
                self.rect.x-=self.speedx
            self.image = scaled_player_image4
        if keystate[pygame.K_d]:
            mode = 1
            if not pygame.sprite.spritecollide(self,right_walls,False):
                self.rect.x+=self.speedx
            self.image = rotated_right_player_image3

        if self.rect.bottom>448:
            self.rect.bottom=448
        if pygame.sprite.spritecollide(self,bullets,True):
            self.life-=1
        if self.life==0:
            self.kill()

    def shoot(self):
        if mode == 1:
            bullet =Bullets(self.rect.right+10,self.rect.centery,mode)
        elif mode == 3:
            bullet =Bullets(self.rect.left-10,self.rect.centery,mode)
        
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot =now  
            all_sprites.add(bullet)
            bullets.add(bullet)



class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y,mode):
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_bullet_image
        self.image.set_colorkey((0,0,0))
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.bottom =y
        self.rect.centerx=x
        self.rect.centery=y
        self.speedy= -5
        self.speedx = 5
        self.inmode = mode
        self.outmode =mode

    def update(self,upp_walls,leftt_walls,rightt_walls,downn_walls):
        if self.inmode == 1:
            self.rect.x+=self.speedx
        elif self.inmode == 3:
            self.rect.x-=self.speedx
        if self.inmode == 5:
            self.rect.x+=self.speedx
        elif self.inmode == 7:
            self.rect.x-=self.speedx
        if self.rect.bottom<0 or pygame.sprite.spritecollide(self,right_walls,False) or pygame.sprite.spritecollide(self,left_walls,False):
            self.kill()

def show_gamestart():
    draw_text(win,"GAME MINI_MILITIA",40,width/2,height/2) 
    draw_text(win,"UP,DOWN,LEFT,RIGHT  or W,S,A,D",10,width/2,height/2) 
    draw_text(win,"Press any key to Start the Game",15,width/2,height*3/8) 
    pygame.display.flip()
    waiting =True
    while waiting:
        clock.tick(fps) 
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==pygame.KEYUP:
                waiting =False


#----------------------------------functions------------------------------------#
def text(string,x,y,color=(50,40,243),size=30):
    font=pygame.font.SysFont('algerian',size)
    texts=font.render(string,True,color)
    win.blit(texts,(x,y))
#----------------------------------------------------------------------#

#----------------------------------main loop------------------------------------#

game_start =True
game_over =True
running = True
while running:
    if game_start:
        show_gamestart()
        game_start =False
        up_walls=pygame.sprite.Group()
        down_walls=pygame.sprite.Group()
        right_walls=pygame.sprite.Group()
        left_walls=pygame.sprite.Group()
        all_sprites=pygame.sprite.Group()
        walls=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        walls.add(up_walls)
        walls.add(down_walls)
        walls.add(left_walls)
        walls.add(right_walls)
        backg=Background()
        all_sprites.add(backg)
        player01=Player01()
        all_sprites.add(player01)
        player02=Player02()
        all_sprites.add(player02)
        for i in up_walls_coord:
            widthl=i[1][0]-i[0][0]
            heightl=1
            j=Line(i[0],i[1],widthl,heightl)
            up_walls.add(j)
            all_sprites.add(j)
        for i in down_walls_coord:
            widthl=i[1][0]-i[0][0]
            heightl=1
            j=Line(i[0],i[1],widthl,heightl)
            down_walls.add(j)
            all_sprites.add(j)
        for i in right_walls_coord:
            heightl=i[1][1]-i[0][1]
            widthl=1
            j=Line(i[0],i[1],widthl,heightl)
            right_walls.add(j)
            all_sprites.add(j)
        for i in left_walls_coord:
            heightl=i[1][1]-i[0][1]
            widthl=1
            j=Line(i[0],i[1],widthl,heightl)
            left_walls.add(j)
            all_sprites.add(j)
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    all_sprites.draw(win)

    #updates
    all_sprites.update(up_walls,down_walls,left_walls,right_walls)

    
    #draw/render
    pygame.display.flip()