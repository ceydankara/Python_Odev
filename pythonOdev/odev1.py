
Ad=str(input("Adınızı giriniz: "))
Yas=int(input("Yasınızı giriniz: "))
DogumYılı= int(input("Dogum yılınız giriniz: "))

print(f"Merhabaa {Ad}! {Yas} yasındasın ve {DogumYılı} yılında dogdun")


sayı1=int(input("İlk sayiyi giriniz: "))
sayı2=int(input("ikinci sayiyi giriniz: "))

toplam=sayı1+sayı2

if sayı1>= sayı2:
    fark=sayı1-sayı2
else :
    fark=sayı2-sayı1

if sayı2!=0:
    bolum= sayı1/sayı2
else:
    print("HATA (sıfıra bolme)")

carpım= sayı1*sayı2

print(toplam,fark,bolum,carpım)