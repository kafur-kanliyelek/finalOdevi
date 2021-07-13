# Net promoter Score
import matplotlib.pyplot as plt

class Nps:
    def __init__(self,sıfırPuanVerenSayısı, birPuanVerenSayısı, ikiPuanVerenSayısı,ucPuanVerenSayısı, dortPuanVerenSayısı,
besPuanVerenSayısı, altiPuanVerenSayısı, yediPuanVerenSayısı, sekizPuanVerenSayısı, dokuzPuanVerenSayısı, onPuanVerenSayısı):
        self.sıfırPuanVerenSayısı = sıfırPuanVerenSayısı
        self.birPuanVerenSayısı = birPuanVerenSayısı
        self.ikiPuanVerenSayısı = ikiPuanVerenSayısı
        self.ucPuanVerenSayısı = ucPuanVerenSayısı
        self.dortPuanVerenSayısı = dortPuanVerenSayısı
        self.besPuanVerenSayısı = besPuanVerenSayısı
        self.altiPuanVerenSayısı = altiPuanVerenSayısı
        self.yediPuanVerenSayısı = yediPuanVerenSayısı
        self.sekizPuanVerenSayısı = sekizPuanVerenSayısı
        self.dokuzPuanVerenSayısı = dokuzPuanVerenSayısı
        self.onPuanVerenSayısı = onPuanVerenSayısı


    def tümPuanlarıGetir(self):
        musteriMemnuniyetVerisi = (self.sıfırPuanVerenSayısı,self.birPuanVerenSayısı,
                                   self.ikiPuanVerenSayısı,self.ucPuanVerenSayısı,
                                   self.dortPuanVerenSayısı,self.besPuanVerenSayısı,
                                   self.altiPuanVerenSayısı, self.yediPuanVerenSayısı,
                                   self.sekizPuanVerenSayısı, self.dokuzPuanVerenSayısı, self.onPuanVerenSayısı)
        print(" Tüm puanlar(küçükten-büyüğe): ",musteriMemnuniyetVerisi)

    def puanGetir(self,sorgu):
        self.sorgu = sorgu
        musteriMemnuniyetVerisiSozluk= {0: f"0 puan veren müşteri sayısı: {self.sıfırPuanVerenSayısı}",
                                   1: f"1 puan veren müşteri sayısı: {self.birPuanVerenSayısı}",
                                   2: f"2 puan veren müşteri sayısı: {self.ikiPuanVerenSayısı}",
                                   3: f"3 puan veren müşteri sayısı: {self.ucPuanVerenSayısı}",
                                   4: f"4 puan veren müşteri sayısı: {self.dortPuanVerenSayısı}",
                                   5: f"5 puan veren müşteri sayısı: {self.besPuanVerenSayısı}",
                                   6: f"6 puan veren müşteri sayısı: {self.altiPuanVerenSayısı}",
                                   7: f"7 puan veren müşteri sayısı: {self.yediPuanVerenSayısı}",
                                   8: f"8 puan veren müşteri sayısı: {self.sekizPuanVerenSayısı}",
                                   9: f"9 puan veren müşteri sayısı: {self.dokuzPuanVerenSayısı}",
                                   10: f"10 puan veren müşteri sayısı: {self.onPuanVerenSayısı}"}


        #sorgu = input("0-5 aralığında değer gir: ")
        print(musteriMemnuniyetVerisiSozluk.get(sorgu,"aradığınız şeye ulaşamıyoruz"))

    def npsHesapla(self):
        toplamMusteri = self.sıfırPuanVerenSayısı + self.birPuanVerenSayısı + self.ikiPuanVerenSayısı + self.ucPuanVerenSayısı + \
                        self.dortPuanVerenSayısı + self.besPuanVerenSayısı + \
                        self.altiPuanVerenSayısı + self.yediPuanVerenSayısı + self.sekizPuanVerenSayısı + self.dokuzPuanVerenSayısı + self.onPuanVerenSayısı




        print("Toplam Musteri:", toplamMusteri)


        destekleyen = self.dokuzPuanVerenSayısı + self.onPuanVerenSayısı
        pasif = self.yediPuanVerenSayısı + self.sekizPuanVerenSayısı
        kotuleyen = self.sıfırPuanVerenSayısı + self.birPuanVerenSayısı + self.ikiPuanVerenSayısı + self.ucPuanVerenSayısı + self.dortPuanVerenSayısı + \
                    self.besPuanVerenSayısı + self.besPuanVerenSayısı

        musteriGrubu = {"kotuleyen":kotuleyen,
                        "pasif": pasif,
                        "destekleyen": destekleyen}
        print(f"müşteri grubu {musteriGrubu}")

        kotuleyenOrani = (kotuleyen/toplamMusteri)*100
        destekleyenOrani = (destekleyen/toplamMusteri)*100
        netTavsiyeSkoru = destekleyenOrani - kotuleyenOrani
        print("Kötüleyen oranı(yüzde): ",kotuleyenOrani)
        print("Destekleyen oranı(yüzde): ",destekleyenOrani)
        #print("Net Tavsiye Skoru:", netTavsiyeSkoru)

        if netTavsiyeSkoru <= 0:
            print("Net Tavsiye Skoru: ", netTavsiyeSkoru)
            print("Kötü, lütfen sıfırın üstüne çıkmaya çalışın")
        elif netTavsiyeSkoru > 0 and netTavsiyeSkoru <= 30:
            print("Net Tavsiye Skoru: ", netTavsiyeSkoru)
            print("İyi, lütfen otuzun üstüne çıkmaya çalışın")
        elif netTavsiyeSkoru > 30 and netTavsiyeSkoru <= 70:
            print("Net Tavsiye Skoru: ", netTavsiyeSkoru)
            print("Çok iyi, yüksek düzeyde müşteri sadakatine ulaşmak için 70'in üstüne çıkmalısınız.")
        else:
            print("Net Tavsiye Skoru: ", netTavsiyeSkoru)
            print("Mükemmel, yüksek düzeyde müşteri sadakatiniz var")

        plt.figure(figsize=(5, 5))
        dilimler = (destekleyen, pasif, kotuleyen)
        etiket = ("Destekleyenler", "Pasifler", "Kötüleyenler")
        renkler = ("g", "y", "r")
        plt.pie(dilimler, labels=etiket, colors=renkler, explode=(0, 0, 0.2), autopct="%.2f")
        plt.title("3 Tip Müşteri grafiği")

        plt.figure(figsize=(5, 5))
        dilimler2 = (destekleyen,kotuleyen) #pasifler istatistike etki etmediği için bu grafiği oluşturma ihtiyacı hissetim
        etiket2 = ("Destekleyenler", "Kötüleyenler")
        renkler2 = ("g","r")
        plt.pie(dilimler2, labels=etiket2, colors=renkler2, explode=(0.0,0.1),autopct="%.2f")
        plt.title("2 Tip Müşteri Grafiği")

        plt.show()


    def bargrafikOlustur(self):
        musteriMemnuniyetVerisi = ( self.sıfırPuanVerenSayısı, self.birPuanVerenSayısı, self.ikiPuanVerenSayısı, self.ucPuanVerenSayısı,
        self.dortPuanVerenSayısı, self.besPuanVerenSayısı, self.altiPuanVerenSayısı, self.yediPuanVerenSayısı, self.sekizPuanVerenSayısı, self.dokuzPuanVerenSayısı,
        self.onPuanVerenSayısı)

        sayiListesi = (0,1,2,3,4,5,6,7,8,9,10) #Değiştirilmeyeceği için tuple kullanıldı

        plt.bar(sayiListesi,musteriMemnuniyetVerisi)
        plt.xlabel("Müşterilerin Verdiği Puanlar")
        plt.ylabel("Verilen Puan Sayısı")
        plt.title("Net Promoter Score(NPS) Grafiği")
        plt.show()






