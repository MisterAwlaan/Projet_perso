import tkinter as tk
from tkinter import font
from tkinter import scrolledtext
from tkinter import messagebox

def menu():
    root = tk.Tk()
    root.title("Mon journal de bord")
    root.geometry("400x400")
    root.config(background="#7366df")
    f = font.Font(size=15)
    Titre = tk.Label(root,text="Bienvenue sur mon Journal de Bord",bg="#7366df",fg="white")
    Bouton_Ajouter_text = tk.Button(root,text="Ajouter un text",bg="#d94bff",command=lambda:formulaire_ajout_text())
    Bouton_afficher_mon_journal_de_bord = tk.Button(root,text="Afficher mon journal de bord",bg="#d94bff",command=lambda:formulaire_pour_afficher())
    Bouton_fermer = tk.Button(root,text="Fermer",bg="red",command=lambda:fermer(root))
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
    text = f"{date},{text},;"
    with open("journal.txt","a",encoding="utf-8") as fichier :
        fichier.write(text)
    messagebox.showinfo("Succès","Votre texte est bien enregistré")
    
def formulaire_ajout_text():
    root = tk.Tk()
    root.title("Ajouter un texte")
    root.geometry("400x400")
    root.config(background="#7366df")
    F = font.Font(size=15)
    label_date = tk.Label(root,text="Date(jj/mm/aaaa)",bg="#7366df",fg="white")
    zone_date = tk.Entry(root,bd=1)
    label_texte = tk.Label(root,text="Votre Récit",bg="#7366df",fg="white")
    zone_texte = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
    bouton_enregistrer = tk.Button(root,text="Enregistrer",bg="#cd2bf8",fg="white",command=lambda:ajouter_text(zone_date.get(),zone_texte.get("1.0",tk.END)))
    bouton_fermer = tk.Button(root,text="Fermer",bg="red",fg="white",command=lambda:fermer(root))
    label_date['font'] = F
    label_texte['font'] = F
    zone_date.place(x=130,y=50)
    label_date.place(x=110,y=20)
    label_texte.place(x=130,y=80)
    zone_texte.place(x=30,y=130)
    bouton_enregistrer.place(x=150,y=310)
    bouton_fermer.place(x=160,y=345)
    root.mainloop()

def fermer(root):
    return root.destroy()

def str_en_liste(text):
    x = []
    liste = text.split(";")
    for i in liste : 
        x.append(i.split(",")) 
    return x
    
def afficher(date):
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Affichage")
    root.config(background="#7366df")    
    liste_secondaire = []
    with open("journal.txt","r") as fichier : 
        text = fichier.read()
        liste = str_en_liste(text)
    for i in liste : 
        if i[0] == date :
            liste_secondaire.append(i)
    for i in liste_secondaire : 
        x = ",".join(i)
    resultat = tk.Label(root,text=x,bg="white",fg="black")
    Fermer = tk.Button(root,text="Fermer",bg="red",fg="white",command=lambda:fermer(root))
    Fermer.pack()
    resultat.pack()
    root.mainloop()


def formulaire_pour_afficher():
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Formulaire pour envoyer la date")
    root.config(background="#7366df")
    date_label = tk.Label(root,text="Date(jj/mm/aaaa)",bg="#7366df")
    zone_de_texte = tk.Entry(root,bd=5)
    bouton_soumettre = tk.Button(root,text="Afficher",command=lambda:afficher(zone_de_texte.get()),bg="purple")
    date_label.place(x=140,y=80)
    zone_de_texte.place(x=120,y=100)
    bouton_soumettre.place(x=160,y=160)
    root.mainloop()

menu()