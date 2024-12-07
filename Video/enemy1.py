import pygame
from pygame import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self,health,animation_list,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.alive=True
        self.living=True
        self.speed=speed
        self.health=health
        self.last_attack=pygame.time.get_ticks()
        self.attack_calmdown=1000
        #means it will wait for 1000milli second means 1 second for each attack
        self.animation_list=animation_list
        self.frame_index=0
        self.action_time=0
        #0 means walking posture and action
        #1 means attaking time and animation
        #2 means death time of an enemy
        self.update_time=pygame.time.get_ticks()
        self.image=self.animation_list[self.action_time][self.frame_index]
        self.rect=pygame.Rect(0,0,20,40) 
        #(x,y,width,height)
        self.rect=self.image.get_rect() 
        self.rect.center=(x,y)




    def update(self,Surface,Aim, bullet_sprites):
        if self.alive:

            #checking collision between bullet and enemy
            if pygame.sprite.spritecollide(self, bullet_sprites,True):
                self.health-=30


            #we will check that if emeny reaches target or its aim position
            if self.rect.right>Aim.rect.left:
                self.update_action_time(1)
                #action will change from walk(0) to attack(1) the castle
                print("Alert - Enemy Reached The Target Position (Castle)")

            if self.action_time==0:
                self.rect.x+=self.speed
            # to move the enemy we will update the speed expression here


            if self.action_time==1:
                if pygame.time.get_ticks() - self.last_attack > self.attack_calmdown:
                    #checking if sufficient time is there b/w each attack
                    Aim.health-=100
                    print(Aim.health)
                    if Aim.health<0:
                        Aim.health=0
                    self.last_attack=pygame.time.get_ticks()
                    #means it resets the timer again



            #checking if the enemy has health zero
            #if health is zero we will introduce death animation
            if self.health<=0:
                Aim.money+=100
                Aim.score+=150
                self.update_action_time(2)
                self.alive=False
                print(Aim.money)



            if Aim.health<=0:
                print("Oh No Enemies Won")

        #this is for updating animations on to the screen
        self.update_animation()



        #this is for drawing images on the screen
        pygame.draw.rect(Surface,"WHITE",self.rect,1)
        Surface.blit(self.image,(self.rect.x-10,self.rect.y-15))






    def update_animation(self):
        ANIMATION_CALM=50
        self.image=self.animation_list[self.action_time][self.frame_index]
        #to check the instant times between the updates of each animation 
        if pygame.time.get_ticks() - self.update_time > ANIMATION_CALM :
            self.update_time=pygame.time.get_ticks()
            self.frame_index+=4
        #to reset animation
        if self.frame_index>=len(self.animation_list[self.action_time]):
            if self.action_time==2:
                pass
                self.frame_index=len(self.animation_list[self.action_time])-1
            else:
                self.frame_index=0


        #this above statements says
        #when even death action is done then animation should stop it should not continue death action
        #len(self.animation_list[self.action_time])-1 is the highest it cannot cross it
        
    def update_action_time(self,new_action_time):
        #if both new action and old action are not equal then change the animation settings
        if new_action_time!=self.action_time:
            self.action_time=new_action_time
            self.frame_index=0
            #means it starts from image 0.png
            self.update_date=pygame.time.get_ticks()
            #it means are gonna update the time