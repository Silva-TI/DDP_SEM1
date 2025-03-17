nilai = {'Yujin':89, 'Hanbin':100, 'Gyuvin':59, 'Matthew':95}

#Akses nilai dictionary
print(nilai['Gyuvin'])

#Tambah nilai dictionary
nilai['Ricky'] = 100

#Looping key
for i in nilai.keys():
    kalimat = f'Nilai {i} adalah {nilai[i]}'
    print(kalimat)

#Ubah nilai Hanbin menjadi 87
nilai['Hanbin'] = 87

#Hapus nilai dictionary
nilai.pop('Ricky')

print("\n=============== Cetak Items ===============")

#Looping Items (key dan value)
for nama, score in nilai.items():
    kalimat = f'Nilai {nama} adalah {score}'
    print(kalimat)
