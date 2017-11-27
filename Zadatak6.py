# coding=utf-8
#Zadatak6-Vezba 1
b=(raw_input("Unesi 5 karaktera:"))
br=0
for i in b:
    if (i=="0"):
        br+=1
    elif (i=="9"):
        br+=1
    elif (i=="1"):
        br+=1
    elif (i=="2"):
        br+=1
    elif (i=="3"):
        br+=1
    elif (i=="4"):
        br+=1
    elif (i=="5"):
        br+=1
    elif (i=="6"):
        br+=11
    elif (i=="7"):
        br+=1
    elif (i=="8"):
        br+=1
    else:
        br=br
print 'Broj pojavljivanja cifara u unetom karakteru je', br



