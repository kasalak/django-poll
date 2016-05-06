import datetime
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
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

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose pub_date
        was older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose pub_date
        is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)

    def create_question(question_text, days):
        """
        Creates a question with the given 'question_text' and published the
        given number of 'days' offest to now (negative for questions published
        in the past, positive for questions published in the future)"""
        time = timezone.now() + datetime.timedelta(days=days)
        
        return Question.objects.create(question_text, pub_date=time)
