import cube 

class Container:
    """
    une classe container contient tous les cubes de la grille.
    permet un affichage ordonné
    """
    def __init__(self):
        self.__grid = dict()

    def addCube(self, color, x, y, z):
    	
        self.__grid.setdefault(z, dict())
        self.__grid[z].setdefault(x, dict())
        self.__grid[z][x][y] = cube.Cube(x, y, z)

    def removeCube(self, x, y, z):
        del self.__grid[z][x][y]

    def mkcube(self, G, event, z):
        obj = G.C.find_withtag("current")
        x, y = (G.C.coords(obj)[0] - G.origin[0], G.C.coords(obj)[1] - G.origin[1])
        if "topc" in G.C.gettags(obj) :
            z += 1
        a = int((2*y + x)/(2*G.d) + z)
        b = int((2*y - x)/(2*G.d) + z)
        if "leftc" in G.C.gettags(obj) :
            a -= 1
        elif "rightc" in G.C.gettags(obj) :
            b -= 1
        self.addCube("red" ,a, b, z)
        self.__grid[z][a][b].init_binds(G, self)
        self.render(G)
        

    def delcube(self, G, event, z):
        obj = G.C.find_withtag("current")
        if "topc" in G.C.gettags(obj) :
            mg = 1
        else :
            mg = -1
        x, y = (G.C.coords(obj)[0] - G.origin[0], G.C.coords(obj)[1] - G.origin[1])
        a = int((2*y + x)/(2*G.d) + z) + mg
        b = int((2*y - x)/(2*G.d) + z) + mg
        self.__grid[z][a][b].clean(G)
        self.removeCube(a, b, z)
        self.render(G)
#ici c est pour avoir affichage ordonée
    def render(self, G):
        for z in sorted(self.__grid.items()) :
            for x in sorted(z[1].items()) :
                for y in sorted(x[1].items()) :
                	y[1].afficher(G)
                    
    def clean(self, G):
        for z in sorted(self.__grid.items()) :
            for x in sorted(z[1].items()) :
                for y in sorted(x[1].items()) :
                    y[1].clean(G)
