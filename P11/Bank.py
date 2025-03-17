class Bank :
    #atribut / property
    norek = ''
    nama = ''
    saldo = 0
    jmlhNasabah = 0
    BANK = 'Bank Syariah Nurul Fikri'

    #method
    #konstruktor
    def __init__(self, no, nasabah, saldo):
        self.norek = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jmlhNasabah += 1

    def cetak(self):
        print(Bank.BANK,
            '\n==============================='
            '\nNo. Rekening\t: ', self.norek,
            '\nNama Nasabah\t: ', self.nama,
            '\nSaldo\t\t:  Rp.', format(self.saldo, ','),
            '\n-------------------------------'
            )
    #method nambah saldo
    def nabung(self, nominal):
        self.saldo += nominal
        print ("\nNabung Suskes!, saldo Anda saat ini:  ", format (self.saldo, ','))
               
     #method tarik saldo
    def tarik(self, nominal):
        self.saldo -= nominal          
        print ("\nTarik Saldo Suskes!, saldo Anda saat ini:  ", format (self.saldo, ','))
                      
               
               
#instansi object
silva = Bank('14040', 'Silva ND', 150000)
yujin = Bank ('20100', 'Han Yujin', 200000)
Haechan = Bank ('80102', 'lee Donghyuk', 400000)
Chenle = Bank ('45632', 'Zhong Chenle', 1000000)

#cetak
silva.cetak()
yujin.cetak()
Haechan.cetak()
Chenle.cetak()

#silva.cetak()
print (silva.saldo)
yujin.nabung(100000)                                                               
Chenle.tarik(200000)

