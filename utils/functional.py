import sqlalchemy
import stdiomask

from sqlalchemy import text

import pandas as pd

from .roles import roles

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getEngine(user, pw):
    eng_str = f"mysql+mysqlconnector://{user}:{pw}@localhost:3306/fabecare_db"
    engine = sqlalchemy.create_engine(eng_str)

    return engine

def getUserInfo():
    check = 0

    while not check:
        pw = stdiomask.getpass("[INFO] Insert password >>> ", '*')
        if pw == 'ciao':
            check = 1
        else:
            print(Bcolors.FAIL + "\n[ERROR] Please check username and/or password..\n" + Bcolors.ENDC)

    return pw

def getRole(user):
    global roles

    for key in roles:
        if user in roles[key]:
            return key


def getAnagrafica(engine, ruolo):

    choice = ''

    print(Bcolors.OKCYAN + """
            [1] Anagrafica completa dei pazienti
            [2] Ricerca paziente
            """ + Bcolors.ENDC)

    while choice != '1' and choice != '2':

        if ruolo == 2:

            while True:

                choice = input("\n[INFO] Seleziona opzione >>> ")

                if choice == '1':
                    query = text("SELECT IDP, NOME, COGNOME, DATA_NASCITA FROM pazienti")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                elif choice == '2':
                    patient_id = input("\n[INFO] Input patient UID >>> ")
                    try:
                        query = text(f"SELECT IDP, NOME, COGNOME, DATA_NASCITA FROM pazienti WHERE IDP = '{patient_id}'")
                        with engine.connect() as conn:
                            res = pd.read_sql_query(query, conn)
                            return res
                    except Exception as e:
                        print(Bcolors.FAIL +  f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
                else:
                    print(Bcolors.FAIL + f"\n[ERROR] Invalid input...\n" + Bcolors.ENDC)

        else:
            choice = input("\n[INFO] Seleziona opzione >>> ")

            if choice == '1':
                query = text("SELECT * FROM pazienti")
                with engine.connect() as conn:
                    res = pd.read_sql_query(query, conn)
                    return res
            elif choice == '2':
                patient_id = input("\n[INFO] Input patient UID >>> ")
                try:
                    query = text(f"SELECT * FROM pazienti WHERE IDP = '{patient_id}'")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                except Exception as e:
                    print(Bcolors.FAIL + f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
            else:
                print(Bcolors.FAIL + f"\n[ERROR] Invalid input..." + Bcolors.ENDC)


def getStoriaClinica(engine, ruolo):

    choice = ''

    print(Bcolors.OKCYAN + """
            [1] Storia clinica di tutti i pazienti
            [2] Ricerca paziente
            """ + Bcolors.ENDC)

    while choice != '1' and choice != '2':

        if ruolo == 2:

            while True:

                choice = input("\n[INFO] Seleziona opzione >>> ")

                if choice == '1':
                    query = text("SELECT ID_PAZIENTE, ID_PERSONALE, PATOLOGIA, PRESCRIZIONI FROM cure")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                elif choice == '2':
                    patient_id = input("\n[INFO] Input patient UID >>> ")
                    try:
                        query = text(f"SELECT ID_PAZIENTE, ID_PERSONALE, PATOLOGIA, PRESCRIZIONI FROM cure WHERE ID_PAZIENTE = '{patient_id}'")
                        with engine.connect() as conn:
                            res = pd.read_sql_query(query, conn)
                            return res
                    except Exception as e:
                        print(Bcolors.FAIL +  f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
                else:
                    print(Bcolors.FAIL + f"\n[ERROR] Invalid input...\n" + Bcolors.ENDC)

        else:
            choice = input("\n[INFO] Seleziona opzione >>> ")

            if choice == '1':
                query = text("SELECT * FROM cure")
                with engine.connect() as conn:
                    res = pd.read_sql_query(query, conn)
                    return res
            elif choice == '2':
                patient_id = input("\n[INFO] Input patient UID >>> ")
                try:
                    query = text(f"SELECT * FROM cure WHERE ID_PAZIENTE = '{patient_id}'")
                    with engine.connect() as conn:
                        res = pd.read_sql_query(query, conn)
                        return res
                except Exception as e:
                    print(Bcolors.FAIL + f"\n[ERROR] Something goes wrong. Error message : {e}\n" + Bcolors.ENDC)
            else:
                print(Bcolors.FAIL + f"\n[ERROR] Invalid input..." + Bcolors.ENDC)
