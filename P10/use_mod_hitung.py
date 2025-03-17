print("----------Gunakan Modul Secara Langsung----------")
import mod_hitung
mod_hitung.tambah(2,3)
mod_hitung.tambah(234,17)
mod_hitung.kali(2,7)
mod_hitung.pangkat(7,4)
mod_hitung.kurang(8,3)
mod_hitung.bagi(8,2)

print("----------Gunakan Modul dialiaskan----------")
import mod_hitung as hitung
hitung.tambah(2,3)
hitung.tambah(234,17)
hitung.kali(2,7)
hitung.pangkat(7,4)
hitung.kurang(8,3)
hitung.bagi(8,2)

print("----------Gunakan Modul Sebagian Fungsi----------")
from mod_hitung import kali,bagi,pangkat
kali(2,7)
pangkat(7,4)
bagi(8,2)

print("----------Gunakan Modul Semua Fungsi----------")
from mod_hitung import *
tambah(2,3)
tambah(234,17)
kali(2,7)
pangkat(7,4)
kurang(8,3)
bagi(8,2)

print("----------Gunakan Modul, Fungsi dialiaskan----------")
from mod_hitung import kali as k, bagi as b, pangkat as p
k(2,7)
p(7,4)
b(8,2)