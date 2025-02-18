
faiz=1.59

vade=36
krediAdi="ihtiyaç"

print(type(faiz))#degisken turunu görebilmek için

print(int(vade)+12)#vade değişkenini inte cevirmek için  
# print(int(krediAdi)) yapamayız cunku donusturebilir deger olmalı

faiz=str(faiz)
print(type(faiz))

vade=input("lütfen deger gir") #deger almak için
print (vade)

#string interpolation

print("Sectiğiniz vade sonucu elde edilen vade"+str(vade))
#ya da
print("Sectiğiniz vade sonucu elde edilen vade {vadeSayisi}".format(vadeSayisi=vade) )

isim="ceyda"
metin= "merhaba {name}".format(name=isim)
print(metin)


# f-string
metin=f"Hosgeldiniz {isim}"
print(metin)

#list
krediler=["ihtiyac kredisi","Tasıt kredisi","konut kredisi" ]
print(type(krediler))

print(krediler)
print(krediler[0])# kacıncı elemanı yazdırmak istersen 

print(len(krediler))#length


dizi=["ihtiyac kredisi",5,10.4]#dizinin elemanları birbirinden farklı yipde olabilir
print(dizi)

krediler.append("Özel kredi")#objeyi listenin sonuna ekleyen bir fonk
print(krediler)

krediler.pop(2)#verdiğin indeksteki elemanı siler eğer indeks vermezsen son elemanı siler
print(krediler)

krediler.remove("Tasıt kredisi")#remove de elemanı (indeks sırasına göre bulduğu ilk elemnaı siler yani iki tane olsaydı hangisinin indeksi küçükse onu)siler ama pop gibi indeksle degil degerle calısır yani silmek istediğin degeri girmelisin
print(krediler)

krediler.extend(["y kredisi","z kredisi"])#birden fazla deger girmek istersek böyle yaparız
print(krediler)


#for

for i in range(10):#range 10a kadar (0 dan) bir arttırarak calısma olayıdır
    print(i)


print("*************")

for i in range(5,10):
    print(i)

print("*************")

for i in range(0,51,10):# baslangıc sayisi,son sayı(dahil olmayacak),kac kac arttırmak istersen o sayi
    print(i)

print("*************")

krediler=["ihtiyac","tasıt","konut"]
for kredi in krediler:
    print(kredi)

print("*************")

#while

i=0
while i<10:#true oldugu surece içindekini calıstırır
    print("x")
    i+=1

print("*************")

while True:
    print("G")#true yazarsak while ın yanına bu sonsuz dongu olur bunu kırmak için break kullanılır
    break


#function

fiyat=100
indirim=20

def calculate():#fonk yazma
    print(100-20)

calculate()

def calculateWparams(a,b):
    print(a-b)

calculateWparams(13,7)

def sayHello(name):
    print(f"Hello {name}")

sayHello("C Ankara")



def calculateWreturn(price,discount):
    return price-discount

yeniFiyat= calculateWreturn(200,50)
print(yeniFiyat)

