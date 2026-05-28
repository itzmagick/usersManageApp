import os
import sqlite3
from core.filter import Filter_data, Filter_name
from core.insert import Insert_Name
from core.select import select_all
from core.entryData import Update_names

def AllTache(choix):
    if choix != "" and choix.isdigit():
        valeur = choix.strip()
        match valeur :
            case '1':
                print('Pour ajouter le nom')
                mail = input('Votre Mail: ')
                password = input('Votre mot de passe:')
                name = Update_names()
                name_clean = Filter_name(name)
                Insert_Name(name_clean, mail, password)               
            case '2':
                def Filter(email, password):
                    if not '@' and '.' in email:
                        print('Mail invalide')
                        exit()
                    
                    if len(password) < 6:
                        print('Le mail dois avoir au minimum 6 caractere')
                        exit()
                    return (email, password)
                
                def verification_role(mail, password):
                    db_root_setting = os.path.join('data', 'data_base')
                    conx = sqlite3.connect(db_root_setting)
                    cursor = conx.cursor()

                    try:
                        query = "SELECT name FROM users WHERE email = ? AND password = ?"
                        cursor.execute(query, (mail, password))
                        data_name = cursor.fetchone()
                    except sqlite3.Error as e:
                        print(f'Erreur lors de la recuperation: {e}')
                    finally:
                        if conx:
                            conx.close()
                    return data_name
                            
                print('Ces informations sont reservées aux personnes specifiques')
                print('Si vous en faite parti, entrez vos identifiants')
                print('\n')

                mailEntryViewUsers = input('Votre mail: ')
                passwordEntryViewUsers = input('Votrez mot de passe: ')

                mail_clean, password_clean = Filter(mailEntryViewUsers, passwordEntryViewUsers)
                data = verification_role(mail_clean, password_clean)

                if data:
                    if data[0] == 'admin':
                        users = select_all()
                        for i in range((len(users))-1):
                            user = users[i]
                            nom = user[0]
                            print(f'{i+1}. {nom}')
                    else:
                        print("Desolé, vous n'avez pas le doit d'acceder à ces informations")
                else:
                    print('\n')
                    print("Mail ou mot de passe incorrect")
                    print('\n')   
                            
            case '3':
                print('Etes-vous sûr de vouloir supprimer votre compte ?')
                choixx = input('Tapez ( OUI ) si oui et ( NON ) si non : ')

                if choixx:
                    clean_choix = choixx.lower().strip()
                    if clean_choix == 'oui':               
                        def Delete(email, password):
                            db_root_setting = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                            db = os.path.join(db_root_setting, 'data', 'data_base')
                            conx = sqlite3.connect(db)
                            cursor = conx.cursor()

                            try:
                                query = 'DELETE FROM users WHERE email= ? AND password= ?'
                                cursor.execute(query, (email, password))
                                conx.commit()
                            except sqlite3.Error as e:
                                print(f'Erreur lors de la suppression: {e}')
                            finally:
                                if conx:
                                    conx.close()
                            return True
                            
                        mailEntryVerificationForDeleteAccount = input('Entrez votre mail: ')
                        passwordEntryVerificationForDeleteAccount = input('Entrez votre mot de passe: ')
                        email_clean, password_cln = Filter_data(mailEntryVerificationForDeleteAccount, passwordEntryVerificationForDeleteAccount)
                        status = Delete(email_clean, password_cln)
                        if status:
                            print("L'utilisateur a été supprimer avec succès")
                            
                    else:
                        print(f'Merci de rester parmi nous')
                        exit()
    else:
        print('Donnez le numéro de la fonctionnalité (ex: 1, etc...)')
    return True
