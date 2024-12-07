import pygame
import random
import math
pygame.init()
clock=pygame.time.Clock()
fps=100
width=394
height=448
win=pygame.display.set_mode((width,height))
back=pygame.image.load(r'C:\Users\CS12\Documents\mm\minimilitia\junkyard.png')
pygame.display.set_caption("MINI MILITIA")
g=10
t=1/fps
# scaled_back=pygame.transform.scale(back,(width,height))



player_image = pygame.image.load(r"C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\right.jpg")
scaled_player_image=pygame.transform.scale(player_image,(30,30))
rotated_right_player_image1=pygame.transform.rotate(scaled_player_image,0)
image_rect1=scaled_player_image.get_rect()
r_image_rect1=rotated_right_player_image1.get_rect()

player_image2 = pygame.image.load(r"C:\Users\CS4\Desktop\sripad\vsc\pygame\mini militia\left.png")
scaled_player_image2=pygame.transform.scale(player_image2,(30,30))
image_rect2=scaled_player_image2.get_rect()




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
        self.image.fill((255,0,0))
        # self.image.set_colorkey((255,0,0))
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
        self.speedy=3
        self.speedx =3


    def update(self,up_walls,down_walls,left_walls,right_walls):
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            if not pygame.sprite.spritecollide(self,up_walls,False):
                self.rect.y-=self.speedy
        elif not pygame.sprite.spritecollide(self,down_walls,False):
            self.speedy=self.speedy+(g*t)
            if self.speedy>=5:
                self.speedy=3
            self.rect.y+=self.speedy
        if keystate[pygame.K_LEFT]:
            if not pygame.sprite.spritecollide(self,left_walls,False):
                self.rect.x-=self.speedx
            self.image = scaled_player_image2
        if keystate[pygame.K_RIGHT]:
            if not pygame.sprite.spritecollide(self,right_walls,False):
                self.rect.x+=self.speedx
            self.image = rotated_right_player_image1

        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>394:
            self.rect.right=394
        if self.rect.bottom>448:
            self.rect.bottom=448
        if self.rect.top<0:
            self.rect.top=0


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
backg=Background()
all_sprites.add(backg)
player01=Player01()
all_sprites.add(player01)
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
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    win.fill((0,0,0))
    key=pygame.key.get_pressed()
    all_sprites.draw(win)

    #updates
    all_sprites.update(up_walls,down_walls,left_walls,right_walls)


    #draw/render
    pygame.display.flip()