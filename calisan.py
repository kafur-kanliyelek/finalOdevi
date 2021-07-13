class Calisan:
    calisanlar = []
    def __init__(self):
        pass



    def personelEkle(self):
        self.id = input("Çalışan ID kodunu giriniz: ")
        self.adSoyad= input("Çalışanın ismini giriniz: ")
        self.maas = int(input("Çalışanın Maaşını giriniz: "))

        self.calisanListesi = {self.id: self.adSoyad}
        self.calisanlar.append(self.id)
        print(f"{self.adSoyad} adlı kişi listeye eklendi. Kişinin id numarası: {self.id}")
        print("Çalışanların listesi(id): ",self.calisanlar)
        return



