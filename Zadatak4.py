#Zadatak 4-Vezba 1
# coding=utf-8
#!/usr/bin/python
import math
a=input("Unesite prvi cetvorocifren broj: ")
b=input("Unesite drugi cetvorocifren broj: ")
a1=float(a)
b1=float(b)
i=0
sums=0
sump=0
sumnp=0
for i in range(1,4+1):
    sums+=b1-(b1//10)*10
    if (i%2==0):
        sump+=a1-(a1//10)*10
    else:
        sumnp+=a1-(a1//10)*10
    b1=b1//10
    a1=a1//10
    i+=1
print 'Suma cifara drugog broja=',sums
print 'Razlika zbira cifara prvog broja na parnim i neparnim pozicijama=',sumnp-sump
