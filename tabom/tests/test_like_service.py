from django.test import TestCase

from tabom.models import User, Article
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        #given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        #when
        like = do_like(user.id, article.id)

        #then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)