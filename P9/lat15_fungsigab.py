def infoSuhu():
         lokasi = input ("Lokasi: ")
         suhu = float (input("Suhu: "))
         def status():
                 if suhu < 0: kondisi ="Beku"
                 elif suhu >= 0 and suhu <= 15 : kondisi ="Dingin"
                 elif suhu >= 15 and suhu <= 25 : kondisi ="Sejuk"
                 elif suhu >= 25 and suhu <= 30 : kondisi ="Biasa"
                 else : kondisi ="Panas"
                 return kondisi
         print ('..........Informasi Suhu..........',
            '\nLokasi\t:',lokasi,
            '\nSuhu\t:',suhu,
            '\nkondisi\t:',status() ) 
                 
infoSuhu()
         
