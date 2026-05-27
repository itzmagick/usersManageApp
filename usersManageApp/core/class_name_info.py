import sqlite3
import os

class Information_name:
    def __init__(self, email, password):
        self.mail = email 
        self.password = password

    def recup(self):
        db_root_setting = os.path.join('data', 'data_base')
        conx = sqlite3.connect(db_root_setting)
        cursor = conx.cursor()

        try:
            query = 'SELECT name FROM users WHERE email = ? AND password = ?'
            cursor.execute(query, (self.mail, self.password))
            data_user_name = cursor.fetchone()
        except sqlite3.Error as e:
            print(f'Erreur lors de la recuperation du nom : {e}')
        finally:
            if conx:
                conx.close()

        return data_user_name