import os
import sqlite3
from core.class_name_info import Information_name

def Insert(email, password):
    db_root_setting = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db = os.path.join(db_root_setting, 'data', 'data_base')
    
    conx = sqlite3.connect(db)
    cursor = conx.cursor()

    try:
        query = "INSERT INTO users (email, password) VALUES(?, ?)"
        cursor.execute(query, (email, password))
        conx.commit()
        print('User ajouté')
        confirmation = True
    except sqlite3.Error as e:
        print(f'Erreur lors de l ajout: {e}')
    finally:
        if conx:
            conx.close()

    return confirmation

def Insert_Name(name, mail, password):
    db_root_setting = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db = os.path.join(db_root_setting, 'data', 'data_base')
    conx = sqlite3.connect(db)
    cursor = conx.cursor()

    try:
        query = 'UPDATE users SET name = ? WHERE email= ? AND password= ?'
        cursor.execute(query, (name, mail, password))
        conx.commit()
        runclass = Information_name(mail, password)
        name_new = runclass.recup()
        print(f'Nom de {name_new[0]} a ete ajouté au compte de {mail}')
        confirmation = True
    except sqlite3.Error as e:
        print(f"Erreur lors de la mise à jour : {e}")
    finally:
        if conx:
            conx.close()
    return confirmation

