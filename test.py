from main.models import Article
article = Article(title="Un nuvo")
article.cosa = {'cosas': 1}
article.save()
