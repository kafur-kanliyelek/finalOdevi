import roi
import nps
import calisan
import borsa
import musteriMemnuniyet
import matplotlib.pyplot as plt
import likiditeOrani

"""
#Roi sınıfından türetilmiş nesneler
r1 = roi.Roi()
r1.roiHesapla()
#r2.roiHesapla()
"""

"""
#Nps sınıfından türetilmiş nesneler

n1 = nps.Nps(0,1,2,3,4,5,6,7,8,9,200)

#n1.tümPuanlarıGetir()

#n1.puanGetir(17)

n1.npsHesapla()

#n1.bargrafikOlustur()
"""

#Calisan sınıfından türeyilmiş nesneler
c1 = calisan.Calisan()       #Çalışan sınıfında c1 adlı nesne türetildi
c1.personelEkle()             #personel ekle komutu verildi
print(c1.calisanListesi)        #Sözlük formatında olan liste görüntülendi. id-isim
print(c1.adSoyad)


"""
#Musteri sınıfından türetilmiş nesneler
m1 = musteriMemnuniyet.Musteri() #Musteri sınıfından m1 nesnesi oluşturuldu
m1.puanVer() #Puan ver komutu verildi
"""

"""
#Borsa sınıfından türetilmiş nesneler
b1 = borsa.Borsa()          #Borsa sınıfından b1 nesnesi türetildi, parametrelerin
b1.hisseBasiKar()        #H
b1.fkHesapla()
b1.piyasaDegeri()
"""

"""
l1 = likiditeOrani.Likidite(100,10)
#l1.cariOran()
#l1.asitTestOran()
#l1.nakitOranı()
l1.stokBagimlilikOran()
"""










