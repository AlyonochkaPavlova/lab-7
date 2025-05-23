weekdays = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
count_weekends = int(input("Сколько выходных дней хотите иметь на неделе? "))
work_days = weekdays[:-count_weekends]
weekend_days = weekdays[-count_weekends:]
print("\nВаши выходные дни:", ', '.join(weekend_days))
print("Ваши рабочие дни:", ', '.join(work_days))
