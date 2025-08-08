def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    if b == 0:
        return "Hata: Sıfıra bölünemez!"
    return a / b

def hesap_makinesi():
    print("Temel Hesap Makinesi")
    while True:
        print("\nİşlem seçin:")
        print("1- Toplama")
        print("2- Çıkarma")
        print("3- Çarpma")
        print("4- Bölme")
        print("5- Çıkış")

        secim = input("Seçiminiz: ")
        if secim == '5':
            print("Programdan çıkılıyor...")
            break

        if secim not in ('1','2','3','4'):
            print("Geçersiz seçim!")
            continue

        try:
            sayi1 = float(input("Birinci sayıyı girin: "))
            sayi2 = float(input("İkinci sayıyı girin: "))
        except ValueError:
            print("Hatalı giriş! Lütfen sayı girin.")
            continue

        if secim == '1':
            sonuc = topla(sayi1, sayi2)
        elif secim == '2':
            sonuc = cikar(sayi1, sayi2)
        elif secim == '3':
            sonuc = carp(sayi1, sayi2)
        elif secim == '4':
            sonuc = bol(sayi1, sayi2)

        print("Sonuç:", sonuc)

if __name__ == "__main__":
    hesap_makinesi()
