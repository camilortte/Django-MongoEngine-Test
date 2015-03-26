from main.models import Article
article = Article(title="Un nuvo")
article.cosa = {'cosas': 1}
article.save()
article.save(using='mongo')

# Init mongo mongod


# View data in Mongo:
# mongo

# use prueba
# db.main_article.find()

# https://docs.djangoproject.com/en/1.7/topics/db/multi-db/
