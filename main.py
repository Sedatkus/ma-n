print("Merhaba Etiya")
#! string = metinsel ifade
text = "10"
print(text)
#! integer = tam sayı
number = 5
print(number)
#! double,float,decimal = ondalıklı sayı
dnumber = 5.3
#! matematiksel
print(dnumber) # ondalıklı ifadeyi yazdırır
print(number + 5) # 5 + 5 = 10
print(number - 5) # 5 - 5 = 0
print(number * 5) # 5 * 5 = 25
print(number / 5) # 5 / 5 = 1
print(number % 3) # Bu ifade kalanı verir = 2
#! boolean,bool = true veya false
print(1 == 1) # True
print(2 != 2) # False

print(1 > 2) # F
print(1 < 2) # T

print(1 <= 2) # T
print(1 >= 2) # F

print(10 % 2 == 0) # T
print(50 / 2 == 25) # T
print(50 / 2 == 25.0) # T

text = "Merhaba Etiya"
#print(text.upper()) # Büyük harfle yazar
print(text.lower()) # Küçük harfle yazdırır
print(text.startswith("Mer"))
print(text.endswith("Etiya"))
name = "Halit"
age= "23"
company = "Kodlamaio"
print(f"{name} {age} yaşında {company}'da çalışıyor")
print(name + " " + age + " " + "yaşında" + " " + company + "'da çalışıyor")


######   KODLAMA.iO  Engin Hoca Notlar #########
baslik = "Haberiniz Olsun" #string metinsel bir ifade 
vade = 12  # integer sayısal bir ifade
faizoranı = 1.76 # Float ondalıklı bir ifade
print(baslik)
print(type(baslik))

print(vade)
print(type(vade))

print(faizoranı)
print(type(faizoranı))

mesaj = "Hoşgeldin"
musteriAdi = "SEDAT"
musteriSoyadi = "KUŞ"
# print(mesaj+" "+musteriAdi+" "+musteriSoyadi) (Tırnak içi metinsel ifade olduğu için boşluk bırakmak için)
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi

print(sonucMesaj)

sayi1 = 10 #int
sayi2 = 20 #int
print(sayi1+sayi2) # 10 + 20 = 30

print("İlk Gün Ödevi SEDAT KUŞ")