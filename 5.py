def cariPasangan(seq):
    seen = {}
    dupes = []
    for x in seq:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] +=1
    for i in range(len(dupes)):
        print("[",dupes[i],",",dupes[i],"]")

a = [5, 13, 7, 5, 9, 20, 9, 5, 14]
cariPasangan(a)
