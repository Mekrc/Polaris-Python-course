def main():
    fiyat = float(input("Fiyatı girin: "))
    oran = float(input("İndirim oranını girin: "))

    if 0<oran<100:
        indirim = fiyat * oran / 100
        yeni_fiyat = fiyat - indirim
        print(f"İndirimli fiyat: {yeni_fiyat}") 
    else: 
        print("Geçersiz indirim oranı. Lütfen 0 ile 100 arasında bir değer girin.")
        main()  

main()  