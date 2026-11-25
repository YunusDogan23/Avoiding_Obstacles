import random


class Engelden_kacinma:
    def __init__(self, hak1=3, can1=100, puan=0):
        self.hak = hak1
        self.baslangic_can = can1
        self.can = can1
        self.puan = puan
        self.tur = 1
        self.serit = ["sol", "sağ"]
        self.araba = "sol"  # oyuna sol şeritten başlıyoruz

    def engel_uret(self):
        return random.choice(self.serit)

    def yol_ciz(self, engel=None):
        # A = araba, X = engel. ikisi aynı yerdeyse * çiziyor
        ust = ["     ", "     "]
        alt = ["     ", "     "]

        araba_i = self.serit.index(self.araba)
        if engel is not None:
            engel_i = self.serit.index(engel)
            if engel_i == araba_i:
                ust[engel_i] = "  *  "
            else:
                ust[engel_i] = "  X  "

        alt[araba_i] = "  A  "

        print("  sol   sağ")
        print("|" + ust[0] + "|" + ust[1] + "|")
        print("|" + alt[0] + "|" + alt[1] + "|")

    def serit_sec(self):
        while True:
            secim = input("Hangi şeride gideceksin? (sol / sağ, boş bırakırsan aynı şeritte kalırsın): ").strip().lower()

            if secim == "":
                print(f"{self.araba} şeritte kalmaya devam ediyorsun.")
                return
            if secim == "sag":  # türkçe karakter olmadan yazınca da kabul etsin
                secim = "sağ"

            if secim in self.serit:
                if secim != self.araba:
                    print(f"{self.araba} şeritten {secim} şeride geçtin.")
                self.araba = secim
                return

            # eskiden yanlış yazınca engelden kaçmış sayılıyordu, artık tekrar soruyor
            print("Öyle bir şerit yok, sol ya da sağ yaz.")

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
        print(f"- Tur {self.tur} | Hak: {self.hak} | Can: {self.can} | Puan: {self.puan} -")
        print(f"Araban şu an {self.araba} şeritte.")
        self.yol_ciz()

        engel = self.engel_uret()
        # print("engel:", engel)  # test ederken açıyordum
        self.serit_sec()

        print(f"Engel {engel} şeritte çıktı!")
        self.yol_ciz(engel)

        if self.araba == engel:
            self.hasar_al(50)
        else:
            print("Kıl payı kurtardın, +10 puan.")
            self.puan += 10

        print()
        self.tur += 1

    def baslat(self):
        print("--- Engelden Kaçma Oyunu ---")
        print(f"Kurallar: {self.hak} hakkın ve her hakta {self.can} canın var.")
        print("Her turda ya şerit değiştir ya da olduğun yerde kal, engel rastgele bir şeritte çıkacak.\n")

        try:
            while self.hak > 0:
                self.tur_oyna()
        except (KeyboardInterrupt, EOFError):
            print("\nOyundan çıktın.")
            return

        print(f"OYUN BİTTİ! Tüm haklarını kaybettin. {self.tur - 1} tur dayandın, puanın: {self.puan}")


if __name__ == "__main__":
    oyun = Engelden_kacinma()
    oyun.baslat()
