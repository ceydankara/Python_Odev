# Basit Hesap Makinesi 
ilkSayi= int(input("İlk sayi: "))

ikinciSayi = int(input("ikinci sayi: "))

islem= input("Lütfen işlem seciniz(+,-,*,/): ")

if islem=="+" :
   a= int(ikinciSayi+ilkSayi)
   print("sonuc:", a)
elif islem == "-":
    a = ilkSayi - ikinciSayi
    print("Sonuç:", a)
elif islem == "*":
    a = ilkSayi * ikinciSayi
    print("Sonuç:", a)
elif islem == "/":
    if ikinciSayi != 0:
        a = ilkSayi / ikinciSayi
        print("Sonuç:", a)
    else:
        print("Hata: Sıfıra bölme yapılamaz!")
else:
    print("Geçersiz işlem seçtiniz!")
    
