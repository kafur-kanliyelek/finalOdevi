class Musteri:
    musteriPuanListesi = []

    def __init__(self):
        self.ad = input("Ad: ")
        self.soyad = input("Soyad: ")


    def puanVer(self):
        while True:
            self.verilenPuan = int(input("Kaç puan verdiğini gir: "))

            onay = input("Verdiğin puanı onaylıyorsan 'o' yaz, çıkmak için 'out' yaz: ")
            if onay == "o":
                while self.verilenPuan <= 10 and self.verilenPuan > 0:
                    print(self.ad, self.soyad, "verdiğin puan:", self.verilenPuan)
                    self.musteriPuanListesi.append(self.verilenPuan)
                    print("Verilen Puanlar",self.musteriPuanListesi)

                    break
                else:
                    print("Yanlış değer girdiniz")
            elif onay == "out":
                print("Çıkılıyor")
                break

            else:
                print("Girdiğin puanı onaylamadın. Onaylamak için 'o' harfini girebilirsin. Yeniden puan girmeni bekliyoruz...")







