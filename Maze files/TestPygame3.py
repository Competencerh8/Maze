# -*- coding: utf-8 -*-


import random
import pygame
from pygame.locals import *
from labyrinthe3 import *

pygame.init()

# Any constants
size_cell = 50
width = 15 # nombre de cases
height = 15 #nombre de cases
height2 = size_cell * height
width2 = size_cell * width

# We instantiate the window display; we name it and add an icon
# on instancie la fenêtre d'affichage, on la nomme et on rajoute une icône
window = pygame.display.set_mode((height2,width2))
pygame.display.set_caption("Labyrinthe")
icone = pygame.image.load("icone2.jpg")
pygame.display.set_icon(icone)


# we instantiate the labyrinth and add a character
# On instancie le labyrinthe et on lui ajoute un personnage
laby = Labyrinthe(15,"labytest.txt",[0,0],[0,14],2)
laby._set_character('McGyver')


# We instantiate text that we display when the player find the exit
# On instancie du texte qu'on va afficher par la suite quand l'utilisateur aura trouvé la sortie
font=pygame.font.Font("cubic.ttf", 90)
font2=pygame.font.Font("cubic.ttf", 60)
text = font.render("You Win",1,(155,0,0))
text2 = font2.render( "Recommencer",1,(255,0,0))
text3 = font2.render( "(Enter)",1,(255,0,0))
text4 = font.render("Press enter",1,(0,0,0))

#game loop
lost = False
game_over = False
while not game_over :
    
    #Limitation de vitesse de la boucle
    #30 frames par secondes pour ne pas 
    #surcharger le processeur
    pygame.time.Clock().tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #essentiel pour que la fenêtre se ferme quand on clique sur la croix dans le coin
            game_over = True
        
        #we implement character's moves 
        #Ici on implémente les mouvements du caractère en fonction des instructions de l'utilisateur    
        if event.type == pygame.KEYDOWN:
            
            if((laby.character.position != laby.end or laby.character.bag < laby.minobject) and lost == False):
            
            
                if event.key == pygame.K_RIGHT:
                    b = laby.move('d')
                
                elif event.key == pygame.K_LEFT:
                    b= laby.move('g')
            
                elif event.key == pygame.K_UP:
                    b= laby.move('h')
              
                elif event.key == pygame.K_DOWN:
                    b= laby.move('b')
                
                
                
                x = laby.character.position[0]
                y = laby.character.position[1]
                if laby.wall[x][y] == 'g':
                    print("On recommence")
                    lost = True
                
            
            
            if event.key == pygame.K_RETURN:
                print("on recommence")
                lost = False
                laby = Labyrinthe(15,"labytest.txt",[0,0],[0,14],3)
                laby._set_character('McGyver')
                
                
    
    
    
    laby.affiche(window) 
    
    
    if(laby.character.position == laby.end and laby.character.bag == laby.minobject):
        window.blit(text, (160,250))
        
        
    x = laby.character.position[0]
    y = laby.character.position[1]
    
    
    if laby.wall[x][y] == 'g' :
        window.blit(text4, (100,250))
        
        
    
    pygame.display.flip() 
    
    
pygame.quit()
quit()