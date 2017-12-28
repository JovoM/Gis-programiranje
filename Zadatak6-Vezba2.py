# coding=utf-8
import numpy as np
br=input("Unesi broj tacaka: ")
x=[]
y=[]
i=0
while i < br:
    x.append(input("Unesi x koordinatu:"))
    y.append(input("Unesi y koordinatu:"))
    i=i+1

stepen_polinoma=input("Unesi stepen polinoma")
koefcijent=np.polyfit(x,y,stepen_polinoma)
fitovanje=np.poly1d(koefcijent)
print "Polinom unetih tacaka izgleda :",fitovanje
