def hesap_makinesi(sayi1, sayi2, islem):
    if islem == "+":
        return sayi1 + sayi2
    elif islem == "-":
        return sayi1 - sayi2
    elif islem == "*":
        return sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            return "Hata: Sıfıra bölme yapılamaz!"
        return sayi1 / sayi2
    else:
        return "Geçersiz işlem!"
print("******************************")

def yas(yas):
    a=100-yas
    print(f"{a} yıl sonra 100 yasındasınız")

yas2= yas(12)

print("********************")
