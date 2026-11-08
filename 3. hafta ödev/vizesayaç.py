import datetime 



sınav_tarihi = input("Sınav tarihini girin (gg/aa/yyyy formatında): ")

while True:
    sınav_tarihi = datetime.datetime.strptime(sınav_tarihi, "%d/%m/%Y")
    bugünün_tarihi = datetime.datetime.now()
    kalan_günler = (sınav_tarihi - bugünün_tarihi).days

    if kalan_günler > 0:
        print(f"Sınava {kalan_günler} gün kaldı")
    elif kalan_günler == 0:
        print("Sınav bugün")
    else:
        print("Sınav tarihi geçmiş")
    break

        