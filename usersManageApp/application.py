from core.index import Show_acceuil

valeurChoix = Show_acceuil()

match valeurChoix:
    case '1':
        from core.login import Recuperation_data       
    case '2':
        from core.sign import Sigin      
        choixValeur = Show_acceuil()
        


            
            


