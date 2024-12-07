
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import numpy as np
import random



app = Ursina()

window.title = 'GUI PAGE 1'
window.fps_counter.enabled = True
max_frames = 45

window.fps_counter.max = 155

wall = Entity(model='quad', scale=(2,3), x=-3,
              collider='box', color=color.white,texture='assets\block.png')
level = Entity(model='quad', color=color.white, scale=(3, 1), x=4, collider='box',texture='assets\brickshadow.png')
trap = Entity(model='quad', scale=(2,2, 2), x=-5, y=1, collider='box', texture=f'assets\dfgdfg.jpg',color=color.red)




app.run()