from tabom.models import Article, Like, User


def do_like(user_id: int, article_id: int) -> Like:
    # user = User.objects.get(pk=user_id)
    # article= Article.objects.get(pk=aticle_id)
    like = Like.objects.create(user_id=user_id, article_id=article_id)
    # like=Like(user=user_id, aticle=aticle_id).save()
    return like
