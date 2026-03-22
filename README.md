
REST API(хотелось бы grpc) для управления сетью ресторанов и их меню. Проект выполнен на базе Django REST Framework.
Технические требования

    Python 3.10+

    Django 5.x / 6.x

    Django REST Framework

    SQLite (Database)

Установка и запуск

    Развернуть виртуальное окружение:
    Bash

    python -m venv .venv
    source .venv/bin/activate

    Установить зависимости:
    Bash

    pip install django djangorestframework

    Применить миграции базы данных:
    Bash

    python manage.py makemigrations api
    python manage.py migrate

    Запустить локальный сервер:
    Bash

    python manage.py runserver


## Запуск через Docker
1. Собрать образ: `docker build -t pizza-api .`
2. Запустить контейнер: `docker run -p 8000:8000 pizza-api`

Список эндпоинтов
Базовый CRUD (api/)

    GET, POST /api/restaurants/ — Управление ресторанами.

    GET, POST, PUT, DELETE /api/pizzas/ — Управление меню пицц.

    GET, POST /api/chefs/ — Управление данными шеф-поваров.

    GET /api/ingredients/ — Просмотр доступных ингредиентов.

    GET, POST /api/reviews/ — Работа с отзывами.

Специализированные эндпоинты

    GET /api/restaurants/{id}/menu/ — Получение полного списка пицц конкретного ресторана с детализацией ингредиентов.

Валидация и особенности

    Reviews: Поле rating ограничено диапазоном от 1 до 5 включительно через MinValueValidator и MaxValueValidator.

    Database: Использование prefetch_related в эндпоинте меню для минимизации количества SQL-запросов (решение проблемы N+1).

    Relations: Архитектура включает связи OneToOne (Chef-Restaurant), ForeignKey (Pizza/Review-Restaurant) и ManyToMany (Pizza-Ingredient).

Тестирование

Для запуска автоматизированных тестов использовать команду:
Bash

python manage.py test api
