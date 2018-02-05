   # -*- coding: utf-8 -*-

#File containing classes

class Character:
  #Class which define the character by its name and its position.  
   

    
    def __init__(self, name, position,bag):
        """we use the '__init__() method with many parameters, the class constructor"""
        self.name = name
        self.position = position
        self.bag = bag
        
    def __repr__(self):
        return("Je m'apelle {} et je suis à la position {}.".format( \
                self.name, self.position))

McGyver = Character('McGyver', [0,0],0)


class Labyrinthe:
    #class defined by its parameters
    #its size, its emptyness, its entrance, its exit, its chararacter.
   
    
    def __init__(self,size,wall,begin,end,minobject):
        
        self.size = size
        
        laby = []
        with open (wall, "r") as f:
            y = 0
            for line in f:
                laby.append([])
                for character in line:
                    laby[y].append(character)
                laby[y]=laby[y][0:len(laby[y])-1]
                y=y+1
            
                
        self.wall = laby
        
        self.character = Character('defautNom',[0,0],0)
        
        self.begin = begin
        
        self.end = end
        
        self.minobject = minobject
        
        L =[] # list of empty cells
        
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
        """Méthode appelée quand on souhaite initialiser le character"""
        bag= 0
        self.character = Character(name,self.begin,bag)
        
    def __repr__(self):
        
        a=''
        for k in range(len(self.wall)-1):
            a=a+''.join(self.wall[k])+'\n'
        
        a=a+''.join(self.wall[len(self.wall)-1])
        return(a)
    
    def available_position(self,position):
        
        x=position[0] #première élément de la liste
        y=position[1] # deuxième élément
        
        if x<0:
            return False
        else:
            if x>=self.size:
                return False
            else:
                if y<0:
                    return False
                else:
                    if y>=self.size:
                        return False
                    else:
                        if self.wall[x][y]=='1':
                            return False
                        else:
                            return True
        
