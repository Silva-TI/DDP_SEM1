#Belajar Looping For
print('----------cetak angka 1 s/d 15-----------')
angka = 15
for no in range(angka):
    #no = no + 1
    no += 1
    print('angka', no)


print('----------cetak angka 5 s/d 25-----------')
awal = 5
akhir = 25
step = 2
for no in range(awal,akhir,step):
    no += 1
    print('angka', no)

    print('----------cetak bilangan ganjil-----------')
awal = 5
akhir = 25
step = 2
for no in range(awal,akhir,step):
    if (no % 2 == 1):
    #bil ganjil
     no += 2
    print('angka', no)
   

