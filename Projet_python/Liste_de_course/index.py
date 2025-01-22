import tkinter as tk
from tkinter import *

def menu():
    root = tk.Tk()
    root.title("Liste de course")
    root.geometry("1080x720")

    Titre = tk.Label(root,text="Bienvenue sur votre liste de course")
    Titre.pack()

    bouton_afficher = tk.Button(root,text="Afficher la liste ",command=lambda:afficher())
    bouton_afficher.pack()

    root.mainloop()
    
    pass


def afficher():
    with open("liste.txt","r") as fichier:
        liste = fichier.read()
    


menu()