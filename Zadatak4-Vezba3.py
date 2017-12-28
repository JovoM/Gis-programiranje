# coding=utf-8
import math
class Inzenjer:
    def __init__(self,ime="Jovo",prezime="Marjanovic",maticni_br=123456,lic=2):
        self.ime=ime
        self.prezime=prezime
        self.maticni_br=maticni_br
        self.lic=lic

    def daj_Ime(self):
        return self.ime

    def daj_Prezime(self):
        return self.prezime

    def daj_Maticni_br(self):
        return self.maticni_br

    def daj_Licencu(self):
        return self.lic

    def postavi_Ime(self,ime):
        self.ime = ime

    def postavi_Prezime(self, prez):
            self.prezime = prez

    def postavi_Maticni_br(self, mat):
                self.maticni_br= mat

    def postavi_Licencu(self, lic):
                    self.lic = lic

    def informacije(self):
        print "Ime:{0:s}, Prezime:{1:s}, Maticni broj:{2:s}, Licenca:{3:s}".format(str(self.ime),str(self.prezime),str(self.maticni_br),str(self.lic))

class GeodetskiInzenjer(Inzenjer):
    
    def __init__(self,ime,prezime,maticni_br,lic,god_st):
        Inzenjer.__init__(self,ime,prezime,maticni_br,lic)
        self.god_st=god_st

    def daj_Godinu_Staza(self):
        return self.god_st

    def postavi_Godinu_Staza(self,god_st):
        self.god_st=god_st

    def informacije1(self):
        print  "Ime:{0:s}, Prezime:{1:s}, Maticni broj:{2:s}, Licenca:{3:s},Broj godine staza:{4:s}".format(str(self.ime),str(self.prezime),str(self.maticni_br),str(self.lic),str(self.god_st))

    def ispis_licence(self):
        b=self.daj_Licencu()
        if b == None:
            print "Nema licence"
        else:
          print  "Licenca je:", self.lic
a=GeodetskiInzenjer("Jovo","Marjanovic",1256463,None,20)
a.ispis_licence()

class ElektrotehnickiInzenjer(Inzenjer):
    def __init__(self,ime,prezime,maticni_br,lic,br_proj):
        Inzenjer.__init__(self,ime,prezime,maticni_br,lic)
        self.br_proj=br_proj

    def daj_Br_Proj(self):
        return self.br_proj

    def Postavi_Br_Proj(self,brp):
        self.br_proj=brp

    def Informacije2(self):
        print "Ime:{0:s}, Prezime:{1:s}, Maticni broj:{2:s}, Licenca:{3:s},Broj projekta:{4:s}".format(str(self.ime),str(self.prezime),str(self.maticni_br),str(self.lic),str(self.br_proj))

    def IspisLicence2(self):
        c = self.daj_Licencu()
        if c== None:
            print "Nema licence"
        else:
          print  "Licenca je:", self.lic

