from ursina import *

app = Ursina()
window.fps_counter.enabled = False


class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='assets/ss1'):
        super().__init__(
            parent = scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color.color(0,0, random.uniform(0.9, 1.0)),
            scale = 1.0
        )


for x in range(3):
    for y in range(3):
        for z in range(3):
            voxel = Voxel(position=(x,y,z))
EditorCamera()
app.run()