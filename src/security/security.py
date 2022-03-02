from src.security.hash import generate
from colorama import Fore, Style
from dotenv import load_dotenv

import os

# This is the API initialization security


load_dotenv()

class Debug():
    def Danger(self, message ):
        self.message = message

        print(Fore.RED + Style.BRIGHT + "[!]" + Fore.RESET , self.message , Style.NORMAL)

    def Info(self, message, mes):
        self.message = message
        self.mes = mes

        print(Fore.BLUE + Style.BRIGHT + "[+]" + Fore.RESET , self.message , self.mes , Style.NORMAL)
    
    def Error(self, err):
        self.error = err
        
        print(Fore.RED + Style.BRIGHT + "[!]" + Fore.RESET , self.error , Style.NORMAL)

debug = Debug()

# Dotenv

def securityKEY():

    SECRET_KEY = os.getenv("AUTHORIZATION")

    if SECRET_KEY == 'None' or None:

        try:
            debug.Danger('''You didn't generate a hash to protect your APIKEY, so we generated one for you!\n''')
            debug.Info('Here:', generate())
            debug.Info('You should put it there in .env','')

            exit()

        except Exception as err:
            debug.Error(err)
            exit()

    else:
        pass


    
    










