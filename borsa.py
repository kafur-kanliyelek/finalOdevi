#f/k hesapla
#piyasa değeri
#hisse başına kar

import matplotlib.pyplot as plt

class Borsa:
    def __init__(self):
        self.hissefiyatı = int(input("Hisse fiyatı giriniz: "))
        self.toplamhissesayısı = int(input("Toplam hisse sayısını giriniz: "))
        self. isletmenetkari = int(input("İşletme net karını giriniz: "))
        self.hissebasikar = self.isletmenetkari / self.toplamhissesayısı


    def hisseBasiKar(self):
        print(f"\nHisse başı kar: {self.hissebasikar} \n")
        return self.hissebasikar

    def fkHesapla(self):
        fk = self.hissefiyatı / self.hissebasikar
        print("Fiyat-Kazanç Oranı: ", fk)
        print(f"1 Türk Lirası kar etmek için {fk} lira ödüyorsunuz\n")
        return fk

    def piyasaDegeri(self):
        piyasaDegeri = self.hissefiyatı * self.toplamhissesayısı
        print("Piyasa Değeri: ", piyasaDegeri)
        return piyasaDegeri









