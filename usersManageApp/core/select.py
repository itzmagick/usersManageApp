import os
import sqlite3

def select_all():
    db_root_setting = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db = os.path.join(db_root_setting, 'data', 'data_base')
    conx = sqlite3.connect(db)
    cursor = conx.cursor()

    try:
        query = "SELECT name FROM users WHERE name != 'admin'"
        cursor.execute(query)
        data_users = cursor.fetchall()
    except sqlite3.Error as e:
        print(f'Erreur lors de la recuperation des donnees: {e}')
    finally:
        if conx:
            conx.close()

    return data_users