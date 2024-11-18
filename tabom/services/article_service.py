from tabom.models import Article


def get_an_article(article_id: int) -> Article:
    return Article.objects.get(pk=article_id)
