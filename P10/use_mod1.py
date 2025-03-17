import myModul1
def main():
     while True:
            pilihan = str(input("Tentukan Pilihanmu(1: Luas Lingkaran, 2:Luas Persegi, 3:Luas Segitiga):"))
            if pilihan == '1':
               myModul1.LuasLingkaran()
            elif pilihan =='2':
               myModul1.LuasPersegi()
            elif pilihan =='3':
                myModul1.LuasSegitiga()
            else:
               print("Pilihan tidak tersedia")
main()
         