''' Быстрый чек-лист на каждый день
        git status       # Проверить изменения
        git pull        # Забрать обновления

        # ... Работа ...

        git add .       # Добавить изменения
        git commit -m "Update"
        git push        # Отправить на GitHub
'''
# ваше решение

dist = input("Введите расстояние до работы в километрах: ")
mil = 1.8
some_value = int(dist)
result = f"Расстояние до работы в милях: {some_value * mil}"
print(result)

