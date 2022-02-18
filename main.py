#!/usr/bin/python
import tkinter as tk
import sys, time, numpy
from tkinter import filedialog
import container as cont
import grid as grille
import cube as Cub
import fonction as fct


def actionQuitter():
	"""pour tout fermer
	"""
	if tk.messagebox.askyesno("Exit", "voulez vous vraiment quitter ?"):
		   root.destroy()

def actionSauver():
	"""pour sauver un fichier
	"""
	Fichier=filedialog.asksaveasfilename( title="selectionner un fichier", filetypes=[('CSV files','.ps')])
	v.set(Fichier)
	C.postscript(file=Fichier)
def actionAide():
	"""pour ouvrir de l aide
	"""
	Ftopl = tk.Toplevel()#creation d une toplevel
	txt   = tk.Text(Ftopl)
	txt.pack(side="top", expand=True, fill="both")
	fd=open("aide.txt", 'r')
	li=fd.readline()
	while li!='':
		txt.insert(tk.END, li)
		li=fd.readline()
	fd.close()
	txt.tag_add("pbold", 4.9, 4.33)


if __name__ == "__main__" :

###############################ZONE DE CREATION ############################################################################
	root  = tk.Tk()#creation du root

	ftopl = tk.Toplevel(width=2400, height=2400)#creation d une toplevel
	ftopl.title('Modelisation Isometrique')

	fram =  tk.Frame(ftopl,width="150m",height="100m",borderwidth=4)#creation d une frame
	C     = tk.Canvas(fram, width=1000, height=9000, bg="grey",highlightthickness=5,highlightbackground="black")
	cadre = tk.Frame(ftopl,width="120m",height="100m",borderwidth=4)#creation d une frame
	cadre.pack(fill="x")

	Cub.Cube.initialisation(C)
	v =     tk.StringVar()



#*********************************************************************************#
# AIDE
#********************************************************************************#
	aide  = tk.Menubutton(cadre, text="aide")#creation du menuboutton
	Aid   = tk.Menu(aide, tearoff=False)
	Aid.add_command(label="aide",command=actionAide)
	aide["menu"]=Aid # options accessibles via un dico
	aide.pack(side="right")

#*********************************************************************************#
# CREATION d un menu boutton qui s appelle fichier pour gerer les entrees sorties
#********************************************************************************#
	mFichier=tk.Menubutton(cadre, text="Fichier",bg="ivory")#creation du menuboutton
	# menu associe
	menu1=tk.Menu(mFichier, tearoff=False)
	m1cb = {}
	listeAction=[actionSauver,actionQuitter]
	menu1.add_command(label = "sauver",command=actionSauver)
	menu1.add_command(label = "quitter",command=actionQuitter)
	mFichier["menu"]=menu1 # options accessibles via un dico
	mFichier.pack(side="left")

#*********************************************************************************#
# CREATION d un menu boutton qui s appelle Cube pour modifier les cubes
#*********************************************************************************#
	mCube=tk.Menubutton(cadre, text="Cube",bg="ivory")#creation du menuboutton
	# menu associe
	menu2=tk.Menu(mCube, tearoff=False)
	mcube = {}
	menu2.add_command(label = "Couleur",command=fct.OuvrirFenetreCouleur)
	mCube["menu"]=menu2 # options accessibles via un dico
	mCube.pack()

#*********************************************************************************#
	gr = grille.Grid(C, 35, int(sys.argv[1]), int(sys.argv[1]))
	cont = cont.Container()
	gr.show(cont)

	fram.pack()
	C.pack(padx=20, pady=20)

	root.bind_all(actionQuitter)

	root.mainloop()
	exit(0)
