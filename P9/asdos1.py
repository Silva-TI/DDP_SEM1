def hitungGaji():
    nama = input("Nama :") 
    jabatan = input("Jabatan Anda(Manager/Asisten Manager/Supervisor/Staff) :")
    agama = input("Agama Anda:")
    status = input("Status Pernikahan:")

    def gapok():
    
        match jabatan:
            case "Manager":
                return 15000000
            
            case "Asisten Manager":
                return 10000000
            
            case "Supervisor":
                return 7000000
            
            case "Staff":
                return 4000000
            
            case _:
                return 0
            
    tunjab = 0.3 * gapok()
    BPJS = 0.1 * gapok()

    def tunkel(s):
        match s:
            case "ya"|"iya"|"Iya"|"Ya"|"Sudah":
                return 0.1 * gapok ()
            case _:
                return 0
    gator = gapok() + tunjab + BPJS + tunkel(status)
   

    def zakat ():
        return (0, 0.025 * gator) [agama =='islam' and gator >= 7000000]
    
    
    gaber = gator - zakat()
    print('=============Perhitungan Gaji Pegawai=============')
    print("Nama Pegawai\t\t:", nama,
            "\nJabatan\t\t\t:", jabatan,
            "\nAgama\t\t\t:", agama,
            "\nStatus Pernikahan\t:", status,
            "\nGaji Pokok\t\t:", gapok(),
            "\nTujnangan Jabatan\t:", tunjab,
            "\nTujangan Keluarga\t:", tunkel(status),
            "\nBPJS\t\t\t:", BPJS,
            "\nZakat Profesi\t\t:", zakat(),
            "\nGaji Bersih\t\t:", gaber, )            
hitungGaji()