def testString(kata):
    angka = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    simbol = ("!", "@", "#", "$", "%", "^", "&", "*", "+")
    hitungKata = len(kata.split())
    hitungSalah = 0
    while True:
        if any(char in angka for char in kata):
            hitungSalah = hitungSalah+1
            if any(char in simbol for char in kata):
                hitungSalah = hitungSalah+1
            total = hitungKata - hitungSalah
            print("Jumlah kata sebanyak: ", total,"/", hitungKata)
            break            
        else:
            print("Jumlah kata sebanyak: ", hitungKata,"/",hitungKata)
            break
                

kata = input("Masukkan kata disini : ")
testString(kata)
