from django.db.models import F

from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:
    # like = Like.objects.filter(user_id=user_id, article_id=article_id)
    # if like.exists():
    #     raise Exception("Already Liked")
    like = Like.objects.create(user_id=user_id, article_id=article_id)
    Article.objects.filter(id=article_id).update(like_count = F("like_count") + 1)
    return like


def undo_like(user_id: int, article_id: int) -> None:
    delete_count, _ = Like.objects.filter(user_id=user_id, article_id=article_id).delete()
    if delete_count:
        article = Article.objects.get(id=article_id)
        article.like_count -= 1
        article.save()
