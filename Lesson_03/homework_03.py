"""Solutions for homework_03 tasks."""

# alice_in_wonderland = '"Would you tell me, please, which way
#            I ought to go from here?"\n
#           "That depends a good deal on where you want to get to,"
#            said the Cat.\n"I don't much care where ——" said Alice.\n
#           "Then it doesn't matter which way you go," said the Cat.\n
#           "—— so long as I get somewhere," Alice added as an explanation.\n
#           "Oh, you're sure to do that," said the Cat,
#           "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так,
#            щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

# Splitting variable alice_in_wonderland,
# so that it occupies several physical lines.
# Main option without escape character.
alice_in_wonderland = '''
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''

# Additional option with escape character.
alice_in_wonderland2 = ('\"Would you tell me, please, '
                        'which way I ought to go from here?\" \n'
                        '\"That depends a good deal on where '
                        'you want to get to,\" said the Cat.\n'
                        '\"I don\'t much care where ——\" said Alice.\n'
                        '\"Then it doesn\'t matter which way you go,\" '
                        'said the Cat.\n'
                        '\"—— so long as I get somewhere,\" '
                        'Alice added as an explanation.\n'
                        '\"Oh, you\'re sure to do that,\" said the Cat, '
                        '\"if you only walk long enough.\"')

print(alice_in_wonderland, end='\n\n')   # Print variable alice_in_wonderland2.
print(alice_in_wonderland2, end='\n\n')  # Print variable alice_in_wonderland.
# Compare two variables values.
print(alice_in_wonderland == alice_in_wonderland2)
# Compare unique id() value in memory.
print(alice_in_wonderland is alice_in_wonderland2)
print(id(alice_in_wonderland))
print(id(alice_in_wonderland2), end='\n\n')

# Find and display all single quotation marks (') in the text
quotation_marks = alice_in_wonderland.count("'")
print(f"Found {quotation_marks} single quotation marks (') in the text")

# Задачі 04 -10:
# Переведіть задачі з книги "Математика, 5 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в п'ятому класі

# task 04

# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?

# Task 04 solution.
black_sea = 436_402   # Black sea square 436'402 sqr.km.
azov_sea = 37_800     # Azov sea square 37'800 sqr.km.
overall = black_sea + azov_sea  # Overall square of Black and Azov seas.
print(f'Overall square of Black and Azov seas equals: {overall} sqr.km.')

# task 05

# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.

# Task 05 solution.
overall_goods = 375_291               # Overall goods in all supermarkets.
first_second = 250_449                # Goods in first and second supermarkets.
second_third = 222_950                # Goods in second and third supermarkets.
first = overall_goods - second_third  # First supermarket goods.
second = first_second - first         # Second supermarket goods.
third = second_third - second         # Third supermarket goods.
print(f'First supermarket has {first} goods.')
print(f'Second supermarket has {second} goods.')
print(f'Third supermarket has {third} goods.')

# task 06

# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.

# Task 06 solution.
months = 18                                   # Period: 1.5 year = 18 months.
cost_per_month = 1179                         # Computer cost per month.
computer_value = cost_per_month * months      # Overall computer value.
print(f'Overall computer value: {computer_value} grn.')

# task 07

# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9

# Task 07 solution.
a = 8019 % 8                             # Modulus a) example 8019 : 8
b = 9907 % 9                             # Modulus b) example 9907 : 9
c = 2789 % 5                             # Modulus c) example 2789 : 5
d = 7248 % 6                             # Modulus d) example 7248 : 6
e = 7128 % 5                             # Modulus e) example 7128 : 5
f = 19224 % 9                            # Modulus f) example 19224 : 9
print(f'a) = {a}, b) = {b}, c) = {c}, '
      f'd) = {d}, e) = {e}, f) = {f}')   # Printing results.

# task 08

# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн

# Task 08 solution.
big_pizza = 4 * 274      # Big pizza total: 3 items * 274
small_pizza = 2 * 218    # Small pizza total: 2 items * 218
juice = 4 * 35           # Juice total: 3 pack * 35
cake = 1 * 350           # Cake total: 1 item * 350
water = 3 * 21           # Water total: 3 bottles * 21
overall_bill = big_pizza + small_pizza + juice + cake + water
print(f'Overall order bill will be: {overall_bill} grn.')

# task 09

# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?

# Task 09 solution.
overall_photos = 232                                 # Overall photos.
photos_per_page = 8                                  # Photos per page.
pages = overall_photos // photos_per_page            # Pages in album.
print(f'Album should have {pages} pages.')

# task 10

# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?

# Task 10 solution.
distance = 1600                     # Distance from Kharkiv to Budapest.
gas_per_km = 9                      # Gas litre needed per 100 km.
tank = 48                           # Tank capacity liters.
gas = distance // 100 * gas_per_km  # Overall gas for journey.
stops = gas // tank                 # Gas station stops.
print(f'1) Overall {gas} litres will be spent for journey.\n'
      f'2) Family will stops minimum {stops} times in gas station.')
