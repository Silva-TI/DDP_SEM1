gender = ('laki-laki', 'Perempuan')
umur = ('0-10', '11-20', '21-30')

#Budi adalah murid smp dengan umur .. berjenis kelamin laki-laki 
print(f"Budi adalah seorang murid smp dengan umur {umur[1]} dan berjenis kelamin {gender[0]}")

#Mawar adalah seorang Mahasiswi dengan umur .. dan berjenis kelamin Perempuan 
print(f"Mawar adalah seorang Mahasiswi dengan umur {umur[2]} dan berjenis kelamin {gender[1]}")

#Menghitng jumlah item pada variable
print(f"Jumlah item pada variable gender ada {len(gender)} sedangkan item pada variable umur ada {len(umur)}")

#Nested Tuple
makanan= ('Mie Ayam', 'Karedok', 'Ayam Penyet', 'Pecel Lele')
miumanan =  ('Es Teh', 'Es Jeruk', 'Es Kelapa', 'Es Campur')
dessert = ('Es Krim', 'Pisang Goreng', 'Puding')

menu =(makanan,miumanan,dessert)

print(menu[1])
print(menu[2][1])
print(menu)

