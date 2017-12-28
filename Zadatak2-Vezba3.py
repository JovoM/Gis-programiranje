# coding=utf-8
import math
# Modul geometrija
class Tacka:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def po_xosi(self,x_pomeraj):
       self.x=float(self.x) + x_pomeraj

    def po_yosi(self,y_pomeraj):
         self.y=float(self.y) + y_pomeraj

    def rastojanje_do(self, t):
        dx = self.x - t.x
        dy = self.y - t.y
        return math.sqrt(dx ** 2 + dy ** 2)

class Duz:
    def __init__(self,pT=0,kT=0):
        self.pT=pT
        self.kT = kT

    def kreiraj_duz(self,xP,yP,xK,yK):
        PT=Tacka(xP,yP)
        KT=Tacka(xK,yK)
        d=Duz(PT,KT)
        return d

    def duzina_duzi(self):
        dd=self.pT.rastojanje_do(self.kT)
        return dd
    def __str__(self):
        return "Y koordinata pocetne tacke: {0:s}, X koordinata pocetne tacke: {1:s}, Y koordinata krajnje tacke: {2:s}, X koordinata krajnje tacke: {3:s}".format(str(self.pT.y),str(self.pT.x),str(self.kT.y),str(self.kT.x))

# Test Geometrija
pX=raw_input("Unesi x koordinatu pocetne tacke:")
pY=raw_input("Unesi y koordinatu pocetne tacke:")
kX=raw_input("Unesi x koordinatu krajnje tacke:")
kY=raw_input("Unesi y koordinatu krajnje tacke:")
pT=Tacka(pX,pY)
kT=Tacka(kX,kY)
D=Duz(pT,kT)
d=Duz()
l=d.kreiraj_duz(3,5,6,7)
print l.__str__()
print D.__str__()
px=float(input("Unesi x pomeraj:"))
py=float(input("Unesi y pomeraj:"))
kT.po_xosi(px)
kT.po_yosi(py)
d1=Duz(pT,kT)
print d1.__str__()




