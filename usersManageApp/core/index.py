def Show_acceuil():
    print('Bienvenue sur usersManageApp')
    print('1. Se connecter')
    print("2. S'inscrire")

    choix = input("Choisi l'action: ")
    if choix and choix.isdigit():
        valeur = choix.strip()
    return valeur


