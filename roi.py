# ROI = (Gelir - (yatırım maliyeti + ürün maliyeti)) / (yatırım maliyeti + ürün maliyeti)

class Roi:
    def __init__(self):
        pass


    def roiHesapla(self):
        self.gelir = int(input("Gelir giriniz: "))
        self.ymaliyet = int(input("Yatırım maliyeti giriniz: "))  # yatırım maliyeit
        self.umaliyet = int(input("Ürün maliyeti giriniz: "))  # ürün maliyeti

        maliyet = self.ymaliyet + self.umaliyet
        roi = (self.gelir-maliyet)/maliyet
        roiYüzdesi = roi*100
        print("ROI: ",roi, "|  Roi Yüzdesi:", roiYüzdesi)
        while roiYüzdesi <= 100:
            if roiYüzdesi == 100:
                print("Dengeli. Kar-zarar yok.")
                break
            else:
                print(f"Zarardasın. Her 100 liralık yatırımda {roiYüzdesi} lira geri dönüş alıyorsunuz.")
                break
        else:
            print(f"Kardasın. Her 100 liralık yatırımda {roiYüzdesi} lira geri dönüş alıyorsunuz.")


