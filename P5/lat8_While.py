print('------------cetak bilangan 50 s/d 100------------')
awal = 50
akhir =  100
while (awal <= akhir):
    print('Bprintilangan', awal)
    awal += 1

print('------------cetak bilangan genap 100 s/d 50------------')
awal = 100
akhir =  50
while (awal >= akhir):
    if awal % 2 == 0:
        print ('Bil Genap', awal)
    awal -= 1