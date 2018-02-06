# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
import random

laby = []

# We load the labyrinth from a txt file

with open("labytest.txt", "r") as f:
    y = 0
    for line in f:
        laby.append([])
        for character in line:
            laby[y].append(character)
        laby[y] = laby[y][0:len(laby[y])-1]
        y = y+1


class Character:
    # Class which define the character by its name and its position.

    def __init__(self,name,position,bag):

    # we use the '__init__() method with many parameters, the class constructor

        self.name = name
        self.position = position
        self.bag = bag

    def __repr__(self):
        return("Je m'apelle {} et je suis à la position {}.".format(
                self.name, self.position))

McGyver = Character('McGyver', [0,0], 0)

class Labyrinthe:
    # class defined by its parameters
    # its size, its emptyness, its entrance, its exit, its chararacter.

    def __init__(self,size,wall,begin,end,minobject):

        self.size = size

        laby = []
        with open (wall,"r") as f:
            y = 0
            for line in f:
                laby.append([])
                for character in line:
                    laby[y].append(character)
                laby[y] = laby[y][0:len(laby[y])-1]
                y = y+1

        self.wall = laby

        self.character = Character('defautNom',[0,0],0)

        self.begin = begin

        self.end = end
        self.minobject = minobject

        L = []  # list of empty cells

        for i in range(size):
            for j in range(size):

                cell = laby[i][j]

                if cell == '0':

                    coordCell = [i,j]
                    L.append(coordCell)

        for k in range(self.minobject):

            [i,j] = random.choice(L)
            L.remove([i,j])
            self.wall[i][j] = 'o'


    def _set_character(self,name):
    #we call the method for initializing the character
    #Méthode appelée quand on souhaite initialiser le character"""

        bag = 0
        self.character = Character(name,self.begin,bag)

    def __repr__(self):

        a = ''
        for k in range(len(self.wall)-1):
            a = a+''.join(self.wall[k])+'\n'

        a = a +''.join(self.wall[len(self.wall)-1])
        return(a)

    def available_position(self,position):

        x = position[0]   #first element of the list
        y = position[1]   # second élément

        if x < 0:
            return False
        else:
            if x >=self.size:
                return False
            else:
                if y < 0:
                    return False
                else:
                    if y >=self.size:
                        return False
                    else:
                        if self.wall[x][y] == '1':
                            return False
                        else:
                            return True

    def play(self):

        while(self.character.position != self.end or self.character.bag<self.minobject):

            a = ''
            for k in range(len(self.wall)-1):
                u = ''.join(self.wall[k])+'\n'

                if k == self.character.position[0]:
                    u = ''
                    for i in range(len(self.wall[k])):
                        if i == self.character.position[1]:
                            u = u + 'X'
                        else:
                            u = u+self.wall[k][i]
                    u = u + '\n'
                
                a = a + u

            u = ''.join(self.wall[len(self.wall)-1])

            if len(self.wall)-1 == self.character.position[0]:
                    u = ''
                    for i in range(len(self.wall[len(self.wall)-1])):
 
                        if i == self.character.position[1]:
                            u = u + 'X'
                        else:
                            u = u + self.wall[len(self.wall)-1][i]
            a = a + u
            
            print(a)
            
            print("where do you want to go ? (t,r,b,l)")
            
            c = input()
            
            if c=='t':
                new_position = self.character.position + []
                new_position[0] -= 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print(" new position is :")
                else:
                    print("Impossible to go in this direction")

            elif c=='r':
                new_position = self.character.position + []
                new_position[1] += 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print(" new position is :")
                else:
                    print("Impossible to go in this direction")
                    
            elif c=='b':
                new_position = self.character.position + []
                new_position[0] += 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print(" new position is :")

                else:
                    print("Impossible to go in this direction")

            else :
                new_position = self.character.position + []
                new_position[1] -= 1
                if self.available_position(new_position)==True:
                    self.character.position = new_position
                    print(" new position is :")

                else:
                    print("Impossible to go in this direction")

    # On verifie si le personnage est sur une case qui contient un objet et on récupère ou non
    #we check if the character is on a square that contains an object. if yes, we collect it

            x=self.character.position[0]
            y=self.character.position[1]

            if self.wall[x][y] == 'o':
                self.character.bag +=1
                self.wall[x][y] = '0'


        print("you're out ! well done !")

    
    def affiche(self, window):
    # Cette fonction affiche le labyrinthe dans la fenetre donnée en argument, on reprend le code précédent de play
    # this function displays the labyrinth in the window
        
        wall2 = pygame.image.load("wall2.jpg").convert()
        exitt = pygame.image.load("exit2.jpg").convert()
        entrance = pygame.image.load("entrance2.jpg").convert()
        emptyness = pygame.image.load("empty.png").convert()
        perso = pygame.image.load("perso2.jpg").convert()
        obj = pygame.image.load("object.png").convert()
        guard = pygame.image.load("guard.png").convert()
        size_cell = 50
        
        n = len(self.wall)
        for i in range(n):
            for j in range(n):
                
    # we calculate the squares's position in pixels
    # on calcule la position en pixel (x,y) des différentes cases
                if self.wall[i][j] == 'b': 
                    x = j * size_cell
                    y = i * size_cell
                    window.blit(entrance,(x,y))
                    
                elif self.wall[i][j] == '1':
                    x = j * size_cell
                    y = i * size_cell
                    window.blit(wall2,(x,y))
                    
                elif self.wall[i][j] == '0':
                    x = j * size_cell
                    y = i * size_cell
                    window.blit(emptyness,(x,y))
                        
                elif self.wall[i][j] == 'g':
                    x = j * size_cell
                    y = i * size_cell
                    window.blit(guard,(x,y))
                    
                elif self.wall[i][j] == 'o':
                    x = j * size_cell
                    y = i * size_cell
                    window.blit(obj,(x,y))

        y = self.character.position[0] * size_cell
        x = self.character.position[1] * size_cell
        window.blit(perso,(x,y))
    
    # We implement the function which allow us to move the character in the direction we want
    # Ici on implémente la fonction qui permet de faire bouger le personnage en fonction de la direction donnée en argument
    def move(self, direction):
        

        if direction=='t':
            new_position = self.character.position + []
            new_position[0] -= 1
            if self.available_position(new_position) == True:
                self.character.position = new_position
            else:
                return(0)

        elif direction=='r':
            new_position = self.character.position + []
            new_position[1] += 1
            if self.available_position(new_position) == True:
                self.character.position = new_position
            else:
                return(0)
                
        elif direction=='b':
            new_position = self.character.position + []
            new_position[0] += 1
            if self.available_position(new_position) == True:
                self.character.position = new_position

            else:
                return(0)

        else :
            new_position = self.character.position + []
            new_position[1] -= 1
            if self.available_position(new_position) == True:
                self.character.position = new_position

            else:
                return(0)
                
# On verifie si le personnage est sur une case qui contient un objet et on le récupère ou non
# #we check if the character is on a square that contains an object. if yes, we collect it  
        x=self.character.position[0]
        y=self.character.position[1]

        if self.wall[x][y] == 'o':
            self.character.bag +=1
            self.wall[x][y] = '0'

laby = Labyrinthe(15,"labytest.txt", [0,0], [0,14], 3)
laby._set_character('McGyver')