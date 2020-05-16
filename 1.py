def triangle(A):
    if A < 0:
        print("Bilangan Tidak Boleh Negatif")
    else :
        for baris in range(0, A):
            for kolom in range(0, baris+1):
                print("# ", end="")
            print("\r")
A = int(input("Masukkan bilangan positif: "))
triangle(A)
