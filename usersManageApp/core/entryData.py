def EntryData():
    emailEntry = input('Entrez votre mail: ')
    passwordEntry = input('Entrez votre password: ')

    return emailEntry, passwordEntry

def Fonctionnalite():
    print("Tu veux faire quoi parmis ces fonctionnalités")
    print("1. Ajouter un nom au compte")
    print("2. Voir tous les utilisateurs")
    print("3. Supprimer mon compte")

    chose = input('Donne le numéro de la fonctionnalité: ')
    print('\n')
    
    if chose and chose.isdigit():
        choix = chose
    else:
        print("Choisi le numero de la fonctionnalité")

    return choix

def Update_names():
    print('Ajouter un nom au profil')
    name = input('Entrez votre nom: ')

    return name

