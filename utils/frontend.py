from time import sleep
import os

from .logos import header, header_anagrafica, logo, header_storia

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


def join_art(s1, s2, str_between=''):
    lines1 = s1.split('\n')
    lines2 = s2.split('\n')
    max_dist = max([len(s) for s in lines1])
    f_str = '{:<' + str(max_dist) + '}{}{}'
    s3 = "\n".join([f_str.format(str1, str_between, str2) for str1, str2 in zip(lines1, lines2)])
    return s3

def createLogo(HEADER, LOGO):

    fullLogo = join_art(HEADER, LOGO)
    fullLogo = Bcolors.OKCYAN + fullLogo + Bcolors.ENDC

    return fullLogo


def createMainScreen():
    os.system("cls")
    print(Bcolors.OKCYAN + createLogo(header, logo) + Bcolors.ENDC)

    print(Bcolors.OKCYAN + """
        SELEZIONARE UN'OPERAZIONE DA ESEGUIRE

        [1] Visualizza anagrafica pazienti
        [2] Visualizza parametri vitali
        [3] Analisi parametri vitali
        [4] Visualizza la storia clinica dei pazienti
        [00] Chiudi il programma

        """ + Bcolors.ENDC)

def createAnagraficaScreen():
    os.system("cls")
    print(Bcolors.OKCYAN + createLogo(header_anagrafica, logo) + Bcolors.ENDC + "\n")


def createStoriaClinicaScreen():
    os.system("cls")
    print(Bcolors.OKCYAN + createLogo(header_storia, logo) + Bcolors.ENDC + "\n")

def fakeBuild():
    print("\n[*] Connecting to server...")
    sleep(2)
    print("[#] Connection established...")
    sleep(1)
    print("[*] Validating credentials...")
    sleep(2)
    print("[#] Credential validated...")
    sleep(1)
    print("\n\n[INFO] Welcome to FaBE-CARE")
    sleep(3)