# Учебный Проект Яндекс практикума Yatube
Yatube сервис для публикации личных дневников или блогов. 
Сервис позволяет регистрироваться и публиковать собственные записи в блоге , 
группировать блоги по группам, просматривать, подписываться и оставлять комментарии на других авторов.

[![2022-02-20-005129.png](https://i.postimg.cc/jddJtB9W/2022-02-20-005129.png)](https://postimg.cc/K4wY5pmF)

### Функционал проекта.

1. Установка интерфейса администратора сайта (админка).
 - создание суперпользователя (администратора)
 - регистрация в админке моделей Post и Group (описание моделей см.ниже) для возможности администрирования сообществ и постов пользователей (создание/редактирование/удаление).
 - реализация системы поиска и фильтрации в админке.

2. Создание и настройка форм регистрации и аутентификации пользователей.
Реализация возможности::
 - зарегистрироваться на сайте
 - пройти аутентификацию
 - сменить пароль.

3. Настройка авторизации пользователей.

    3.1. Неавторизованный пользователь может:
     - просматривать посты всех пользователей
     - просматривать комментарии к постам.
     - просматривать профиль сообщества

    3.2. Авторизованный пользователь может.
     - просматривать посты всех пользователей
     - просматривать комментарии к постам.
     - просматривать профиль сообщества
     - создавать пост (с указанием/без сообщества)
     - редактировать собственный пост
     - комментировать посты  свои и других авторов
     - редактировать свои комментарии
     - удалять свои комментарии
     - подписываться/отписываться от других авторов


4. Настройка пагинации:
 - на главной странице
 - на странице сообщества
 - в админке (в разделе постов)

##Для локального запуска проекта 
Клонируем репозиторий и переходим в него
```
git clone https://github.com/antonov-andreu/yatube
```
Открываем проект и устанавливаем виртуальное окружение
```
python -m venv env
```
Включаем Debug режим в settings.py
```
DEBUG = True
```
Активируем виртуальное окружение(для windows)
```
source env/scripts/activate
```
Активируем виртуальное окружение(для mac)
```
source env/bin/activate
```
Обновляем менеджер пакетов и устанавливаем требуемые пакеты
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Переходим в папку головного проекта
```
cd yatube/
```
Применяем миграции в базу данных
```
python manage.py migrate
```
Собираем статику для проекта
```
python manage.py collectstatic
```
Создаем суперпользователя для входа в админку
```
python manage.py createsuperuser
```
Запускаем проект локально
```
python manage.py runserver
```
После запуска проект будет доступен по адресу  http://127.0.0.1:8000/

Админ панель будет доступна по адресу  http://127.0.0.1:8000/admin

(Для прекращения работы проекта в терминале Pycharm нужно нажать control + c )

##Для запуска проекта в docker
Выключаем Debug режим в settings.py
```
DEBUG = False
```
Создаем в корневой папке проекта файл .env c переменными окружения для работы с базой данных
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
Зпускаем сборку докера
```
docker-compose up -d --build 
```
Далее делаем миграции, создаем суперпользователя и собираем статику
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```
После запуска проект будет доступен по адресу  http://localhost/

Админ панель будет доступна по адресу  http://localhost/admin
## Технологический стек:
- [Python3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Pillow](https://pypi.org/project/Pillow/)
- [Bootstrap](https://getbootstrap.com/)
## Автор 
https://github.com/antonov-andreu
