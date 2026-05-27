from core.filter import Filter_data
from core.insert import Insert
from core.entryData import EntryData
from core.class_name_info import Information_name

def Sigin(email, password): 
    confirmation = Insert(email, password)
    if confirmation:
        runclass = Information_name(email, password)
        name_final = runclass.recup()
        if name_final[0]:
            print(f"Salut {name_final[0]}, bienvenue parmi nous")                    
        else: 
            print('Bienvenue parmi nous')            

email, password = EntryData()
clean_mail, clean_password = Filter_data(email, password)
Sigin(clean_mail, clean_password)

