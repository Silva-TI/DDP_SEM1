Topping_Seblak = ['Sosis', 'Baso', 'Jamur Enoki', 'Ceker']
print(Topping_Seblak[1])

del Topping_Seblak[3]
print(Topping_Seblak)
      
for toping in Topping_Seblak :
    print (toping)
#Tambahin Dumpling diantara Sosis dan Baso
Topping_Seblak.insert(1, 'Dumpling Ayam')
#Tambahin Toping di akhir list
Topping_Seblak.append('Makaroni')
print (Topping_Seblak)

#Topping_Baru = ['Kerupuk', 'Wagyu', 'Kwetiau']
#Topping_Seblak.append(Topping_Baru)
#print(Topping_Seblak)

print(Topping_Seblak[0:3])
print(Topping_Seblak[1:4])
