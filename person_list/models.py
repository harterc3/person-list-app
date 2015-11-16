from datetime import date

from django.db import models


class Person(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	date_of_birth = models.DateField()
	zip_code = models.CharField(max_length=10)

	def __unicode__(self):
		return '{} {} was born on {} and lives in {}'.format(self.first_name, self.last_name, self.date_of_birth, self.zip_code)

	def was_born_in_past(self):
		return self.date_of_birth <= date.today()