import os
import sqlite3

def Update_name(newname, email, password):
    db_root_setting = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db = os.path.join(db_root_setting, 'data', 'data_base')

    conx = sqlite3.connect(db)
    cursor = conx.cursor()

    try:
        query = "UPDATE users SET name = ? WHERE email= ? AND password = ?"
        cursor.execute(query, (newname, email, password))
        conx.commit()
    except sqlite3.Error as e:
        print(f'Erreur lors de la mise a jour du nom: {e}')
    finally:
        if conx:
            conx.close()
    