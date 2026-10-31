dogum = input("Doğum yılınızı girin: ")

yaş = 2026 - int(dogum)
print(f"yaşınız: {yaş}")
if yaş < 18:
    print("Reşit değilsiniz.") 
else:
    print("Ehliyet alabilirsiniz.")