import subprocess
import os
import time

# def clear():
def clear():
    os.system('clear')

def run_update():    
    clear()
    print("Aktualizuje system\n")
    os.system("sudo apt-get update")
    print("\nUPDATE - zakończono\n")
    os.system("sudo apt-get full-upgrade -y")
    print("\nFULL UPGRADE - zakończono\n")
    os.system("sudo apt-get dist-upgrade -y")
    print("\nDIST UPGRADE - zakończono\n")
    os.system("sudo apt-get autoremove -y")
    print("\nAUTOREMOVE - zakończono\n")
    os.system("sudo apt-get autoclean -y")
    print("\nAUTOCLEAN - zakończono\n")
    time.sleep(2)
    clear()
    print("Zaktualizowano system")
    time.sleep(2)
    # sprawdz czy w systemie jest zainstalowana conda
    # jesli tak to zaktualizuj
    if os.path.exists("/home/$(whoami)/anaconda3/bin/conda"):
        os.system("/home/$(whoami)/anaconda3/bin/conda update conda -y")
        print("\nZaktualizowano conda\n")
        os.system("/home/$(whoami)/anaconda3/bin/conda update --all")
        print("\nZaktualizowano pakiety conda\n")
        time.sleep(2)

if __name__ == "__main__":
    # sprawdz jaki system jest zainstalowany
    # jesli linux to zaktualizuj system
    # jesli windows to wyswietl komunikat
    if os.name == "nt":
        print("Ten program nie działa na systemie Windows")
        time.sleep(2)
        exit(0)
    else:
        run_update()
