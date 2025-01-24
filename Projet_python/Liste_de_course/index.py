import tkinter as tk
from tkinter import messagebox

def menu():
    root = tk.Tk()
    root.title("Liste de course")
    root.geometry("1080x720")

    Titre = tk.Label(root,text="Bienvenue sur votre liste de course")
    Titre.pack()

    bouton_afficher = tk.Button(root,text="Afficher la liste ",command=lambda:afficher())
    bouton_ajouter_produit = tk.Button(root,text="Ajouter un produit",command=lambda:ajouter_produit())
    bouton_afficher.pack()
    bouton_ajouter_produit.pack()
    root.mainloop()
    
def afficher():
    with open("liste.txt","r") as fichier:
        liste = fichier.read()
    tk.messagebox.showinfo("Ma liste")

def ajouter_produit():
    root = tk.Tk()
    root.title("Ajout nouveau produit")
    root.geometry("200x200")
    
    
    nom = tk.Label(root,text="Nom")
    quantite = tk.Label(root,text="Quantité")

    nom_form = tk.Entry(root,bd=5)
    quantite_form = tk.Entry(root,bd=5)
    
    
    nom.place(x=0, y=15)
    quantite.place(x=0,y=45)
    
    envoyer = tk.Button(root,text="Enregistrer",command=lambda:envoi(nom_form.get(),quantite_form.get()))
    envoyer.place(x=70,y=100)
    nom_form.place(x=50,y=15)
    quantite_form.place(x=50,y=45)
    root.mainloop() 
    
def envoi(nom,quantite):
    text = f'{nom},{quantite};\n'
    with open("liste.txt","a") as ficher:
        ficher.write(text)
    tk.messagebox.showinfo("Réussie",message="Votre liste est enregistré") 
 
menu()