import pygame as py
from pygame.locals import *
from sys import exit
from random import randint


class Bird(py.sprite.Sprite):
    def __init__(self, dir_img):
        py.sprite.Sprite.__init__(self)
        
        self.dir_img = dir_img
        
        self.bird_sheet = py.image.load(self.dir_img).convert_alpha()
        self.bird_sheet = py.transform.scale(self.bird_sheet, (2*self.bird_sheet.get_width(), 2*self.bird_sheet.get_height()))
        
        self.sprite_list = []
        for c in range(3):
            img = self.bird_sheet.subsurface((c*(86*2), 0), (2*86, 2*64))
            self.sprite_list.append(img)
        
        self.n_sprite = 0
        self.image = self.sprite_list[self.n_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 200)
        
        
    def update(self):
        self.n_sprite += 0.15
        if self.n_sprite >= 3:
            self.n_sprite = 0
        self.image = self.sprite_list[int(self.n_sprite)]
        

class Bg(py.sprite.Sprite):
    def __init__(self, dir_img,  x_img, y_img, speed = 1):
        py.sprite.Sprite.__init__(self)
        
        self.dir_img = dir_img
        self.image = py.transform.scale2x(py.image.load(self.dir_img).convert_alpha())
        self.x_img = x_img*self.image.get_width()
        self.y_img = 800 - y_img
        self.speed = speed
        
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x_img, self.y_img
    
    
    def update(self): 
        self.x_img -= self.speed
        self.rect.topleft = self.x_img, self.y_img
        if self.x_img <= -self.image.get_width():
             self.x_img = self.image.get_width()
             
             
class Pipe(py.sprite.Sprite):
    def __init__(self, dir_img,  x_img, y_img, speed, rotate=False): 
        
        py.sprite.Sprite.__init__(self)
        
        self.rotate = rotate
        self.dir_img = dir_img
        self.x_img = x_img
        self.y_img = y_img
        self.speed = speed
        
        self.image = py.image.load(self.dir_img).convert_alpha()
        self.image = py.transform.scale(self.image, (self.image.get_width()*1.70, self.image.get_height()*1.70))
        self.rect = self.image.get_rect()
        
        if self.rotate:
            self.image = py.transform.flip(self.image, False, True)
            self.rect.bottomleft = self.x_img, self.y_img
        else:
            self.rect.topleft = self.x_img, self.y_img
              
              
    def update(self): 
        self.x_img -= self.speed
        if self.rotate:
            self.rect.bottomleft = self.x_img, self.y_img
        else:
            self.rect.topleft = self.x_img, self.y_img
            
        if self.x_img <= -self.image.get_width():
            self.x_img = 585


def pipeys():
    y_a = randint(300, 550)
    y_b = y_a - 125
    ys = (y_a, y_b)
    
    return ys