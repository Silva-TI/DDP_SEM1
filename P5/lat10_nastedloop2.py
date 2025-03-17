string = ""
bar = 1
bebas = int (input('masukan jumlah baris :'))
#Looping Bintang Menggunakan While
while bar <= bebas:
    col = bar
    while col > 0:
        string += "*"
        col -= 1
    string += "\n"
    bar += 1    
print(string)