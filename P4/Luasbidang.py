print("----------Luas Bidang------------")
print("Luas Bidang")
print("Pilih Bidang:",
"\n1.Segitiga",
"\n2.Lingkaran",
"\n3.Persegi Panjang")
Pilihan =int (input("\nMasukkan Pilihan:"))
#percabangan
if(Pilihan == 1):
    alas = eval(input("Masukkan alas:"))
    tinggi = eval(input("Masukkan tinggi:"))

#Hitung Luas Segitiga
    hasil = 0.5 * alas * tinggi
    print(f"Hasil dari perhitungan luas segitiga adalah {hasil}")

#Lingkaran
elif(Pilihan == 2):
    jari2 = eval(input("Masukkan jari-jari:"))

#Hitung Luas Lingkaran
    luas = 3.14 * jari2 **2
    print(f"Hasil dari perhitungan luas lingkaran adalah {luas}")

#Persegi Panjang
elif(Pilihan == 3):
    panjang = eval(input("Masukkan panjang:"))
    lebar =  eval(input("Masukkan lebar:"))

#Hitung Luas Persegi Panjang
    luas = panjang * lebar
    print(f"Hasil dari perhitungan luas persegi panjang adalah {luas}")
else:
    print("Pilihan Tidak Tersedia")

print("\nProgram Selesai <3")

