import pygame as py
import obj
import os
from pygame.locals import *
from sys import exit

py.init()

class Bg(py.sprite.Sprite):
    def __init__(self, dir_img,  x_img, y_img, rotate=False):
        
        py.sprite.Sprite.__init__(self)

        self.rotate = rotate
        self.dir_img = dir_img
        self.x_img = x_img
        self.y_img = y_img
        
        self.image = py.image.load(self.dir_img).convert_alpha()
        self.image = py.transform.scale(self.image, (self.image.get_width()*1.70, self.image.get_height()*1.70))
        self.rect = self.image.get_rect()
        if self.rotate:
            self.image = py.transform.flip(self.image, False, True)
            self.rect.bottomleft = self.x_img, self.y_img
        else:
            self.rect.topleft = self.x_img, self.y_img


largura, altura = 500, 800
tela = py.display.set_mode((largura, altura))
defalt_dir = os.path.dirname(__file__)
img_dir = os.path.join(defalt_dir, "img")

ys = obj.pipeys()

ft = Bg(os.path.join(img_dir, "pipe.png"), 200, 550)
ft1 = Bg(os.path.join(img_dir, "pipe.png"), 200, 100, True)
teste = py.sprite.Group()
teste.add(ft)
teste.add(ft1)

print(ys)

while True:
    tela.fill((255, 255, 255))
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
    
    teste.draw(tela)
    teste.update()
    ft.y_img += 0.02
    
    py.display.flip()
    