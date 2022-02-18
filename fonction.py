import tkinter as tk
from tkinter import filedialog
import numpy as num
import tkinter.colorchooser as color


################################ESPACE DES FONCTIONS#########################################################################

colors = "#313c8c"	
def changerCouleur():
	global colors
	colors = (color.askcolor())[1]
def OuvrirFenetreCouleur():
	fenetre = tk.Toplevel()#creation d une toplevel
	fenetre.title('choix couleurs')
	fenetre.geometry('300x150')
	tk.Button(fenetre,text='Selectionner une Couleur',command=changerCouleur).pack(expand=True)
