# Yatube API
### Описание:
APi-сервис Yatube, имеющий тот же функционал что и Yatube_Django_project(https://github.com/OrdinaryWorker/Yatube_Django_project), но предотсавляющий исключительно интерфейс для других веб-сервисов и мобильных приложений. Основным используемым модулем явлеяется DRF, для аутентификации пользователей использйется модуль JWT.
### Стек технологий:
* Python 3.7
* Django 2.2.19
* Django-rest-api
* JWT + Djoser token authentication
### Запуск проекта в DEV-режиме:
* Setup and activate venv 'source venv/Scripts/activate'
* Setup plugins from requirements.txt 'pip install -r requirements.txt'
* Appling migrations 'python manage.py migrate'
* Launch Dev-server 'python manage.py runserver'
### Документация по API находится по адресу: http://localhost:8000/redoc/
### Примеры запросов:
___
GET http://127.0.0.1:8000/api/v1/posts/
___
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
___
GET http://127.0.0.1:8000/api/v1/posts/{id}/
___
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
___
