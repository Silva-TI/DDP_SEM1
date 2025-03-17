list_menu = [
    ['Mie Ayam', 'Karedok', 'Ayam Penyet', 'Pecel Lele'],
    ['Es Teh', 'Es Jeruk', 'Es Kelapa', 'Es Campur'],
    ['Es Krim', 'Pisang Goreng', 'Puding']
]

print(f"Yujin makan {list_menu[0][2]} dan minum {list_menu[1][0]} lalu ditutup dengan {list_menu[2][2]}")
print(f"Mawar makan {list_menu[0][1]} dan minum {list_menu[1][1]} lalu ditutup dengan {list_menu[2][0]}")

for menu in list_menu :
    for makanminum in menu :
        print (makanminum) #semua list dipecah