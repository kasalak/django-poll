from django.test import TestCase
import datetime

from django.utils import timezone
from .models import Question

# Create your tests here.

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """
        was_published_recently() should return False for questions with a
        pub_date in the future
        """

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)
