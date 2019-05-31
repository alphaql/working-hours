# Creation of a restframework API with Django


Follow these commands for building the container:

```bash
docker-compose build
docker-compose up
```

It's possible to drop all containers with this command:

```bash
docker-compose down
```

With this command you can access to one shell associated to the web container: 

```bash
docker-compose up web /bin/bash
```


When the web container is running it's necessary to create the migrations in
the database, so execute this:
```bash
python manage.py migrate
```

With this command you can create a superuser account:
```bash
python manage.py createsuperuser
```

The admin page will be available in the following URL:
http://localhost:8081/admin

The django project and several apps were created with
these commands in local:

```bash
django-admin startproject django_project .
django-admin startapp api
```