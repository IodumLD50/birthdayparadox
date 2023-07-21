'''Имитационное моделирование парадокса дней рождения.
Изучаем неожиданные вероятности из "Парадокса дней рождения".'''

import datetime, random





def qetBirthdays(numberOfBirthdays):
    # Bозвращаем список объектов дат для случайных дней рождения.
    birthdays = []
    for i in range(numberOfBirthdays):
        # Год в нашем имитационном моделировании роли не играет, лишь бы в объектах дней рождения он был одинаков.
        startOfYear = datetime.date(2001, 1, 1)
        # Получаем случайный день года:
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def qetMatch(birthdays):
    # Возвращаем объект даты дня рождения, встречающегося несколько раз в списке дня рождения.
    if len(birthdays) == len(set(birthdays)):
        return None # Все днирождения различны 
    # Сравниваем все дни рождения друг с другом попарно:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA # Возвращаем найденое соответствия.
            



# Отражаем вводную информацию:
print('Имитационное моделирование парадокса дней рождения. Изучаем неожиданные вероятности из Парадокса дней рождения')            
# Создаём кортеж создание месяцев по порядку:
MONTHS = ('январь', 'февраль', 'март', 'май', 'апрель', 'июнь',
          'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь')

while True: # Запрашиваем пока пользователь не введёт допустимое значение.
    print('Сколько дней рождения нужно сгенерировать? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # Пользователь ввел допустимое значение.
    
print()

# Генирируем и отображаем дни рождения:
print(f'{numBDays} дней рождений сгенерированных случайным образом: ')
birthdays = qetBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Выводим запятую для каждого дня рождения после первого.
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print('\n')

# Выясним, встречаются ли да совпадающих дня рождения.
match = qetMatch(birthdays)

# Отображаем результаты:
print('В этом симуляторе, ', end='')        
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('у нескольких людей день рождения', dateText)
else:
    print('нет повторяющихся дней рождений.')      
print()
   
# Производим 100 000 операций имитационного моделирования:
print('Cгенерировать', numBDays, 'случайных дней рождений 100 000 раз...')  
input('Нажмите Enter, чтобы начать...')    

print('Давайте проведем еще 100 000 симуляций')
simMatch = 0 # Число операций моделирования с совпадающими днями рождения.
for i in range(100000):
     # Отображаем сообщение о ходе выполнения каждые 10 000 операций:
    if i % 10000 == 0:
         print(i, 'генераций проведено...')
    birthdays = qetBirthdays(numBDays)
    
    if qetMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100000 генераций проведено...')

# Отображаем результаты имитационного моделирования:
probability = round(simMatch / 100_000 * 100, 2)
print('Из 100 000 симуляций', numBDays, 'совпадающий день рождения в этой группе', simMatch, 'раз')
print('Это значит что у', probability, '% людей совпадают дени рождения в этих группах.')
print('Это, вероятно, больше, чем вы думаете!')