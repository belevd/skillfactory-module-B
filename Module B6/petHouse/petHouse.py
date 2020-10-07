from Cat import Cat

cats = []
cat_1 = Cat('Барон', 'мальчик', 2)
cat_2 = Cat('Сэм', 'мальчик', 2)

cats.append(cat_1)
cats.append(cat_2)

for cat in cats:
    if cat.getSex() == 'мальчик':
        print(f'Этого котика зовут {cat.getName()}. Он мальчик. Ему {cat.getAge()} года')
    else:
        print(f'Эту кошечку зовут {cat.getName()}. Она девочка. Ей {cat.getAge()} года')