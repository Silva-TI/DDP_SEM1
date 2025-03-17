pegawai = input("Nama\t:")
agama = input("Agama\t:")
divisi = input("Divisi\t:")
jabatan = input("Jabatan\t:")

#Set Gaji
if jabatan == "Staff":
    gaji = 4000000
elif jabatan == "Kabang":
    gaji = 7000000
elif jabatan == "Manager":
    gaji = 10000000
else:
    gaji = 0

# Tunjangan Jabatan
tunjab = 0.2 * gaji

# Gaji Kotor
gaji_kotor = gaji + tunjab

# Zakat
zakat = 0
if agama == "Islam" and gaji_kotor >= 7000000:
    zakat = 0.025 * gaji_kotor
else:
    zakat = 0

# Gaji Bersih
gaji_bersih = gaji_kotor - zakat

# Output
print(f"Nama\t: {pegawai}")
print(f"Agama\t: {agama}")
print(f"Divisi\t: {divisi}")
print(f"Jabatan\t: {jabatan}")
print(f"Gaji pokok\t: {gaji}")
print(f"Tunjangan Jabatan\t: {tunjab}")
print(f"Gaji Kotor\t: {gaji_kotor}")
print(f"Zakat\t\t: {zakat}")
print(f"Gaji Bersih\t: {gaji_bersih}")

#Cetak
print("\nTerimakasih Telah Menggunakan Layanan Kami <3")