# coding=utf-8
#!/usr/bin/python
#Zadatak3-Vezba1
p1s=float(input("Unesite stepene prvog pravca"))
p1m=float(input("Unesite minute prvog pravca"))
p1sec=float(input("Unesite sekunde prvog pravca"))
p2s=float(input("Unesite stepene drugog pravca"))
p2m=float(input("Unesite minute drugog pravca"))
p2sec=float(input("Unesite sekunde drugog pravca"))
p1=(p1s+p1m/60+p1sec/3600)
p2=(p2s+p2m/60+p2sec/3600)
u=p2-p1
u1=round(u,4)
print(u1)