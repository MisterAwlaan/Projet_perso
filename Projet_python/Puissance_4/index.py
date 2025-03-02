# Grille pour le puissance 4 
a = [[0,0,0,0],
     [0,0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

def grille():
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])

def verif_verti():
    if a[0][0] == 1 and a[1][0] == 1 and a[2][0] == 1 and a[3][0] == 1 : 
        return True
    if a[0][0] == 2 and a[1][0] == 2 and a[2][0] == 2 and a[3][0] == 2 : 
        return True
    
    if a[0][1] == 1 and a[1][1] == 1 and a[2][1] == 1 and a[3][1] == 1 : 
        return True
    if a[0][1] == 2 and a[1][1] == 2 and a[2][1] == 2 and a[3][1] == 2 : 
        return True

    if a[0][2] == 1 and a[1][2] == 1 and a[2][2] == 1 and a[3][2] == 1 : 
        return True
    if a[0][2] == 2 and a[1][2] == 2 and a[2][2] == 2 and a[3][2] == 2 :
        return True

    if a[0][3] == 1 and a[1][3] == 1 and a[2][3] == 1 and a[3][3] == 1 :
        return True 
    if a[0][3] == 2 and a[1][3] == 2 and a[2][3] == 2 and a[3][3] == 2 :
        return True 

def verif_horizon():
    if a[0][0] == 1 and a[0][1] == 1 and a[0][2] == 1 and a[0][3] == 1  :
        return True
    if a[0][0] == 2 and a[0][1] == 2 and a[0][2] == 2 and a[0][3] == 2  :
        return True

    if a[1][0] == 1 and a[1][1] == 1 and a[1][2] == 1  and a[1][3]== 1:
        return True 
    if a[1][0] == 2 and a[1][1] == 2 and a[1][2] == 2  and a[1][3]== 2:
        return True

    if a[2][0] == 1 and a[2][1] == 1 and a[2][2] == 1 and a[2][3] == 1 :
        return True
    if a[2][0] == 2 and a[2][1] == 2 and a[2][2] == 2 and a[2][3] == 2 :
        return True

    if a[3][0] == 1 and a[3][1] == 1 and a[3][2] == 1 and a[3][3] == 1 :
        return True
    if a[3][0] == 2 and a[3][1] == 2 and a[3][2] == 2 and a[3][3] == 2 :
        return True

def verif_diagonal():
    if a[0][0] == 1 and a[1][1] == 1 and a[2][2] == 1 and a[3][3] == 1 : 
        return True
    if a[0][0] == 2 and a[1][1] == 2 and a[2][2] == 2 and a[3][3] == 2 : 
        return True
    
    if a[0][3] == 1 and a[1][2] == 1 and a[2][1] == 1 and a[3][0] == 1 : 
        return True
    if a[0][3] == 2 and a[1][2] == 2 and a[2][1] == 2 and a[3][0] == 2 : 
        return True

def action(j):
    pass
