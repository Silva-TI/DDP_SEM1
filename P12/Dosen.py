#import class person
from Person import * 

class Dosen(Person):
    #atribut
    gelar =""
    jabatan ="Dosen"
    __gaji= 0 #protected / private atribut

    def __init__(self,name, gender, age,  gelar, jabatan = "Dosen"):
         super().__init__(name, gender, age)
         self.gelar = gelar 
         self.jabatan = jabatan

    #method
    def setGaji(self, nominal):
        self.__gaji = nominal

    def cetak(self):
        super().cetak()
        print("gaji \t\t:", self.__gaji,
              "\njabatan \t:", self.jabatan,
              "\ngelar \t\t:", self.gelar)
    

dosen = Dosen('Yujin', 'Laki laki', 18, "S.Kom, M.T" )
dosen.setGaji(5500000)
dosen.cetak()