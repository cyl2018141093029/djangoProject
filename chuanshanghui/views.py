# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import PeopleForm
from .models import People


def index(request):
    people = People.objects.all()
    if request.method == 'Post':
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            form = PeopleForm()

        context = {
            'people': people,
            'form': form
        }
        return render(request, 'index.html', context=context)
