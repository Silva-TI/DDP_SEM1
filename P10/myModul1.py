def LuasLingkaran():
    jari = float(input("Masukkan Jari Jari Lingkaran: "))
    hitung = 3.14 *(jari **2)
    print (f"Luas lingkaran dengan jari jari {jari}cm adalah{hitung}")

def LuasPersegi():
     sisi = float(input("Masukkan sisi persegi:"))
     hitung = sisi * sisi
     print(f"Luas persegi dengan sisi{sisi})cm adalah {hitung}")

def LuasSegitiga():
     Alas = float(input("Masukkan nilai alas:")) 
     Tinggi = float(input("Masukkan nilai Tinggi:"))  
     hitung = Alas * Tinggi * 0.5
     print(f"Luas Segitiga dengan alas{Alas}cm dan tinggi {Tinggi}cm adalah {hitung}" )