from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, Like, User
from tabom.services.like_service import do_like, undo_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # when
        like = do_like(user.id, article.id)

        # then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # given
        # list(Like.objects.filter(user_id=1))
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # expect
        like1 = do_like(user.id, article.id)
        # 예외(Exception) 발생하면 통과, 아니면 AssertionError발생
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)

    def test_it_should_raise_exception_when_like_an_user_does_not_exist(self) -> None:
        # Given
        invalid_user_id = 9988
        article = Article.objects.create(title="test_title")

        # Expect
        with self.assertRaises(IntegrityError):
            do_like(invalid_user_id, article.id)

    # def test_it_should_raise_exception_when_like_an_article_does_not_exist(self) -> None:
    #     # Given
    #     user = User.objects.create(name="test")
    #     invalid_article_id = 9988
    #
    #     # Expect
    #     with self.assertRaises(IntegrityError):
    #         do_like(user.id, invalid_article_id)

    def test_like_count_should_increase(self) -> None:
        # given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # when
        do_like(user.id, article.id)

        # then
        result_article = Article.objects.get(id=article.id)
        self.assertEqual(1, result_article.like_count)

    def test_a_user_can_undo_like(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")
        like = Like.objects.create(user_id=user.id, article_id=article.id)

        # When
        undo_like(user.id, article.id)

        # Then
        with self.assertRaises(Like.DoesNotExist):
            Like.objects.get(id=like.id)

    # def test_it_should_raise_exception_when_undo_like_which_does_not_exist(self) -> None:
    #     # Given
    #     user = User.objects.create(name="test")
    #     article = Article.objects.create(title="test_title")
    #
    #     # Expect
    #     with self.assertRaises(Like.DoesNotExist):
    #         undo_like(user.id, article.id)
