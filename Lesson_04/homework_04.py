"""Solutions for homework_04 tasks."""
import logging

_log = logging.getLogger('Main')
log_formatter = logging.Formatter('%(asctime)s [%(levelname)s]  %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
_log.addHandler(console_handler)
_log.setLevel(logging.DEBUG)

adventures_of_tom_sayer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by,
dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out,
Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sayer у завданнях 1-3
# task 01 ==
# Дані у строці adventures_of_tom_sayer
# розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")
# Replacing "\n" with spaces " ".
new_adventures_of_tom_sayer = adventures_of_tom_sayer.replace('\n', ' ')
_log.info(new_adventures_of_tom_sayer)

# task 02 ==
# Замініть .... на пробіл
# Replacing "...." with spaces " ".
new_adventures_of_tom_sayer = new_adventures_of_tom_sayer.replace('....', ' ')
_log.info(new_adventures_of_tom_sayer)

# Option 2 for task 01 and task 02
# Create a translation table where "\n" = " " and  "...." = null
mapping_table = adventures_of_tom_sayer.maketrans('\n', ' ', '....')
# Apply the specified translations to the input string.
tom_sayer = adventures_of_tom_sayer.translate(mapping_table)
_log.info(tom_sayer)

# task 03 ==
# Зробіть так, щоб у тексті було не більше одного пробілу між словами.
# Removing additional spaces from the text.
new_adventures_of_tom_sayer = ' '.join(new_adventures_of_tom_sayer.split())
_log.info(new_adventures_of_tom_sayer)

# task 04
# Виведіть, скількі разів у тексті зустрічається літера "h"
# Count 'h' letter in new_adventures_of_tom_sayer variable and display result.
letter_h = new_adventures_of_tom_sayer.count('h')
_log.info('Letter "h" is found %s times in the text.', letter_h)

# task 05
# Виведіть, скільки слів у тексті починається з Великої літери?
# Replacing " with empty spaces to prevent including " in words.
# Creating list of words from the string with split function.
words = new_adventures_of_tom_sayer.replace('"', '').split()
# Creating new list of words with capitalized letter.
# Calculate quantity of words with capitalized letter with function len().
uppercase_words = len([word for word in words if word.istitle()])
_log.info('There are %s title letter words in the text.', uppercase_words)

# task 06
# Виведіть позицію, на якій слово Tom зустрічається вдруге
# Find first position of word 'Tom' in the text
first_position = new_adventures_of_tom_sayer.find('Tom')
# Find and display second position of word 'Tom' in the text.
second_position = new_adventures_of_tom_sayer.find('Tom', first_position+1)
output = (f'The word "Tom" is located in {second_position} position'
          f' for the second time in the text.')
_log.info(output)

# task 07
# Розділіть змінну new_adventures_of_tom_sayer по кінцю речення.
# Збережіть результат у змінній adventures_of_tom_sayer_sentences
# Splitting variable new_adventures_of_tom_sayer by sentence end.
adventures_of_tom_sayer_sentences = new_adventures_of_tom_sayer.split('. ')
_log.info(adventures_of_tom_sayer_sentences)
# Calculating quantity of sentences in the adventures_of_tom_sayer_sentences.
sentences = f'There are {len(adventures_of_tom_sayer_sentences)} sentences.'
_log.info(sentences)

# task 08
# Виведіть четверте речення з adventures_of_tom_sayer_sentences.
# Перетворіть рядок у нижній регістр.
_log.info(adventures_of_tom_sayer_sentences[3])  # Display forth sentence.
# Modifying sentence where all word are lower  case.
sentence_lower = adventures_of_tom_sayer_sentences[3].lower()
_log.info(sentence_lower)

# task 09
# Перевірте чи починається якесь речення з "By the time".
# Check if any sentence in list adventures_of_tom_sayer_sentences
# starts with 'By the time'.
# Result: True or False.
# Also we need to know exactly sentence quantity in the ist.
sentence1 = adventures_of_tom_sayer_sentences[0].startswith('By the time')
sentence2 = adventures_of_tom_sayer_sentences[1].startswith('By the time')
sentence3 = adventures_of_tom_sayer_sentences[2].startswith('By the time')
sentence4 = adventures_of_tom_sayer_sentences[3].startswith('By the time')
sentence5 = adventures_of_tom_sayer_sentences[4].startswith('By the time')

# Option to find and display which sentence begins with 'By the time'
# in the list adventures_of_tom_sayer_sentences.
# If we don't exactly sentences in list and we want to display those sentence
# which begins with 'By the time', this is best option.
_log.info([sentence for sentence in adventures_of_tom_sayer_sentences if
           sentence.startswith('By the time')])

# task 10
# Виведіть кількість слів останнього
# речення з adventures_of_tom_sayer_sentences.
# Display list adventures_of_tom_sayer_sentences last sentence words quantity.
words_quantity = len(adventures_of_tom_sayer_sentences[-1].split())
_log.info('Last sentence has %s words.', words_quantity)
