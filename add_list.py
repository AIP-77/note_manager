# Запрашиваем у пользователя информацию
username = input('Введите имя пользователя: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки ( например-"ожидает", "готово", "в работе"): ')
created_date = input('Введите дату создания заметки в формате "день-месяц-год": ')
issue_date = input('Введите дату истечения заметки в формате "день-месяц-год": ')

# Запрашиваем несколько заголовков и добавляем их в список
title1 = input('Введите первый заголовок заметки: ')
title2 = input('Введите второй заголовок заметки: ')
title3 = input('Введите третий заголовок заметки: ')
titles = [title1, title2, title3]

# Выводим все данные заметки
print('\nВы ввели следующие данные:')
print('Имя пользователя: ', username)
print('Заголовки заметки: ', titles)
print('Описание заметки: ', content)
print('Статус заметки: ', status)
print('Дата создания заметки: ', created_date[:5])
print('Дата истечения заметки:  ', issue_date[:5])
