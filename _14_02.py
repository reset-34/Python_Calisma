#kütüphane dahil ediyoruz
import operations
#giriş alıyoruz
n= int (input("Faktöriyeli Hesaplanacak sayısı giriniz: "))

#Hesaplama yap
result = operations.recursive_factorial(n)

#Çıktı 
print(f"{n}!= {result}")