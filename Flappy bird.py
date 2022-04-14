import pygame as py
import obj
import os
from random import randint
from pygame.locals import *
from sys import exit

py.init()

color = {'Blue': (0, 0, 255), 'Red': (255, 0, 0), 'Green': (0, 255, 0),
         'White': (255, 255, 255), 'Gray': (100, 100, 100)}
defalt_dir = os.path.dirname(__file__)
img_dir = os.path.join(defalt_dir, "img")
largura, altura = 500, 800
tela = py.display.set_mode((largura, altura))
py.display.set_caption('Flappy Bird')
fps = py.time.Clock()

bird_sheet = py.transform.scale2x(py.image.load(os.path.join(img_dir, 'bird.png')).convert_alpha())

all_sprites = py.sprite.Group()

for c in range(2):
    bg = obj.Bg(os.path.join(img_dir, 'bg.png'), c, 1000, 1)
    all_sprites.add(bg)

for c in range(3):
    ys = obj.pipeys()
    pipe = obj.Pipe(os.path.join(img_dir, 'pipe.png'), c, ys[0], 4)
    pipe1 = obj.Pipe(os.path.join(img_dir, 'pipe.png'), c, ys[1], 4, True)
    all_sprites.add(pipe)
    all_sprites.add(pipe1)

for c in range(2):
    piso = obj.Bg(os.path.join(img_dir, 'base.png'), c, 150, 4)
    all_sprites.add(piso)

while True:
    
    tela.fill(color['Gray'])
    fps.tick(60)
    
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            exit()


    all_sprites.draw(tela)
    all_sprites.update()
    if pipe.x_img <= -84:
        ys = obj.pipeys()
        pipe.y_img = ys[0]
        pipe1.y_img = ys[1]

    py.display.flip()