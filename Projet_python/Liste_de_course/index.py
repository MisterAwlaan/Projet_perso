import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

#Fonction Menu
def menu():
    root = tk.Tk()
    root.title("Liste de course")
    root.geometry("400x400")
    root.config(background="#65157d")    
    
    Titre = tk.Label(root,text="Bienvenue sur votre liste de course",bg='#65157d',fg='white')
    Titre.pack()
    
    f = font.Font(size=15)
    g = font.Font(size=18)
    
    
    bouton_afficher = tk.Button(root,text="Afficher la liste ",bg='#e56161',command=lambda:afficher())
    bouton_ajouter_produit = tk.Button(root,text="Ajouter un produit",bg='#e56161',command=lambda:ajouter_produit())
    bouton_cocher = tk.Button(root,text="Suivi Liste",bg='#e56161',command=lambda:cocher())
    bouton_supprimer_produit = tk.Button(root,text="Supprimer un produit",bg="#e56161",command=lambda:formulaire_supprimer_produit())
    bouton_fermer = tk.Button(root,text="Fermer",bg='red',command=lambda:fermer(root))
    
    
    
    bouton_afficher['font'] = f
    bouton_ajouter_produit['font'] = f
    bouton_cocher['font'] = f
    bouton_fermer['font'] = f
    bouton_supprimer_produit['font'] = f
    Titre['font'] = g
    
    bouton_afficher.place(x=120,y=100)
    bouton_ajouter_produit.place(x=110,y=150)
    bouton_cocher.place(x=140,y=200)
    bouton_supprimer_produit.place(x=100,y=250)
    bouton_fermer.place(x=155,y=300)
    root.mainloop()

#Fonction qui permet d'afficher le fichier txt
def afficher():
    root = tk.Tk()
    root.title("Ma Liste")
    root.geometry("300x300")
    root.config(background="#65157d")
    with open("liste.txt","r") as fichier:
        liste = fichier.read()
    label = tk.Label(root,text=liste,bg="#65157d",fg="white")
    label.pack()
    root.mainloop()

#Fonction qui permet d'ajouter un produit au fichier txt
def ajouter_produit():
    root = tk.Tk()
    root.title("Ajout nouveau produit")
    root.geometry("200x200")
    root.config(background="#65157d")
    nom = tk.Label(root,text="Nom",bg="#65157d",fg="white")
    quantite = tk.Label(root,text="Quantité",bg="#65157d",fg="white")
    nom_form = tk.Entry(root,bd=5)
    quantite_form = tk.Entry(root,bd=5)
    nom.place(x=0, y=15)
    quantite.place(x=0,y=45)
    envoyer = tk.Button(root,text="Enregistrer",bg="#e56161",fg="white",command=lambda:envoi(nom_form.get(),quantite_form.get()))
    envoyer.place(x=70,y=100)
    nom_form.place(x=50,y=15)
    quantite_form.place(x=50,y=45)
    root.mainloop() 
    
#Fonction qui permet d'envoyer la commande
def envoi(nom,quantite):
    text = f'{nom},{quantite};\n'
    with open("liste.txt","a") as ficher:
        ficher.write(text)
    tk.messagebox.showinfo("Réussie",message="Votre liste est enregistré") 

#Fonction qui coche la liste de course
def cocher():
    root = tk.Tk()
    root.title("Suivie de la liste")
    with open("liste.txt","r")as fichier :
        liste = transformation_txt_en_liste(fichier)
    variable = []
    for i,option in enumerate(liste):
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(root,text=option,variable=var)
        checkbox.pack()
        variable.append(var)
    root.mainloop()

#Fonction qui permet de convertir un fichier txt en list
def transformation_txt_en_liste(fichier):
    liste = fichier.split("\n")
    return liste

#Fonction qui permet de fermer une page        
def fermer(root):
    root.destroy()
    
#Fonction qui supprime un produit qui est dans la liste
def supprimer_produit(nom_du_produit):
    with open("liste.txt","r") as fichier :
        txt = fichier.read()
    liste = transformation_txt_en_liste(txt)
    for i in liste : 
        if nom_du_produit in i :
            liste.remove(i)
    resultat = '\n'.join(liste)
    with open("liste.txt",'w')as fichier : 
        fichier.write(resultat)
        
def formulaire_supprimer_produit():
    root = tk.Tk()
    root.title("Supprimer Produit")
    root.geometry("400x400")
    root.config(background="#65157d")
    
    f = font.Font(size=15)
    
    nom_du_produit = tk.Label(root,text="Nom du produit",bg="#65157d",fg="white")
    form_nom = tk.Entry(root,bd=5)
    bouton_confirmer = tk.Button(root,text="Confirmer",bg="pink",command=lambda:supprimer_produit(form_nom.get()))
    bouton_fermer = tk.Button(root,text="Fermer",bg="red",command=lambda:fermer(root))
    
    nom_du_produit["font"] = f
    
    nom_du_produit.place(x=130,y=100)
    form_nom.place(x=130,y=150)
    bouton_confirmer.place(x=160,y=200)
    bouton_fermer.place(x=170,y=250)
    root.mainloop()
    

menu()