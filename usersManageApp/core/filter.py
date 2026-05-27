def Filter_data(email, password):
    if email == '' or password == '':
        print('Ramplissez tous les champs')
        exit()

    if not '@' and '.' in email:
        print('Mail invalide')
        exit()

    if len(password) < 6:
        print('Le mot de passe doit contenir au minimum 8 caracteres')
        exit()

    emailClean = email
    passwordClean = password.strip()

    return emailClean, passwordClean

def Filter_name(name):
    if name:
        for caractere in name:
            if caractere.isdigit():
                print('Le nom dois contenir que des lettres')
                break
        clean_name = name.lower()
    else:
        print('Entrez votre nom')
    return clean_name

