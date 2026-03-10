is_Kabisat = True
is_notKabisat = False
tahun = int(input("Masukkan tahun: "))

def kabisat(tahun, is_Kabisat, is_notKabisat):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        print(is_Kabisat)
    else:
        print(is_notKabisat)

kabisat(tahun, is_Kabisat, is_notKabisat)