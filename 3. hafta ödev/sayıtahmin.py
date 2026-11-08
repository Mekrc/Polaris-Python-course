import random 


sayı =  random .randint(1,100)

print("1 ile 100 arasında bir sayı tuttum. Tahmin etmeye çalışın!") 
while True:
    tahmin = int (input("Tahmininizi girin: "))
    if tahmin < sayı:
        print("Daha büyük bir sayı söyleyin.")  
    elif tahmin > sayı:
        print("Daha küçük bir sayı söyleyin.")  
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break