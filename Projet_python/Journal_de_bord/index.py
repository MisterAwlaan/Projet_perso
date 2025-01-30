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






menu()