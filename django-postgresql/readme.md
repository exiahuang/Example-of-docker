# Summary

Django, postgresql, docker

# how to create a docker project
`you not need to run this command!`
```
docker-compose run web django-admin.py startproject django_example .
```

the code will be like below

```
│  docker-compose.yml
│  Dockerfile
│  manage.py
│  readme.md
│  requirements.txt
│
└─django_example
        settings.py
        urls.py
        wsgi.py
        __init__.py
```


# run server
docker-compose up

# sync with your db
```
$ docker-compose run web python manage.py syncdb
```