import random

class Engelden_kacinma:
    def __init__(self, hak1=3, can1=100, sans=0):
        self.hak = hak1
        self.baslangic_can = can1
        self.can = can1
        self.sans = sans
        self.tur = 1
        self.serit = ["sol", "sağ"]

    def engel_uret(self):
        return random.choice(self.serit)

    def hasar_al(self, miktar=50):
        self.can -= miktar
        print(f"Çarptın! {miktar} canın azaldı. (Kalan can: {self.can})")

        if self.can <= 0:
            self.hak -= 1
            print(f"Canın bitti, 1 hak kaybettin. (Kalan hak: {self.hak})")

            if self.hak > 0:
                self.can = self.baslangic_can
                print(f"Yeni hakka geçtin, canın {self.can} oldu.")

    def tur_oyna(self):
        print(f"- Tur {self.tur} | Kalan Hak: {self.hak} | Mevcut Can: {self.can} | Şans: {self.sans} -")

        engel = self.engel_uret()
        secim = input("Hangi şerittesin (sol / sağ): ").strip().lower()

        print(f"Engel '{engel}' şeritte.")

        if secim == engel:
            self.hasar_al(50)
        else:
            print("Engelden kaçtın!")
            self.sans += 10

        print()
        self.tur += 1
    
    def baslat(self):
        print("--- Engelden Kaçma Oyunu ---")
        print(f"Kurallar: {self.hak} hakkın ve her hakta {self.can} canın var.\n")

        while self.hak > 0:
            self.tur_oyna()
        
        print(f"OYUN BİTTİ! Tüm haklarını kaybettin. Toplam {self.tur - 1} tur hayatta kaldın.")

if __name__ == "__main__":
    oyun = Engelden_kacinma(hak1=3, can1=100, sans=0)
    oyun.baslat()