# primer 11.111
# mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# for i in mass:
#    mass2 = []
#    if i % 2 == 0:
#        mass2.append(mass[i])
# print(mass[len(mass) - 1])

# primer 11.112
# mass = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f'Первый элемент списка: {mass[0]}\n'
#      f'Последний элемент списка: {mass[len(mass) - 1]}\n'
#      f'Псоледний элемент больше первого элемента списка на: {mass[len(mass) - 1] - mass[0]}'
#      f'Индекс первого элемента: 0\nИндекс последнего элемента: {len(mass) - 1}')

# primer 11.113
# mass = list(range(1, 101))
# mass.sort()
# print(f"В самай толстой книге: {mass[len(mass) - 1]} страниц!")

# primer 11.114
# mass = [110, 1314, 255454, 446552, 676, 23, 1243124, 1919, 233466, 34524, 1241415]
# mass.sort()
# print(f'Самая дорогая машина стоит: {mass[len(mass) - 1]}')

# primer 11.115
# mass = [343, 75475, 1212, 100, 50, 150, 250, 450, 670, 346]
# mass.sort()
# print(f'Килограм самых дешевых конфет стоит: {mass[0]}')