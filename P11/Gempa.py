class Gempa:
    #atribut
    lokasi = ""
    skala = 0

    #konstruktor
    def __init__(self, lokasi="-", skala= 0):
        self.lokasi = lokasi
        self.skala = skala

    #method
    def dampak(self):
        if(self.skala <2):
            ket = 'Tidak Terasa'

        elif(self.skala >=2 and self.skala <4):
            ket = 'Bangunan Retak'

        elif(self.skala >=4 and self.skala <6):
            ket = 'Bangunan Roboh'

        else:
            ket='Berpotensi Tsunami'
        
        print('Telah terjadi gempa di', self.lokasi,
              'dengan skala ', self.skala, '  richter',
              'yang berdampak', ket
              )
        
#instansiasi  object
banten = Gempa()
banten.lokasi = "Banten"
banten.skala = 1.2
banten.dampak()

malang = Gempa('malang', 6.0)
malang.dampak()