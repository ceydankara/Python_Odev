
sayi=int(input("Sayı giriniz: "))

if sayi%2==0:
    print("Sayi çift sayidir.")
else:
    print("Sayi tek sayidir.")

print("*************************")


Not=int(input("Notunuzu giriniz: "))
if 90<=Not<=100:
    print("Harf notunuz A")
elif 80<=Not<=89:
    print("Harf notunuz B")
elif 70<=Not<=79:
    print("Harf notunuz C")
elif 60<=Not<=69:
    print("Harf notunuz D")
elif 59<=Not<=0:
    print("Harf notunuz E")
else:
    print("Yanlıs deger girildi.")

print("*************************")

yas=int(input("Yasınızı giriniz: "))
if 0<=yas<=12:
    print("Cocuk")
elif 13<=yas<=19:
    print("Genc")
elif 20<=yas<=59:
    print("Yetişkin")

elif 60<=yas:
    print("Yaslı")

else:
    print("Yanlıs degr girildi")

