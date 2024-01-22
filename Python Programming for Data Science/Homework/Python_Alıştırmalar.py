# Görev 1: Verilen degerlerin veri yapilarini inceleyiniz
x = 8  # int
y = 3.2  # float
z = 8j + 18  # complex
a = "Hello World"  # str
b = True  # bool
c = 23 < 22  # bool
l = [11, 2, 3, 4]  # list
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}  # dict
t = ("Machine Learning", "Data Science")  # tuple
s = {"Python", "Machine Learning", "Data Science"}  # set

type(s)

# Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
# kelime kelime ayiriniz.

text = "The goal is to turn data into information, and information into insight."

text = "The goal is to turn data into information, and information into insight."

result = [word.upper() for word in text.replace(",.", " ").split()]
print(result)

result = []

for char in text:
    if char in ",.":
        result.append(" ")
    else:
        result.append(char.upper())

result_str = ''.join(result)

result_list = result_str.split()

print(result_list)

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Görev 3: Verilen listenin eleman sayısına bakınız.

len(lst)

# Sıfırıncı ve onuncu indeksdeki elemanları çağırınız.

print("Sıfırıncı indeks: ", lst[0])
print("Onuncu indeks: ", lst[10])

# Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

data_list = lst[0:4]
print(data_list)

# Sekizinci indeksteki elemanı silin.

lst.pop(8)

# Yeni eleman ekleyiniz.

lst.append("YENİ ELEMAN :)")

# Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")

# Görev 4:  Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dct = {'Christian': ["America", 18],
       'Daisy': ["England", 12],
       'Antonio': ["Spain", 22],
       'Dante': ["Italy", 25]}

# Key Değerlerine erişiniz

dct.keys()

# Value Değerlerine erişiniz

dct.values()

# Daisy key'ine ait 12 değerini 13 olarak güncelle

dct["Daisy"][1] = 13

# Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dct.update({"Ahmet": ["Turkey", 24]})

# Antonio'yu dictionary'den siliniz.

del dct["Antonio"]

# Görev 4: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

sayilar = [12, 13, 18, 93, 221]


# Yöntem 1
def func(sayilar):
    even_list = []
    odd_list = []
    for sayi in sayilar:
        if sayi % 2 == 0:
            even_list.append(sayi)
        else:
            odd_list.append(sayi)
    return even_list, odd_list


even_list, odd_list = func(sayilar)


# Yöntem 2

def func(sayilar):
    even_list = [sayi for sayi in sayilar if sayi % 2 == 0]
    odd_list = [sayi for sayi in sayilar if sayi % 2 != 0]
    return even_list, odd_list


even_list, odd_list = func(sayilar)

# Görev 6:Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi
# öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

# Yöntem 1
muh_fak = []

for muh_fak, ogrenci in enumerate(ogrenciler, 1):
    if muh_fak <= 3:
        print("Müdendislik Fakültesi ", muh_fak, ". öğrenci: ", ogrenci)
    else:
        print("Tıp Fakültesi ", muh_fak, ". öğrenci: ", ogrenci)

# Yöntem 2

sonuclar = [
    "Mühendislik Fakültesi {indeks}. öğrenci: {ogrenci}" if indeks <= 3 else "Tıp Fakültesi {indeks}. öğrenci: {ogrenci}"
    for indeks, ogrenci in enumerate(ogrenciler, 1)]

for sonuc in sonuclar:
    print(sonuc)

# Görev 7:Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri
# yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "'SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

dersler = zip(kredi, ders_kodu, kontenjan)

for ders in dersler:
    print(f"Kredisi {ders[0]} olan {ders[1]} kodlu dersin kontenjanı {ders[2]} kişidir.")

# Görev 8:Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1.küme 2.kümeyi kapsiyor ise ortak elemanlarını eğer
# kapsamıyor ise 2.kümenin 1.kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume(kume1, kume2):
    if kume2.issubset(kume1):
        ortak = kume2.intersection(kume1)
        print({ortak})
    else:
        fark = kume2.difference(kume1)
        print(fark)


kume(kume1, kume2)
