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

#Yöntem 1
result = []

for char in text:
    if char in ",.":
        result.append(" ")
    else:
        result.append(char.upper())

result_str = ''.join(result)

result_list = result_str.split()

print(result_list)


#Yöntem 2

result = [word.upper() for word in text.replace(",", " ").replace(".", " ").split()]
print(result)
