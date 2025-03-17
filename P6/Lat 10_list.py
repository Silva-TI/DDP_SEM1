#Membuat Stryktur Data List Baru
ar_buah = ['Pepaya', 'Mangga', 'Pisang', 'Jambu', 'Belimbing']
#Ganti Buah PisangDengan Apel
ar_buah[2] = 'Apel'
#Menghapus Buah Belimbing
del ar_buah[4]

print('buah index0', ar_buah[0])
print('buah index0', ar_buah[0])

#cetak
for buah in ar_buah:
    print('buah', buah)
#Tambah Element
ar_buah.insert(2,'Naga')
ar_buah.append('Jeruk')
ar_buah.append('Salak')
ar_buah.append('Melon')
ar_buah.append('Manggis')

print ('----------cetak all element----------')
for buah in ar_buah:
    print('buah', buah)

print ('-------------Potong Element------------')
print ('buah', ar_buah[3:6])

