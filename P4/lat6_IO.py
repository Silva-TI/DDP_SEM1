nama = input("Nama Mahasiswa\t:")
bb = float(input("Berat Badan\t:"))
tb = float(input("Tinggi Badan\t:"))
imt = bb/(pow (tb,2))
#kondisi fisik
if imt < 18.5: fisik = "kurus"
elif imt >= 18.5 and imt < 25 : fisik = "Normal"
elif imt >= 25 and imt < 30 : fisik = "Overweight"
elif imt <= 30 : fisik = "Obesitas"
else: fisik = ""
#cetak
print("Nama Mahasiswa\t: %s"
      "\nBerat Badan\t: %.2f"
      "\nTinggi Badan\t: %.2f"
      "\nIMT\t\t: %.2f"
      %(nama,bb,tb,imt)
       )