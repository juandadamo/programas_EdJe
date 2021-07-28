#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Pygame template - skeleton for a new pygame project
import pygame
import random, matplotlib
import matplotlib.pyplot as plt
from PIL import ImageColor


# In[23]:


prop_cycle = plt.rcParams['axes.prop_cycle']
colores = prop_cycle.by_key()['color']


# In[24]:


WIDTH = 720  # width of our game window
HEIGHT = 480 # height of our game window
FPS = 30 # frames per second
# initialize pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego")
clock = pygame.time.Clock()
color_azul = ImageColor.getrgb(colores[0])
color_naranja = ImageColor.getrgb(colores[1])


# In[25]:


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(color_naranja)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        #self.rect.x = 50
        #self.rect.y = 50
    def update(self):
        self.rect.centerx += 1


# In[26]:


clock = pygame.time.Clock()
mis_sprites = pygame.sprite.Group()
screen.fill(color_azul)
jugador = Jugador()  
mis_sprites.add(jugador)

running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    
    # Draw / render

    mis_sprites.update()

    # Draw / render
    
    mis_sprites.draw(screen)

    pygame.display.flip()
    
pygame.quit()


# In[21]:


jugador.rect.centerx


# In[ ]:





# In[ ]:





# In[ ]:




