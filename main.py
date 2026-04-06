# class_tuwuncha


📘 Class (Sinf) haqida tushuncha
Class (sinf) — bu dasturlashda obyektlar yaratish uchun qolip (shablon) hisoblanadi. U ichida xususiyatlar (atributlar) va funksiyalar (metodlar) bo‘ladi.

Oddiy qilib aytganda:
👉 Class — bu reja, obyekt esa shu reja asosida qurilgan narsa.

🔹 1. Oddiy misol (Python’da)
class Talaba:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def tanishtir(self):
        print(f"Mening ismim {self.ism}, yoshim {self.yosh}")
📌 Tushuntirish:
__init__ — konstruktor (obyekt yaratilganda ishlaydi)

self — obyektning o‘zi

ism, yosh — atributlar

tanishtir() — metod

🔹 2. Obyekt yaratish
t1 = Talaba("Ali", 20)
t1.tanishtir()
🟢 Natija:

Mening ismim Ali, yoshim 20
🧠 Masalalar (mashqlar)
✅ 1-masala: Mashina klassi
Shart:
Mashina nomli class yarating. Unda:

marka

rang

bo‘lsin va info() metodi chiqarib bersin.

✔ Yechim:
class Mashina:
    def __init__(self, marka, rang):
        self.marka = marka
        self.rang = rang

    def info(self):
        print(f"Marka: {self.marka}, Rang: {self.rang}")

m1 = Mashina("Chevrolet", "oq")
m1.info()
✅ 2-masala: Kitob klassi
Shart:
Kitob classi:

nomi

muallifi

va malumot() metodi bo‘lsin.

✔ Yechim:
class Kitob:
    def __init__(self, nomi, muallifi):
        self.nomi = nomi
        self.muallifi = muallifi

    def malumot(self):
        print(f"Kitob: {self.nomi}, Muallif: {self.muallifi}")

k1 = Kitob("Alkimyogar", "Paulo Coelho")
k1.malumot()
✅ 3-masala: Hisob klassi
Shart:
Hisob classi:

son1

son2

va qo‘shish metodini yozing.

✔ Yechim:
class Hisob:
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def qoshish(self):
        print(self.son1 + self.son2)

h = Hisob(5, 7)
h.qoshish()
🔥 Qo‘shimcha tushunchalar:
Class — shablon

Obyekt — classdan yaratilgan nusxa

Metod — class ichidagi funksiya

Atribut — obyektning xususiyati
