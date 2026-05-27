import os
import sqlite3

def Actual_name(email, password, name):
    db_root_setting = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db = os.path.join(db_root_setting, 'data', 'data_base')

    conx = sqlite3.connect(db)
    cursor = conx.cursor()

    try:
        query = 'SELECT name FROM users WHERE email= ? AND password = ? AND name = ?'
        cursor.execute(query, (email, password, name))
        name_user = cursor.fetchone()
    except sqlite3.Error as e:
        print(f'Erreur lors de la recuperation de l ancien nom: {e}')
    finally:
        if conx:
            conx.close()
    return name_user
