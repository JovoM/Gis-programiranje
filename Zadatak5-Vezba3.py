# coding=utf-8
from datetime import datetime

import math
class Osoba:
    def __init__(self,ime,prezime,dat_rodj,adresa):
        self.ime=ime
        self.prezime=prezime
        self.dat_rodj=dat_rodj
        self.adresa=adresa

    def postaviIme(self,ime):
        self.ime=ime
    def postaviPrezime(self,prezime):
        self.prezime=prezime
    def postavDatRodjenja(self,dat_rodj):
        self.dat_rodj=dat_rodj
    def postaviAdresa(self,adresa):
        self.adresa=adresa
    def info1(self):
        print "Ime:{0:s},Prezime:{1:s},Datum rodjena:{2:s},Adresa:{3:s}".format(str(self.ime),str(self.prezime),str(self.dat_rodj),str(self.adresa))

class Djak(Osoba):
    def __init__(self,ime,prezime,dat_rodj,adresa,skola="Vuk Karadzic",odeljenje="IX-5",god_upisa="2000"):
        Osoba.__init__(self,ime,prezime,dat_rodj,adresa)
        self.skola=skola
        self.odeljenje=odeljenje
        self.god_upisa=god_upisa

    def razredDjaka(self):
        a=str(self.odeljenje)
        b=a.split("-")
        return b[0]

    def obnavljanje(self):
        god_trajanja_skolovanja=8
        b=self.god_upisa
        tekuca_god=2017
        c=tekuca_god-int(b)
        if c<=god_trajanja_skolovanja:
            print "Ucenik nije obnavljao godinu"
        else :
            print "Ucenik je obnovio godinu"

class Zaposleni(Osoba):
    def __init__(self,ime,prezime,dat_rodj,adresa,naz_kompanije="GisSoft",departman="fotogrametrija",dat_zakljucenja="13.02.2016",dat_prekida="10.01.2016"):
        Osoba.__init__(self,ime,prezime,dat_rodj,adresa)
        self.departman=departman
        self.dat_zakljucenja=dat_zakljucenja
        self.dat_prekida=dat_prekida

    def dajRadniStaz(self):
        vreme=datetime.now()
        god=vreme.year
        mes=vreme.month
        datz=self.dat_zakljucenja
        datz1=datz.split(".")
        mes1=int(datz1[1])
        god1=int(datz1[2])
        m=(god-god1)*12 + abs(mes-mes1)
        print "Radni staz u mesecima u firmi je:",m

#Glavni program
#Djak
a=raw_input("Unesi ime :")
b=raw_input("Unesi prezime :")
c=raw_input("Unesi datum rodjenja :")
d=raw_input("Unesi adresu :")
e=raw_input("Unesi naziv skole :")
f=raw_input("Unesi odeljenje :")
v=raw_input("Unesi godinu upisa")
D=Djak(a,b,c,d,e,f,v)
print "Razred djaka:",D.razredDjaka()
print D.obnavljanje()
print D.info1()

#Zaposleni
a1=raw_input("Unesi ime:")
a2=raw_input("Unesi prezime :")
a3=raw_input("Unesi datum rodjenja :")
a4=raw_input("Unesi adresu :")
a5=raw_input("Unesi naziv kompanije:")
a6=raw_input("Unesi naziv departmana:")
a7=raw_input("Unesi datum zakljucenja:")
a8=raw_input("Unesi datum prekida:")
Z=Zaposleni(a1,a2,a3,a4,a5,a6,a7,a8)
print Z.dajRadniStaz()
print Z.info1()




