import os
import sqlite3
from core.entryData import EntryData, Fonctionnalite
from core.filter import Filter_data
from core.tache import AllTache

def Recuperation_data(email, password):
    db_root_setting = os.path.join('data', 'data_base')
    conx = sqlite3.connect(db_root_setting)
    cursor = conx.cursor()

    try:
        query = "SELECT email, password FROM users WHERE email = ? AND password = ?"
        cursor.execute(query,(email, password))
        datas_user = cursor.fetchone()
    except sqlite3.Error as e:
        print(f'Erreur lors de la récuperation: {e}')
    finally:
        if conx:
            conx.close()

    return datas_user

email, password = EntryData()
clean_mail, clean_password = Filter_data(email, password)
datas_user = Recuperation_data(clean_mail, clean_password)
emailRecuperer, passwordRecuperer = datas_user[0], datas_user[1]

def Verification(clean_mail, clean_password, emailRecuperer, passwordRecuperer):
    if clean_mail == emailRecuperer or clean_password == passwordRecuperer:
        status = True
    else:
        print('Mail ou mot de passe incorrect')
    return status

Status = Verification(clean_mail, clean_password, emailRecuperer, passwordRecuperer)

if Status:
    chose = Fonctionnalite()
    chose_clean = chose.strip().lower()
    AllTache(chose_clean)

