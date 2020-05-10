from django.test import TestCase

from .models import Article

from datetime import datetime, timedelta

class ArticleTest(TestCase):
    def test_recent_with_future_article(self):
        """
            An article with a date in the future can't be considered as recent
        """

        futureArticle = Article(date = datetime.now()+ timedelta(days = 20))
        self.assertEqual(futureArticle.is_recent(), False)

# Create your tests here.
