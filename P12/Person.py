class Person:
    #atribut
    nama = ""
    gender = ""
    umur = 0

    def __init__(self, name, gender, age):
        self.nama = name
        self.gender= gender
        self.umur = age

    #method cetak
    def cetak(self):
        print("Nama \t\t:", self.nama,
              "\nJenis Kelamin \t:", self.gender,
              "\nUmur \t\t:", self.umur
              )

