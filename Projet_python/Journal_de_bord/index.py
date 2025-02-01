import tkinter as tk
from tkinter import font

def menu():
    root = tk.Tk()
    root.title("Mon journal de bord")
    root.geometry("400x400")
    root.config(background="#7366df")
    f = font.Font(size=15)
    Titre = tk.Label(root,text="Bienvenue sur mon Journal de Bord",bg="#7366df",fg="white")
    Bouton_Ajouter_text = tk.Button(root,text="Ajouter un text",bg="#d94bff")
    Bouton_afficher_mon_journal_de_bord = tk.Button(root,text="Afficher mon journal de bord",bg="#d94bff")
    Bouton_fermer = tk.Button(root,text="Fermer",bg="red")
    Titre["font"] = f
    Bouton_Ajouter_text["font"] = f
    Bouton_afficher_mon_journal_de_bord["font"] = f
    Bouton_fermer["font"] = f
    Titre.pack()
    Bouton_Ajouter_text.place(x=120,y=100)
    Bouton_afficher_mon_journal_de_bord.place(x=70,y=170)
    Bouton_fermer.place(x=150,y=240)
    root.mainloop()

def ajouter_text(date,text):
    text = f"{date},{text}"
    with open("journal.txt","a") as fichier :
        fichier.write(text)
    
def formulaire_ajout_text():
    root = tk.Tk()
    root.title("Ajouter un texte")
    root.geometry("400x400")
    root.config(background="#7366df")
    
    F = font.Font(size=10)
    
    label_date = tk.Label(root,text="Date",bg="#7366df",fg="white")
    zone_date = tk.Entry(root,bd=1)
    label_texte = tk.Label(root,text="Votre Texte",bg="#7366df",fg="white")
    zone_de_texte = tk.Entry(root,bd=1)
    
    label_date['font'] = F
    label_texte['font'] = F

    zone_date.place(x=100,y=50)
    label_date.place(x=0,y=50)
    zone_de_texte.place(x=80,y=100,width=100,height=100)
    label_texte.place(x=0,y=100)    
    root.mainloop()
    





formulaire_ajout_text()