

while True:
    try:
        sayı = int(input("Bir sayı girin: "))
        break
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tamsayı girin.")
