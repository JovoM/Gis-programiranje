# coding=utf-8
niz1=[1,2,3,"p"]
niz2=[6,7,8,"s"]
u=raw_input("Unesi p ili d:")
if u=="p":
   novi_niz = [None]*(len(niz1)+len(niz2))
   novi_niz[0::2] = niz1
   novi_niz[1::2] = niz2
   print "Novi niz je definisian na sledeci nacin" ,novi_niz
elif u=="d":
    novi_niz = [None] * (len(niz1) + len(niz2))
    novi_niz[::2] = niz2
    novi_niz[1::2] = niz1
    print "Novi niz je definisian na sledeci nacin" ,novi_niz


