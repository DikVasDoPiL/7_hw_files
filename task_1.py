# Задача 1 - получить словарь из файла
def cook_read(filename):
    '''Читает файл и возвращает представление в виде словаря'''
    with open(filename, 'r', encoding='utf8') as a:
        f = [i.strip()
            for i in a.readlines()]
    count = 1
    cook_book = {}
    dict_keys = ['ingredient_name', 'quantity', 'measure']
    while count <= len(f):
        item = f[count-1].strip()
        cook_book[item] = []
        for _ in range(int(f[count])):
            count += 1
            ing_name, ing_quantity, ing_measure = [
                i.strip() for i in f[count].split('|')]
            values = [ing_name, int(ing_quantity), ing_measure]
            cook_book[item] += [{x: y for x,
                                 y in zip(dict_keys, values)}]
        count += 3

    return cook_book


cook_book = cook_read('recipes.txt')

for i in cook_book.keys():
    print(i, ':')
    print(*cook_book[i], sep='\n')

