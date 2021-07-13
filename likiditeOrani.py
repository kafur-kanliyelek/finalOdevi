""""
Likidite Oranları: İşletmenin kısa süreli borçlarını ödeyebilme gücünü ve çalışma sermayesinin yeterli olup olmadığını saptayabilmek için kullanılır.
    Cari Oran = Dönen Varlıklar / Kısa Vadeli Yabancı Kaynaklar #kısaVadeliYabKaynaklar, Oranın 2.00'ın üzerinde olması arzu edilir.

0 – 1,00            :  Cari Oran düşük seviyede

1 – 1,85             :  Cari Oran kabul edilebilir seviyede

1,85 ve üzeri      :  Cari Oran iyi seviyede
Cari oranın 10 – 15 gibi aşırı yüksek olması da firmanın sahip olduğu nakdi, yeterli verimlilikte kullanamadığına veya yanıltıcı bir bilançoya işaret etmektedir.

    Asit - Test Oranı = (Dönen Varlıklar - Stoklar) / Kısa Vadeli Yabancı Kaynaklar #Oranın 1.00'ın üzerinde olması arzu edilir.
    Nakit Oranı = (Hazır Değerler + Menkul Kıymetler) / Kısa Vadeli Yabancı Kaynaklar #Oranın 1.00'ın üzerinde olması arzu edilir.
        Nakit oran = 0,20 olması beklenilen seviyedir.
        Nakit Oran < 0,20 ise ; firma nakit akışında sorunlar yaşayabilir ve dış kaynak kullanımında yeni arayışlar içersine girer.
        Nakit Oran >0,20 ise, paranın verimli kullanılıp kullanılmadığı irdelenmelidir.
    Stok Bağımlılık Oranı = [Kıs. Vad. Yab. Kaynaklar - (Hazır Değerler + Menkul Kıymetler)] / Stoklar
"""

class Likidite:
    def __init__(self,donenVarliklar,kısaVadeliYabKaynaklar):
        self.donenVarlıklar = donenVarliklar
        self.kısaVadeliYabKaynaklar = kısaVadeliYabKaynaklar



    def cariOran(self):
        cariOran = self.donenVarlıklar / self.kısaVadeliYabKaynaklar
        print("Cari Oran: ", cariOran)
        if cariOran >= 0 and cariOran < 1:
            print("Cari Oran düşük seviyede")
        elif cariOran >= 1 and cariOran < 1.85:
            print("Cari Oran kabul edilebilir seviyede")
            if cariOran == 1:
                    print("Firma sahip olduğu dönen varlıkları ile kısa vadeli borçlarını ancak ödeyebiliyor")
        elif cariOran >= 1.85 and cariOran < 10:
            print("Cari Oran iyi seviyede ")
            if cariOran == 2:
                print("Cari oranın 2 olması ise, firmanın kısa vadede ödemesi gereken borçlarının 2 katı kadar likit varlığa sahip olduğunu belirtir.")
        elif cariOran >= 10:
            print("Cari oranın 10 – 15 gibi aşırı yüksek olması da firmanın sahip olduğu nakdi, yeterli verimlilikte kullanamadığına veya yanıltıcı bir bilançoya işaret etmektedir.")
        else:
            print("oo bir şeyler ters gitti")
        return cariOran

    def asitTestOran(self):
        stoklar = int(input("Stoklar giriniz: "))
        asitTestoran = (self.donenVarlıklar-stoklar) / self.kısaVadeliYabKaynaklar
        print("Asit Test Oranı", asitTestoran)
        if asitTestoran < 1:
            print("Asit-test oranı arzu edilen seviyenin altında. Şirket sadece dönen varlıkları ile borçlarını ödeyemiyor.")
        elif asitTestoran == 1:
            print("Asit-test oranı arzu edilen seviyede. Şirket sadece dönen varlıkları ile borçlarını ödeyebiliyor")
        elif asitTestoran > 1:
            print("Asit-test oranı arzu edilen seviyede. Şirket sadece dönen varlıkları ile borçlarından fazlasını ödeyebiliyor")
        else:
            print("oo bir şeyler ters gitti")

    def nakitOranı(self):
        hazirDegerler = int(input("Hazır Değerler giriniz: "))
        menkulKiymetler = int(input("Menkul Kıymetler giriniz"))
        nakitOrani = (hazirDegerler + menkulKiymetler) / self.kısaVadeliYabKaynaklar
        print("Nakit Oranı", nakitOrani)
        if nakitOrani < 0.20:
            print("DİKKAT! Nakit oranı arzu edilen seviyenin altında. Firma nakit akışında sorunlar yaşayabilir ve dış kaynak kullanımında yeni arayışlar içerisine girebilir.")
        elif nakitOrani == 0.20:
            print("Nakit oranı arzu edilen seviyede")
        elif nakitOrani > 0.20:
            print("Paranın verimli kullanılıp kullanılmadığını araştırmalısın")

    def stokBagimlilikOran(self):
        stoklar = int(input("Stoklar giriniz: "))
        asitTestoran = (self.donenVarlıklar - stoklar) / self.kısaVadeliYabKaynaklar
        while asitTestoran >= 1:
            print("Asit-test oranı 1 değerinin üzerinde. Bu oranı hesaplamaya ihtiyacınız yok")
            break
        else:
            print("Asit-test oranı 1 değerinin altında. Borçların geri ödenmesinde işletme stoklara bağımlıdır. "
                  "Stok bağımlılık oranını hesaplamamız için lütfen aşağıdaki değerleri giriniz. ")
            hazirDegerler = int(input("Hazır Değerler giriniz: "))
            menkulKiymetler = int(input("Menkul Kıymetler giriniz: "))
            stokBagimlilikOrani = (self.kısaVadeliYabKaynaklar - (hazirDegerler + menkulKiymetler))  / stoklar
            print("Stok Bağımlılık Oranı: ", stokBagimlilikOrani)






