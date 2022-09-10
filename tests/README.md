# Yatube API
## Backend Yatube with API ready for frontend development or mobile application using
### Technologies
* Python 3.7
* Django 2.2.19
* Django-rest-api
* JWT + Djoser token authentication
### Launch project in DEV-mode
* Setup and activate venv 'source venv/Scripts/activate'
* Setup plugins from requirements.txt 'pip install -r requirements.txt'
* Appling migrations 'python manage.py migrate'
* Launch Dev-server 'python manage.py runserver'
### Oleg @OrdinaryWorker
### API Documentation on http://localhost:8000/redoc/
### Requests examples:
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