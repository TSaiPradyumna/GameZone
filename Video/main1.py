#importing statements

import pygame
import math
import enemy1 as enemy
from enemy1 import Enemy
import math
import random
from pygame import mixer

def func1():

    #initiations
    pygame.init()
    pygame.mixer.init()



    Width,Height=1346,708
    win=pygame.display.set_mode((Width,Height))
    pygame.display.set_caption("MY CASTLE DEFENDER")
    clock=pygame.time.Clock()
    FPS=60
        

    #importing images
    bg=pygame.image.load(r"E:\SAI PRADYUMNA\Castle Defender\bg\Background1.png")
    bg=pygame.transform.scale(bg,(1346,708))
    castle_img_100=pygame.image.load(r"E:\SAI PRADYUMNA\Castle Defender\img\Castle\castle_100%.png")
    castle_img_25=pygame.image.load(r"E:\SAI PRADYUMNA\Castle Defender\img\Castle\castle_50%.png")
    castle_img_50=pygame.image.load(r"E:\SAI PRADYUMNA\Castle Defender\img\Castle\castle_25%.png")
    bullet_image=pygame.image.load(r"E:\SAI PRADYUMNA\Castle Defender\Bullet\bullet.png")
    scaled_bullet_image=pygame.transform.scale(bullet_image,(25,25))




    #importing fonts
    font_30=pygame.font.SysFont("Futura",30)
    font_60=pygame.font.SysFont("Futura",60)



    #loading musics
    mixer.music.load(r"E:\SAI PRADYUMNA\Castle Defender\Background_Music\War Music _ battle background music (320 kbps).mp3")
    Bullet_Sound=pygame.mixer.Sound(r"E:\SAI PRADYUMNA\Castle Defender\Sounda\Bomb_Blast\Pistol - Firing Sound.mp3")
    #music controls
    mixer.music.set_volume(60)
    #play the music continuously in background
    mixer.music.play(-1)
    Bullet_Sound.set_volume(20)


    #enemy animation pre reqirements
    Enemy_animate=[]
    Enemy_Type=["Malfi","goblin","purple_goblin","red_goblin"]
    Enemy_Health=[100,105,120,125]
    Animation_Type=["walk","attack","death"]



    #adding enemies
    Maximum_Enemies=10
    Enemy_Instant_Timer=3000
    last_enemy=pygame.time.get_ticks()
    enemies_alive=0


    #Upgrading Game With Levels
    Level=1
    Level_Difficulty=0
    Aim_Difficulty=1500
    #this tells there is no need of more enemies for this level
    Diffiulty_Multilevel=1.1
    #we added this because to increase level difficulty by 10 percent


    #game settings
    game_over=False
    next_level=False




    #Enemy Animation
    for enemy in Enemy_Type:
        #to load all the pre required images over here 
        animation_list=[]
        for animation in Animation_Type:
            no_of_frames=20
            temporary_list=[]
            for i in range(no_of_frames):
                images=pygame.image.load(f'Castle Defender/img/enemies/{enemy}/{animation}/{i}.png')
                img_width=images.get_width()
                img_height=images.get_height()
                images=pygame.transform.scale(images,((img_width)*0.25,(img_height)*0.26))
                temporary_list.append(images)
            animation_list.append(temporary_list)
        Enemy_animate.append(animation_list)


    #drawing text  on screen
    def draw_text(text,font,text_col,x,y):
        img=font.render(text,True,text_col)
        win.blit(img,(x,y))



    class Castle(pygame.sprite.Sprite):
        def __init__(self,image100,image50,image25):
            pygame.sprite.Sprite.__init__(self)
            castle_img100=pygame.transform.scale(castle_img_100,(Width-780,Height-280))
            castle_img50=pygame.transform.scale(castle_img_50,(Width-780,Height-280))
            castle_img25=pygame.transform.scale(castle_img_25,(Width-780,Height-280))
            self.image100 = castle_img100
            self.image50=castle_img50
            self.image25=castle_img25
            self.image=castle_img100
            self.fired=False
            self.health=1500
            self.max_health=self.health
            self.rect=self.image100.get_rect()
            self.rect.x=780
            self.rect.y=360
            self.angle=10
            self.money=0
            self.score=0
        def shoot(self):
            self.pos=event.pos
            # pygame.mouse.get_pos()
            x_distance=(self.pos[0]-self.rect.midleft[0])
            y_distance=-(self.pos[1]-self.rect.midleft[1])
            self.angle=math.degrees(math.atan2(y_distance,x_distance))
            # print(self.angle)
            # print(pos)

        def draw(self):
            if self.health<=250:
                self.image=self.image25
            elif self.health<=500:
                self.image=self.image50
            elif self.health<=1000:
                self.image=self.image100



    class Bullet(pygame.sprite.Sprite):
        def __init__(self,image,angle):
            pygame.sprite.Sprite.__init__(self)
            self.image = scaled_bullet_image
            self.rect=self.image.get_rect()
            self.angle=30
            self.speed=80
            self.rect.x=880
            self.rect.y=650
            #calculating speed 
            self.dx=(math.cos(angle)*self.speed)
            #calculates the x axis speed of the bullets based on the angles by using projectile graph cosine function horizontal speed  
            self.dy=-(math.sin(angle)*self.speed)
            #calculates the y axis speed of the bullets based on the angles by using projectile graph sine function vertical speed  

        def update(self):
            if self.rect.right<0 or self.rect.left>Width or self.rect.bottom<0 or self.rect.top>Height:
                self.kill()
            self.rect.x+=self.dx
            self.rect.y+=self.dy


    bullet_sprites=pygame.sprite.Group()
    enemy_sprites=pygame.sprite.Group()
    print("len(bullet_sprites)",len(bullet_sprites))



    all_sprites=pygame.sprite.Group()
    castle=Castle(castle_img_100,castle_img_50,castle_img_25)
    all_sprites.add(castle)



    running=True
    while running:
        clock.tick()
        win.blit(bg, (0, 0))
        
        bullet_sprites.update()
        bullet_sprites.draw(win)
        enemy_sprites.update(win,castle,bullet_sprites)

        #creating enemies
        if Level_Difficulty<Aim_Difficulty:
            #for loading differnt types of enemies to the game 
            #we introduce random module and math module
            #all_enemies
            e=random.randint(0,len(Enemy_Type)-1)
            if pygame.time.get_ticks() - last_enemy > Enemy_Instant_Timer:
                #then create enemies
                enemy=Enemy(Enemy_Health[e],Enemy_animate[e],-100,608,1)
                #here i used -100 beacuse i want enemies to start beyond the screen and come forward
                enemy_sprites.add(enemy)
                #reseting the enemy timer
                last_enemy=pygame.time.get_ticks()
                #we will increase Level Hardness by giving more energy to enemies
                Level_Difficulty+=Enemy_Health[e]
                print("Level_Difficulty",Level_Difficulty)
                #it will create enemies as per our Aim Difficulty if it is more than 1500 thrn creation of enemies will get stopped



        #we will now make code for checking wether enemies have been spawned
        if Level_Difficulty>=Aim_Difficulty:
            #checking how many enemies are still alive
            enemies_alive=0
            for e in enemy_sprites:
                if e.alive == True:
                    enemies_alive+=1
                print("enemies_alive",enemies_alive)
            #if no ememies are alive we will say level completed
            if enemies_alive==0 and next_level==False:
                next_level=True
                level_reset_time=pygame.time.get_ticks()



        #An Upgrade to next level
        if next_level==True:
            draw_text("LEVEL COMPLETE",font_60,"BLACK",450,400 )
            if pygame.time.get_ticks() - level_reset_time > 3000:
            #after a delay or gap of 3 seconds then proceed to next level
                next_level=False
                Level +=1
                last_enemy=pygame.time.get_ticks()
                #time reseted again
                Aim_Difficulty*=Diffiulty_Multilevel
                Level_Difficulty=0
                #to remove all the enemy objects in the screen after being killed we use empty()
                enemy_sprites.empty()





        castle.draw()
        all_sprites.draw(win)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running =False
            elif event.type == pygame.MOUSEBUTTONUP:
                castle.shoot()
                bullet=Bullet(scaled_bullet_image,castle.angle)
                Bullet_Sound.play()
                bullet_sprites.add(bullet)
                pygame.draw.line(win,"WHITE",(880,650),castle.pos)
        all_sprites.update()
        pygame.display.flip()



                    #[0]means x coordinate [1] means y coordinate
                    #actually what happens is
                    #get_pressed will create a list consist of 3 values
                    #by using indexing [0] means left button on mouse
                    # [1] means mid on mouse
                    # [2] means right button on mouse 