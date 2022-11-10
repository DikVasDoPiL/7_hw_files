# Задача 2 - Получить словарь из ингредиентов и их количества для заданных блюд
cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ],
    'Фахитос': [
        {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'г'},
        {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for i in dishes:
        if i in cook_book:
            for j in cook_book[i]:
                if j['ingredient_name'] not in result:
                    result[j['ingredient_name']] = {'measure': j['measure'],
                                                    'quantity': j['quantity']*person_count}
                else:
                    result[j['ingredient_name']
                           ]['quantity'] += j['quantity']*person_count
    return result


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

for i in shop_list.keys():
    print(i, ':', end=' ')
    print(shop_list[i], sep='\n')
