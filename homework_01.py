"""Fix syntax errors and resolve tasks."""

# task 01 == Виправте синтаксичні помилки
print('Hello', end=' ')
print('world!')

# task 02 == Виправте синтаксичні помилки
hello = 'Hello'
world = 'world'
if True:
    print(f'{hello} {world}!')

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in 'Hello world!':
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
сторона_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = storona_1 + storona_2 + сторона_3 + storona_4
print(f'Figure perimeter is {perimeter} meters.')

# Resolve math exercises from 2nd class study book.
# Задачі 07 -10:
# Переведіть задачі з книги "Математика, 2 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в другому класі

# task 07
# У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?

apples = 4
pears = apples + 5
plums = apples - 2
trees_in_garden = apples + pears + plums
print(f'A total of {trees_in_garden} trees were planted in the garden')

# task 08

# До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?

zero = 0
temp_before = zero + 5
temp_after = temp_before - 10
temp_evening = temp_after + 4
print(f'Temperature will be {temp_evening} degrees in evening.')
# task 09

# Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
# Скількі сьогодні дітей у театральному гуртку?

boys = 24
girls = boys / 2
boys_today = boys - 1
girls_today = girls - 2
children_today = boys_today + girls_today
print(f'The are {children_today} children in theater club today.')

# task 10
# Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

first_book = 8
second_book = 8 + 2
third_book = (first_book + second_book) / 2
all_books = first_book + second_book + third_book
print(f'First book cost: {first_book} grn.')
print(f'Second book cost: {second_book} grn.')
print(f'Third book cost: {third_book} grn.')
print(f'All books will cost: {all_books} grn.')
