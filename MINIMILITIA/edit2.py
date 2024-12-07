import pygame
import random
pygame.init()
clock=pygame.time.Clock()
fps=100
width=394
height=448
win=pygame.display.set_mode((width,height))
back=pygame.image.load(r'C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\junkyard.png')
# scaled_back=pygame.transform.scale(back,(width,height))
# v=1.2
g=9.8


player_image = pygame.image.load(r"C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\right.jpg")
scaled_player_image=pygame.transform.scale(player_image,(30,30))
rotated_right_player_image1=pygame.transform.rotate(scaled_player_image,0)
image_rect1=scaled_player_image.get_rect()
r_image_rect1=rotated_right_player_image1.get_rect()

player_image2 = pygame.image.load(r"C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\left.png")
scaled_player_image2=pygame.transform.scale(player_image2,(30,30))
image_rect2=scaled_player_image2.get_rect()



bullet_image = pygame.image.load(r"C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\bullet5.bmp")
scaled_bullet_image=pygame.transform.scale(bullet_image,(20,20))
# rotated_bullet_image=pygame.transform.rotate(bullet_image,90)
image_rect2=scaled_bullet_image.get_rect()


player_image3 = pygame.image.load(r"C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\villan.jpg")
scaled_player_image3=pygame.transform.scale(player_image3,(30,30))
rotated_right_player_image3=pygame.transform.rotate(scaled_player_image3,0)
image_rect3=scaled_player_image3.get_rect()
r_image_rect3=rotated_right_player_image3.get_rect()

player_image4 = pygame.image.load(r"C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\vil_left.png")
scaled_player_image4=pygame.transform.scale(player_image4,(30,30))
image_rect4=scaled_player_image4.get_rect()



up_walls_coord=[[(96,103),(240,103)],
[(96,150),(200,150)],
[(200,175),(240,175)],
[(301,150),(350,150)],
[(122,305),(148,305)],
[(148,328),(192,315)],
[(192,305),(318,305)],
[(40,48),(350,48)]]
down_walls_coord=[[(96,103),(240,103)],
[(301,105),(350,105)],
[(122,258),(200,256)],
[(200,235),(240,235)],
[(241,256),(301,258)],
[(40,416),(350,416)]]
left_walls_coord=[[(240,103),(240,175)],
[(40,48),(40,416)],
[(301,258),(318,305)],
[(192,305),(192,315)],
[(240,235),(241,256)]]

right_walls_coord=[[(96,103),(96,150)],
[(301,105),(301,150)],
[(200,150),(200,175)],
[(200,235),(200,256)],
[(122,258),(122,305)],
[(148,305),(148,328)],
[(350,48),(350,416)]]


#----------------------------------classes------------------------------------# 
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=back
        self.rect=self.image.get_rect()


class Line(pygame.sprite.Sprite):
    def __init__(self,x,y,widthl,heightl):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((widthl,heightl))
        self.image.set_colorkey((0,0,0))

        self.rect=self.image.get_rect()
        self.rect.x=x[0]
        self.rect.y=x[1]


class Player01(pygame.sprite.Sprite):
    def __init__(self):
        global mode
        pygame.sprite.Sprite.__init__(self)
        self.image = rotated_right_player_image1
        self.image.set_colorkey("BLACK")
        self.rect=self.image.get_rect()
        self.rect.centerx=10
        self.rect.centery=448
        self.rect.bottom = 448
        self.speedy=0
        self.speedx =0
        # self.top=[(i,self.rect.left)for i in range(self.rect.left,self.rect.right)]
        self.up=True
        self.shoot_delay = 2
        self.last_shot = pygame.time.get_ticks()
        mode = 1


    def update(self,up_walls,left_walls,right_walls,down_walls):
        global mode
        self.speedy=self.speedy+(g*t)        
        self.rect.y+=self.speedy
        # self.top=[(i,self.rect.left)for i in range(self.rect.left,self.rect.right)]
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_KP_ENTER]:
            self.shoot()
        if keystate[pygame.K_LEFT]:
            mode = 3
            if not pygame.sprite.spritecollide(self,left_walls,False):
                self.speedx=-2
            self.image = scaled_player_image2
        if keystate[pygame.K_RIGHT]:
            mode = 1
            if not pygame.sprite.spritecollide(self,right_walls,False):
                self.speedx=2
            self.image = rotated_right_player_image1
        if keystate[pygame.K_UP]:
            # mode = 4
            if not pygame.sprite.spritecollide(self,up_walls,False):
                self.speedy=-2
            # self.image =rotated_up_player_image1
        if keystate[pygame.K_DOWN]:
            # mode = 2
            if not pygame.sprite.spritecollide(self,down_walls,False):
                self.speedy=2
            # self.image = rotated_down_player_image1
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>394:
            self.rect.right=394
        if self.rect.bottom>448:
            self.rect.bottom=448
            self.speedy=0
        if self.rect.top<0:
            self.rect.top=0

    def shoot(self):
        if mode == 1:
            bullet =Bullets(self.rect.right,self.rect.centery)
        # elif mode == 2:
        #     bullet =Bullets(self.rect.centerx,self.rect.bottom)
        elif mode == 3:
            bullet =Bullets(self.rect.left,self.rect.centery)
        # elif mode == 4:
        #     bullet =Bullets(self.rect.centerx,self.rect.top)        
        bullet =Bullets(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot =now  
        
class Player02(pygame.sprite.Sprite):
    def __init__(self):
        global mode
        pygame.sprite.Sprite.__init__(self)
        self.image = rotated_right_player_image3
        self.image.set_colorkey("BLACK")
        self.rect=self.image.get_rect()
        self.rect.centerx=300
        self.rect.centery=200
        self.rect.bottom = 448
        self.speedy=0
        self.speedx =0
        # self.top=[(i,self.rect.left)for i in range(self.rect.left,self.rect.right)]
        self.up=True
        self.shoot_delay = 2
        self.last_shot = pygame.time.get_ticks()
        mode = 1


    def update(self,up_walls,left_walls,right_walls,down_walls):
        global mode
        self.speedy=self.speedy+(g*t)        
        self.rect.y+=self.speedy
        # self.top=[(i,self.rect.left)for i in range(self.rect.left,self.rect.right)]
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.shoot()
        if keystate[pygame.K_a]:
            mode = 7
            if not pygame.sprite.spritecollide(self,left_walls,False):
                self.speedx=-1
            self.image = scaled_player_image4
        if keystate[pygame.K_d]:
            mode = 5
            if not pygame.sprite.spritecollide(self,right_walls,False):
                self.speedx=2
            self.image = rotated_right_player_image3
        if keystate[pygame.K_w]:
            # mode = 8
            if not pygame.sprite.spritecollide(self,up_walls,False):
                self.speedy=-1
        if keystate[pygame.K_s]:
            # mode = 6
            if not pygame.sprite.spritecollide(self,down_walls,False):
                self.speedy=2
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>394:
            self.rect.right=394
        if self.rect.bottom>448:
            self.rect.bottom=448
            self.speedy=0
        if self.rect.top<0:
            self.rect.top=0
        
    def shoot(self):
        if mode == 5:
            bullet =Bullets(self.rect.right,self.rect.centery)
        # elif mode == 6:
        #     bullet =Bullets(self.rect.centerx,self.rect.bottom)
        elif mode == 7:
            bullet =Bullets(self.rect.left,self.rect.centery)
        # elif mode == 8:
        #     bullet =Bullets(self.rect.centerx,self.rect.top)        
        bullet =Bullets(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot =now  
        
class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y):
        global mode
        pygame.sprite.Sprite.__init__(self)
        self.image = scaled_bullet_image
        self.image.set_colorkey((255,255,255))
        # self.image = pygame.Surface((10,15))
        # self.image.fill("YELLOW")
        self.rect=self.image.get_rect()
        self.rect.bottom =y
        self.rect.centerx=x
        self.rect.centery=y
        self.speedy= -5
        self.speedx = 5
        self.inmode = mode
        self.outmode =mode

    def update(self,up_walls,left_walls,right_walls,down_walls):
        global mode
        if self.inmode == 1:
            self.rect.x+=self.speedx
        # elif self.inmode == 2:
        #     self.rect.y-=self.speedy
        elif self.inmode == 3:
            self.rect.x-=self.speedx
        # elif self.inmode == 4:
        #     self.rect.y+=self.speedy
        if self.inmode == 5:
            self.rect.x+=self.speedx
        # elif self.inmode == 6:
        #     self.rect.y-=self.speedy
        elif self.inmode == 7:
            self.rect.x-=self.speedx
        # elif self.inmode == 8:
        #     self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()





#----------------------------------functions------------------------------------#


def text(string,x,y,color=(50,40,243),size=30):
    font=pygame.font.SysFont('algerian',size)
    texts=font.render(string,True,color)
    win.blit(texts,(x,y))

#----------------------------------------------------------------------#


up_walls=pygame.sprite.Group()
down_walls=pygame.sprite.Group()
right_walls=pygame.sprite.Group()
left_walls=pygame.sprite.Group()
all_sprites=pygame.sprite.Group()
bullets=pygame.sprite.Group()
backg=Background()
all_sprites.add(backg)
player01=Player01()
player02=Player02()
all_sprites.add(player01)
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



#----------------------------------main loop------------------------------------#



while True:
    clock.tick(fps)
    t=1/fps
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    key=pygame.key.get_pressed()
    all_sprites.draw(win)




    #updates
    all_sprites.update(up_walls,left_walls,right_walls,down_walls)




    #draw/render
    pygame.display.flip()