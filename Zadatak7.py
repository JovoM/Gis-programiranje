# coding=utf-8
#!/usr/bin/python
#Zadatak7-Vezba1
xa=float(input("Unesi x za tacku A "))
ya=float(input("Unesi y za tacku A "))
xb=float(input("Unesi x za tacku B "))
yb=float(input("Unesi y za tacku B "))
xc=float(input("Unesi x za tacku C "))
yc=float(input("Unesi y za tacku C "))
xm=float(input("Unesi x za tacku koja se ispituje "))
ym=float(input("Unesi y za tacku koja se ispituje "))
fa=xa*(yb-yc)
fb=xb*(yc-ya)
fc=xc*(ya-yb)
povabc=abs((fa+fb+fc)/2)

ga=xa*(yb-ym)
gb=xb*(ym-ya)
gm=xm*(ya-yb)
povabm=abs((ga+gb+gm)/2)

lb=xb*(yc-ym)
lc=xc*(ym-yb)
lm=xm*(yb-yc)
povbcm=abs((lb+lm+lc)/2)

da=xa*(ym-yc)
dm=xm*(yc-ya)
dc=xc*(ya-ym)
povacm=abs((da+dm+dc)/2)
ukp=povabm+povbcm+povabc

if (ukp==povabc):
   print 'Da,upada u trougao.'
else:
   print 'Ne,ne upada u trougao.'