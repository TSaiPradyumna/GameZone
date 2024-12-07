self.ui_camera = NodePath(PandaCamera('ui_camera'))
        self.ui_lens = OrthographicLens()
        # moved set_film_size() to window module for correct aspect ratio after setting window size
        self.ui_lens.set_near_far(-1000, 1000)
        self.ui_camera.node().set_lens(self.ui_lens)
        self._ui_lens_node = LensNode('_ui_lens_node', self.ui_lens)

        self.ui_render = NodePath('ui_render')
        self.ui_render.set_depth_test(0)
        self.ui_render.set_depth_write(0)
        self.ui_camera.reparent_to(self.ui_render)
        self.ui_display_region.set_camera(self.ui_camera)
        scene.ui_camera = self.ui_camera

        self.ui = Entity(eternal=True, name='ui', parent=self.ui_camera, scale=(self.ui_size*.5, self.ui_size*.5))
        self.overlay = Entity(parent=self.ui, model='quad', scale_x=self.aspect_ratio, color=color.clear, eternal=True, z=-99)

        # these get created when setting a shader
        self.filter_manager = None
        self.filter_quad = None
        self.render_texture = None
        self.filter_quad = None
        self.depth_texture = None
Was this helpful?

0

github
pokepetter / ursina / ursina / text.py
View on Github
external
tag = tag[4:-1]
                hsb_values = tuple(float(e.strip()) for e in tag.split(','))
                self.current_color = color.color(*hsb_values)

            elif tag.startswith('rgb('):   # set color based on numbers
                tag = tag[4:-1]
                rgb_values = (float(e.strip()) for e in tag.split(','))
                self.current_color = color.rgba(*rgb_values)

            if tag.startswith('scale:'):
                scale = tag.split(':')[1]
                self.scale_override = float(scale)

            elif tag.startswith('image:'):
                texture_name = tag.split(':')[1]
                image = Entity(
                    parent=self.text_node_path,
                    name='inline_image',
                    model='quad',
                    texture=texture_name,
                    color=self.current_color,
                    scale=1,
                    # position=(x*self.size*self.scale_override, y*self.size*self.line_height),
                    origin=(.0, -.25),
                    add_to_scene_entities=False,
                    )
                if not image.texture:
                    destroy(image)
                else:
                    self.images.append(image)
                    # self.text_node.remove_node()
                    # self.text_node = image
Was this helpful?

0

github
pokepetter / ursina / ursina / window.py
View on Github
external
sys.modules[__name__] = Window()

if __name__ == '__main__':
    from ursina import *
    # application.development_mode = False
    app = Ursina()

    window.title = 'Title'
    window.borderless = False
    window.fullscreen = False
    window.fps_counter.enabled = False
    window.exit_button.visible = False
    # window.cog.enabled = False

    Entity(model='cube', color=color.green, collider='box', texture='shore')

    app.run()
Was this helpful?

0

github
pokepetter / ursina / ursina / internal_prefabs / text.py
View on Github
external
target_text = tn.node().getText()
            print(target_text)
            invoke(tn.setX, tn.getX()+999999, delay=(i+x)*speed)

            new_text = ''
            for j, char in enumerate(target_text):
                # print(char)
                new_text += char
                invoke(tn.node().setText, new_text, delay=(i+x+j)*speed)

            x += len(target_text)


if __name__ == '__main__':
    app = Ursina()
    origin = Entity()
    origin.model = 'quad'
    origin.scale *= .05

    descr = '''Title\nIncrease max health
with 25% and raise attack with\n100 for 2 turns.'''
    # descr = descr.strip().replace('\n', ' ')
    replacements = {
        'hp' : 'hp ',
        'max health ' : 'max health ',
        'attack ' : 'attack '
    }
    # descr = multireplace(descr, replacements)
    # descr = 'Title \nIncrease max health with 25%.'
    # descr = 'test text'.upper()
    # descr = 'o---{::::::::::::::::::::&gt;'
    # Text.size = .25
Was this helpful?

0

github
pokepetter / ursina / ursina / entity.py
View on Github
external
def rotation(self, value):
        if not isinstance(value, (Vec2, Vec3)):
            value = self._list_to_vec(value)
        if isinstance(value, Vec2):
            value = Vec3(*value, self.rotation_z)

        self.setHpr(Vec3(value[1], value[0], value[2]) * Entity.rotation_directions)
Was this helpful?

0

github
pokepetter / ursina / ursina / entity.py
View on Github
external
def has_ancestor(self, possible_ancestor):
        p = self
        if isinstance(possible_ancestor, Entity):
            # print('ENTITY')
            for i in range(100):
                if p.parent:
                    if p.parent == possible_ancestor:
                        return True

                    p = p.parent

        if isinstance(possible_ancestor, list) or isinstance(possible_ancestor, tuple):
            # print('LIST OR TUPLE')
            for e in possible_ancestor:
                for i in range(100):
                    if p.parent:
                        if p.parent == e:
                            return True
                            break
Was this helpful?

0

github
pokepetter / ursina / ursina / raycaster.py
View on Github
external
import sys

from ursina import *
from ursina.entity import Entity
from ursina import scene
# from ursina import render
from panda3d.core import CollisionTraverser, CollisionNode, CollisionHandlerQueue
from panda3d.core import CollisionRay, CollisionSegment, CollisionBox
from ursina.vec3 import Vec3
import math
from ursina.hit_info import HitInfo


class Raycaster(Entity):

    def __init__(self):
        super().__init__(
            name = 'raycaster',
            eternal = True
            )
        self._picker = CollisionTraverser()  # Make a traverser
        self._pq = CollisionHandlerQueue()  # Make a handler
        self._pickerNode = CollisionNode('raycaster')
        self._pickerNode.set_into_collide_mask(0)
        self._pickerNP = self.attach_new_node(self._pickerNode)
        self._picker.addCollider(self._pickerNP, self._pq)
        self._pickerNP.show()


    def distance(self, a, b):
Was this helpful?

0

github
pokepetter / ursina / ursina / raycaster.py
View on Github
external
def boxcast(self, origin, direction=(0,0,1), distance=math.inf, thickness=(1,1), traverse_target=scene, ignore=list(), debug=False):
        if isinstance(thickness, (int, float, complex)):
            thickness = (thickness, thickness)
        resolution = 3
        rays = list()
        debugs = list()

        for y in range(3):
            for x in range(3):
                pos = origin + Vec3(lerp(-(thickness[0]/2), thickness[0]/2, x/(3-1)), lerp(-(thickness[1]/2), thickness[1]/2, y/(3-1)), 0)
                ray = self.raycast(pos, direction, distance, traverse_target, ignore, False)
                rays.append(ray)

                if debug and ray.hit:
                    d = Entity(model='cube', origin_z=-.5, position=pos, scale=(.02, .02, distance), ignore=True)
                    d.look_at(pos + Vec3(direction))
                    debugs.append(d)
                    # print(pos, hit.point)
                    if ray.hit and ray.distance > 0:
                        d.scale_z = ray.distance
                        d.color = color.green

        from ursina import destroy
        # [destroy(e, 1/60) for e in debugs]

        rays.sort(key=lambda x : x.distance)
        closest = rays[0]

        return HitInfo(
            hit = sum([int(e.hit) for e in rays]) > 0,
            entity = closest.entity,
Was this helpful?

0

github
pokepetter / ursina / ursina / camera.py
View on Github
external
def set_shader_input(self, name, value):
        if self.filter_quad:
            self.filter_quad.setShaderInput(name, value)
        else:
            print('no filter quad')


sys.modules[__name__] = Camera()


if __name__ == '__main__':
    from ursina import *
    app = Ursina()
    # app.load_editor()
    scene.camera.orthographic = True
    e = Entity()
    e.model = 'quad'
    e.color = color.random_color()
    e.position = (-2, 0, 10)

    e = Entity()
    e.model = 'quad'
    e.color = color.random_color()
    e.position = (2, 0, 10)

    e = Entity()
    e.model = 'quad'
    e.color = color.random_color()
    e.position = (0, 0, 40)
    # from ursina import *
    # Button(text='test button')
    from ursina.shaders import camera_grayscale_shader
Was this helpful?

0

github
pokepetter / ursina / ursina / internal_prefabs / text.py
View on Github
external
sys.path.append("..")
from ursina import *
from panda3d.core import TransparencyAttrib

from os import path
from panda3d.core import Filename
from panda3d.core import TextNode
import textwrap

from ursina.entity import Entity

# note:
#  tag doesn't work well in the middle of text.
# only good for titles for now.

class Text(Entity):

    size = .25

    def __init__(self, text=None, **kwargs):
        super().__init__()
        self.name = 'text'
        self.size = Text.size

        self.setColorScaleOff()
        self.text_nodes = list()
        self.origin = (-.5, .5)
        # self.font = 'VeraMono.ttf'
        temp_text_node = TextNode('')
        self._font = temp_text_node.getFont()

        self.line_height = 1
Was this helpful?

0

