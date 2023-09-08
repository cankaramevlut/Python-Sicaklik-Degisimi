def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*1.8)+32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
     celsius = (fahrenheit - 32) / 1.8
     return celsius

print("Sıcaklık Dönüştürücü Programına Hoş Geldiniz!")
secim = input("Dönüştürmek istediğiniz birimi seçin:\n1. Santigratı Fahrenheit'a çevir\n2. Fahrenheit'i Santigrata çevir\nSeçiminiz (1/2): ")

if secim == "1":
    celsius = float(input("Santigrat sıcaklık değerini girin: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Santigrat, {fahrenheit} Fahrenheit'a eşittir.")

elif secim == "2":
    fahrenheit = float(input("Fahrenheit sıcaklık değerini girin: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit, {celsius} Santigrat'a eşittir.")

else:
    print("Geçersiz seçim! Lütfen 1 veya 2 girin.")