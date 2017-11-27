# coding=utf-8
#!/usr/bin/python
#Zadatak5-Vezba 1
a=input("Unesi petocifren broj")
b=float(a)
i=0
najcif=0
for i in range(1,5+1):
    a1=b-(b//10)*10
    if a1>najcif:
       najcif=a1
    b=b//10
    i=i+1
print 'Najveca cifra unetog petocifrenog broja je', najcif