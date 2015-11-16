from datetime import date, timedelta

from django.test import TestCase

from .models import Person


class PersonMethodTests(TestCase):

	def test_was_born_in_past_with_past_dob(self):
		past_date = date.today() - timedelta(days=2)
		past_person = Person(date_of_birth=past_date)
		self.assertEqual(past_person.was_born_in_past(), True)

	def test_was_born_in_past_with_future_dob(self):
		future_date = date.today() + timedelta(days=2)
		future_person = Person(date_of_birth=future_date)
		self.assertEqual(future_person.was_born_in_past(), False)

	def test_was_born_in_past_with_today_dob(self):
		today_person = Person(date_of_birth=date.today())
		self.assertEqual(today_person.was_born_in_past(), True)