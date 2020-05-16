def hitungUlang(kalimat):
    huruf="abcdefghijklmnopqrstuvwxyz"
    for char in huruf:
        jumlah = kalimat.count(char)
        if jumlah > 1:
            print(char,":", jumlah)

kalimat = input("Masukkan kalimat disini: ")
hitungUlang(kalimat)
