import sqlite3

def data_base():
    conx = sqlite3.connect('data_base')
    cursor = conx.cursor()

    cursor.execute("""CREATE TABLE users (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT UNIQUE,
                   password TEXT,
                   name TEXT
                   )""")
    
    try:
        conx.execute(
            "INSERT INTO users (email, password, name) VALUES (?, ?, ?)", 
            ('admin@gmail.com', '123456', 'admin')
        )

        conx.commit()
    except sqlite3.IntegrityError:
        pass
    conx.close()

data_base()