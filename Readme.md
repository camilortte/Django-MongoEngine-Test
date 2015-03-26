Test Django Mongo
==================

This is a sample project, that show how work with tho databases, especific with MongoDB(Use [django-mongodb-engine](https://django-mongodb-engine.readthedocs.org/en/latest/)) and other like SQLite.

## Config enviroment
Firs you should configurate the project:

- Init mongo:
```
mongod
```

- Open a shel of mongo (To view the data):
```
mongo
```

- Type next:
```
db.prueba
use prueba
```

- Create new env, install the requiere packages and sync de database:
```
pip install -r requeriments.txt
python manage.py syncdb
```

## View databases:
In this moment see the database and compare with models in the ```main/models.py``` folder, you can see taht Article model is no in the database.

- Now type in the shell of Django project(```python manage shell```):
```
from main.models import Article
article = Article(
	title="Un nuevo titulo",
	content="Esto será guardado en MongoDB"
)
article.cosa = {'cosas': 'Guardo cualquier json'}
article.save()
```

## Test the data:
In the shell's mongo type:
```db.main_article.find()```
You can see the data of model Article save.


## Help?
- [Django and multiples databases](https://docs.djangoproject.com/en/1.7/topics/db/multi-db/)
- [django-mongodb-engine](https://django-mongodb-engine.readthedocs.org/en/latest/)) 

#About
Camilo Ramírez @camilortte - camilolinchis@gmail.com 

