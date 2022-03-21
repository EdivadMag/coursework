import json
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.db.models import Avg

from .models import Professor
from .models import Module
from .models import ProfRating


@api_view(['GET'])
def List(request):
    subjects = Module.objects.all()
    list = []
    profList = []
    for sub in subjects:
        professors = sub.professors.all()
        x = ''
        for c in professors:
            x = x + str(c.name) + " "
        p = {'code': sub.code, 'name': sub.name, 'professors': x}
        list.append(p)

    result = {"subject list": list}
    response = HttpResponse(json.dumps(result))
    return HttpResponse(response)


@api_view(['GET'])
def View(request):
    professors = Professor.objects.all()
    list = []
    # subjects = Subject.objects.filter(professor='1IT')

    for prof in professors:
        p = {
            'name': prof.name, 'average': prof.ratings.aggregate(Avg('rating'))['rating__avg']
        }
        list.append(p)

    result = {"Professors list": list}
    response = HttpResponse(json.dumps(result))
    return HttpResponse(list)


@api_view(['GET'])
def ModuleRating(request, profId, moduleId):
    rating = ProfRating.objects.filter(
        professor=profId, module=moduleId).aggregate(Avg('rating'))
    return HttpResponse(rating)
