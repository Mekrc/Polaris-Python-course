vize_notu = float(input("Vize notunu girin: "))
final_notu = float(input("Final notunu girin: "))   

def harf_notu(vize, final):
    ortalama = (vize * 0.4) + (final * 0.6)
    
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 80:
        return "BB"
    elif ortalama >= 75:
        return "CB"
    elif ortalama >= 70:
        return "CC"
    elif ortalama >= 65:
        return "DC"
    elif ortalama >= 60:
        return "DD"
    else:
        return "FF"

print("Harf Notu:", harf_notu(vize_notu, final_notu))
