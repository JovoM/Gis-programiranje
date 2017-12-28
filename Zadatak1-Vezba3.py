# coding=utf-8
#Modul sfera
import math
class Sfera:
    broj = 0
    def __init__(self ,r=0,xCentar=0,yCentar=0,zCentar=0):
        self.r=r
        self.xCentar=xCentar
        self.yCentar=yCentar
        self.zCentar=zCentar
        Sfera.broj+=1

    @staticmethod
    def broj_objekata():
        print "Broj kreiranih objekata je{0: d}".format(Sfera.broj)

    def zap_lopte(self):
        return (4/3)*(self.r**3)*math.pi

#Test Sfera
sfera = Sfera(4.0, 0, 0, 0)
globus = Sfera(12, 1.0, 1.0, 1.0)
bilijarska_lopta = Sfera(10, 10, 0)
jedinicna_sfera = Sfera(1, 0, 0, 0)

Sfera.broj_objekata()

print "Zapremina sfere je: " ,sfera.zap_lopte()
print "Zapremina globusa je:" ,globus.zap_lopte()
print "Zapremina bilijarske lopte je:" ,bilijarska_lopta.zap_lopte()
print "Zapremina jedinicne sfere je:" ,jedinicna_sfera.zap_lopte()




















