# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Section import Section

class Wall:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]
            # Si on ne met pas de paramètre position, le constructeur l'initialise à 0 par défaut. 
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
            # Si on ne met pas de paramètre widht, cela renvoie une exception car ce paramètre est obligatoire.
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
            # Si on ne met pas de paramètre height, cela renvoie une exception car ce paramètre est obligatoire.
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0 
            # Si on ne met pas de paramètre orientation, le constructeur l'initialise à 0 par défaut.             
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2  
            # Si on ne met pas de paramètre thickness, le constructeur l'initialise à 0,2 par défaut.
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5] 
            # Si on ne met pas de paramètre color, le constructeur l'initialise à [0.5, 0.5, 0.5] par défaut.
            
        # Objects list
        self.objects = []
        #Création d'une liste d'objets

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color'],
                                      'position': self.parameters['position']})
        self.objects.append(self.parentSection) 
        #Création d'une section grâce aux paramètres vus au dessus, section est ajoutée à la liste d'objets.
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self                 

    # Finds the section where the object x can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None
    
    # Adds an object    
    def add(self, x):      
        # A compléter en remplaçant pass par votre code
        findsection = self.findSection(x)   
        self.objects.pop(findsection[0])
        self.objects.extend(findsection[1].createNewSections(x))
        return self    
                    
    # Draws the faces
    def draw(self):
        # A compléter en remplaçant pass par votre code
        gl.glPushMatrix()
        gl.glRotatef(self.parameters["orientation"],0,0,1)
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
        self.parentSection.drawEdges()
        for x in self.objects:
            x.draw()
        gl.glPopMatrix()
        