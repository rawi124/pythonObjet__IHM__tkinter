import fonction as fct

class Cube:
    """
    Une classe Cube pour créer et afficher le cube un cube
    """
    toile = None
    def __init__(self,x,y,z):
    	self.x = x 
    	self.y = y
    	self.z = z
    	self.left = fct.colors
    	self.right = fct.colors
    	self.top = fct.colors
    	
    def faceGauche(self, G):
        gx = (self.x - self.y)*G.d              + G.origin[0]
        gy = (self.x + self.y - 2*self.z)*G.d/2 + G.origin[1]
        G.C.create_polygon(gx,     gy+G.d,
                           gx-G.d, gy+(G.d/2),
                           gx-G.d, gy-(G.d/2),
                           gx,     gy,
                           gx,     gy+G.d, outline="#000", fill=self.left, tags=("leftc", "leftc"+str(id(self))))

    def faceDroite(self, G):
        gx = (self.x - self.y)*G.d              + G.origin[0]
        gy = (self.x + self.y - 2*self.z)*G.d/2 + G.origin[1]
        G.C.create_polygon(gx,     gy+G.d,
                           gx+G.d, gy+(G.d/2),
                           gx+G.d, gy-(G.d/2),
                           gx,     gy,
                           gx,     gy+G.d, outline="#000", fill=self.right, tags=("rightc", "rightc"+str(id(self))))

    def faceDevant(self, G):
        gx = (self.x - self.y)*G.d              + G.origin[0]
        gy = (self.x + self.y - 2*self.z)*G.d/2 + G.origin[1]
        G.C.create_polygon(gx,     gy-G.d,
                           gx+G.d, gy-(G.d/2),
                           gx,     gy,
                           gx-G.d, gy-(G.d/2),
                           gx,     gy-G.d, outline="#000", fill=self.top, tags=("topc", "topc"+str(id(self))))

    def afficher(self, G):
        self.faceGauche(G)
        self.faceDroite(G)
        self.faceDevant(G)

    def init_binds(self, G, cont) :
        G.C.tag_bind("topc"+str(id(self)), "<1>", lambda event: cont.mkcube(G, event, self.z))
        G.C.tag_bind("topc"+str(id(self)), "<Button-3>", lambda event: cont.delcube(G, event, self.z))

        G.C.tag_bind("leftc"+str(id(self)), "<Button-3>", lambda event: cont.delcube(G, event, self.z))
        G.C.tag_bind("leftc"+str(id(self)), "<1>", lambda event: cont.mkcube(G, event, self.z))
        
        G.C.tag_bind("rightc"+str(id(self)), "<Button-3>", lambda event: cont.delcube(G, event, self.z))
        G.C.tag_bind("rightc"+str(id(self)), "<1>", lambda event: cont.mkcube(G, event, self.z))

    def clean(self, G):
        G.C.delete("topc"+str(id(self)))
        G.C.delete("leftc"+str(id(self)))
        G.C.delete("rightc"+str(id(self)))
    def initialisation(cls,canva):
    	Cube.toile = canva
    initialisation = classmethod(initialisation)

