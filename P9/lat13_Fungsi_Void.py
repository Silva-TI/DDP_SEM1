#Membuat Function Void Define by User
def hitungUmur(thn_now):
    nama = input("Nama Anda: ")
    thn_lahir= int(input("Tahun Lahir: "))
    umur = thn_now - thn_lahir
    print("Mahasiiswa a.n %s yang lahir tahun %i saat ini berumur %2.f tahun" %(nama,thn_lahir,umur))

    #Panggil Fungsi
    hitungUmur(2024)    

