List_Makanan = [

    ['Bakwan', 'Combro', 'Misro', 'Tahu'],
    ['Sop Iga', 'Sop Buntut', 'Sop Ayam', 'Soto Mie'],
    ['Naik Uduk', 'Nasi Goreng', 'Nasi Rames', 'Nasi Padang'],
]

#Cetak Element
print('----------Cetak Makanan Tetentu----------')
print (List_Makanan[0][3])  #tahu
print (List_Makanan[1][3])  #Sotot Mie
print (List_Makanan[2][0])  #Nasi Uduk
print ('-----------Cetak Seluruh Makanan----------')
#Inateed Loop
for menu in List_Makanan:
    for food in menu :
        print(food)