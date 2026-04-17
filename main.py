sozlar = ["olma", "gilos", "olma", "shaftoli", "gilos", "gilos"]
chastota = [sozlar.count(i) for i in set(sozlar)]

for i in range(len(set(sozlar))):
    print(list(set(sozlar))[i], ":", chastota[i])
