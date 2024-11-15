from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:
    # like = Like.objects.filter(user_id=user_id, article_id=article_id)
    # if like.exists():
    #     raise Exception("Already Liked")
    like = Like.objects.create(user_id=user_id, article_id=article_id)
    return like
