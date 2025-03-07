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
