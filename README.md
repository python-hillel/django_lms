# django_lms

## Lesson 01
1. Создали новый проект - прототип **LMS**.
2. Создали приложение **students** и модель **Student**.
3. Добавили **vie**w - функцию для отображения студентов на основании параметров GET запроса.

## Lesson 02


## Lesson 03


## Lesson 04
- Базовый шаблон для всего проекта (root **templates** folder)
```python
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    }
]
```
- Создали шаблон для обновления студента и изменили view-функцию
- Создали шаблон и view-функцию для удаления студента
- Добавили обработку неверного запроса (**get_object_or_404**)
- Расширили маршрутизатор проекта
- Добавили имена маршрутам
> Добавили имя приложения в маршрутизатор приложения
- Заменили хард-код ссылки на динамически создаваемые
```python
from django.urls import reverse

print(reverse('list'))
```
```html
{% url 'students:list' %}
```
- Добавили новое приложение **core**
- Вынесли общие валидаторы и view-функцию **index** в новое приложение
- Добавили табличную разметку и стилевое оформление в шаблон **students/list.html**

## Lesson 05
- Подключили загрузку переменных окружения из файла **.env**
- Удалено поле **age** из модели **Student**
- Создали метод для динамического вычисления возраста
- Подключили **bootstrap5**
- Изменили базовый шаблон
- Добавили навигационную панель
- Добавили стили кнопкам и таблице
- Добавили иконку в панель меню
- Включили контент в контейнер
- Зафиксировали панель меню
- Добавили оформление формам (применили **crispy-forms**)
- Изменили формат отображения дат.
