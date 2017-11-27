# coding=utf-8
import random
br = 0
ime = input("Unesi svoje ime")
b = random.randint(1, 100)
print('Dobro dosao u igru "Igraj i pobedi".Potrebno je da pogodis broj koji je definisao racunar u opsegu od 10 do 100.Srecno')
while br<100:
    a = input("Unesi broj")
    a = int(a)

    br = br + 1

    if a < b:
        print('Tvoj broj je manji od zamisljenog')

    if a > b:
        print('Tvoj broj je veci od zamisljenog')

    if a == b:
        break

if a==b:
   br = str(br)
   print('Odlicno,vi ste pogodili zamisljen broj sa broje pokusaja' ,  br)
