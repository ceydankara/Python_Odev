baslik="İhtiyaç Kredisi"
print(baslik)

baslik="Taşıt Kredisi"
print(baslik)
#ayni değişken adıyla farklı şeyler yazabiliriz

vade=36 #numerik bir ifade
vade2="36" #metinsel bir ifade
ekvade=6
aylikOdeme=200.50 #float veri türü

#bool,boolean true ya da false döndürür.
yukselisteMi=True

#matematiksel operatorler
#+
print(1+3)
print(vade + 6)
print(vade + ekvade)

#-
print(5-5)
print(vade-ekvade)
print(vade-9)


#*
print(12*2)
print(vade*3)

#/
print(5/5)
print(vade/2)
#bolme operatoru float deger dondurur tam deger istersen // kullan


#mod alma
print(10%2)
print(6%4)
print (vade%3)

#mantıksal operatorler

print(1<3)
print(1>8)
print(1<=3)

print(1!=1)
print(1!=2)

# or and

print(1>2 or 5>2)
print(1>2 or 5>2 and 3>2)



#if else
sayi1=10
sayi2=20

if sayi1>sayi2:
    print("Sayi1 sayi2 den buyuktur.")
    print("hala if içindeyiz")

elif sayi1==sayi2:
    print("iki sayi birbirine esittir")

else:
    print("sayi1,sayi2 den buyuktur")

print("burası iften çıktı")










