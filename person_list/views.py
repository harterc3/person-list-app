from datetime import date

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PersonForm
from .models import Person

def index(request):
	person_list = Person.objects.filter(
		date_of_birth__lte=date.today()
	)
	return render(request, 'person_list/index.html', {'person_list': person_list})

def create(request):
	if request.method == 'POST':
		form_submission = PersonForm(request.POST)
		if form_submission.is_valid():
			new_person = form_submission.save()
			return HttpResponseRedirect(reverse('person_list:detail', args=[new_person.id]))
	person_form = PersonForm()
	return render(request, 'person_list/create.html', {'person_form': person_form})

def detail(request, person_id):
	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		return redirect_to_index()
	else:
		return render(request, 'person_list/detail.html', {'person': person})

def edit(request, person_id):
	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		return redirect_to_index()
	else:
		if request.method == 'POST':
			form_submission = PersonForm(data=request.POST or None, instance=person)
			if form_submission.is_valid():
				form_submission.save()
				return HttpResponseRedirect(reverse('person_list:detail', args=[person_id]))
		person_form = PersonForm(instance=person)
		return render(request, 'person_list/edit.html', {'person_form': person_form, 'person': person})

def delete(request, person_id):
	try:
		person = Person.objects.get(pk=person_id)
	except Person.DoesNotExist:
		return redirect_to_index()
	else:
		if request.method == 'POST':
			person.delete()
			return redirect_to_index()
		return render(request, 'person_list/delete.html', {'person': person})

def redirect_to_index():
	return HttpResponseRedirect(reverse('person_list:index'))