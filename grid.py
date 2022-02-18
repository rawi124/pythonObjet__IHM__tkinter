import tkinter as tk
from container import *


class Grid(tk.Frame):
    """
    classe grille pour l affichage de la grille
    """
    def __init__(self, C, d=20, l=3, h=3):
        self.d = d
        self.__l = l
        self.__h = h
        self.origin = (0, 0)
        self.C = C

    """
    Rend une case de grille à l'écran.
    C est le canvas sur lequel on affiche la case,
    ox et oy sont les coordonnées de la case.
           1
    4            2
           3
    Les coordonnées vont dans le sens de la lecture (+ vers la gauche et le bas)
    """
    def rendercase(self, ox, oy):
        self.C.create_polygon(ox,        oy,
                              ox+self.d, oy+(self.d/2),
                              ox,        oy+self.d,
                              ox-self.d, oy+(self.d/2),
                              ox,        oy, outline="#000", fill="#FFF", tags="case")
    
    """
    Rend une grille entière à l'écran.
    """
    def render(self, cont):
        self.C.delete("case")
        cont.clean(self)
        self.C.update()
        for i in range(self.__l):
            for j in range(self.__h) :
                L = self.origin[0]+(j*self.d)-(i*self.d)
                l = self.origin[1]+(j*self.d/2)+(i*self.d/2)
                self.rendercase(L, l)
        cont.render(self)

    def show(self, cont) :
        self.C.bind("<Configure>", lambda event: self.update(event, cont))
        self.C.bind("<Button-4>", lambda event: self.zoom(1, event, cont))
        self.C.bind("<Button-5>", lambda event: self.zoom(-1, event, cont))
        self.C.tag_bind("case", "<1>", lambda event: cont.mkcube(self, event, 0))
    
    def zoom(self, z, event, cont) :
        if z == 1 :
            self.d += 2
        elif self.d > 0 :
            self.d -= 2
        self.render(cont)
            

    def update(self, event, cont) :
        if event :
            self.C.update()
            self.origin = (event.width//2, event.height//3)
            self.render(cont)
