import json
from rest_framework import viewsets
#from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.db.models import Avg

from .models import Professor
from .models import Module
from .models import ProfRating


# @api_view(['GET'])
def List(request):
    if request.method == 'GET':
        subjects = Module.objects.all()
        list = []
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


# @api_view(['GET'])
def View(request):
    if request.method == 'GET':
        professors = Professor.objects.all()
        list = []
        for prof in professors:
            p = {
                'name': prof.name, 'average': prof.ratings.aggregate(Avg('rating'))['rating__avg']
            }
            list.append(p)

        result = {"Professors list": list}
        response = HttpResponse(json.dumps(result))
        return HttpResponse(response)


# @api_view(['GET'])
def Average(request, id, moduleId):
    if request.method == 'GET':
        rating = ProfRating.objects.filter(
            professor=id, module=moduleId).aggregate(Avg('rating'))['rating__avg']
        profName = Professor.objects.get(profId=id)
        moduleName = Module.objects.get(code=moduleId)
        x = {
            'name': profName.name, 'module': moduleName.name, 'average': rating
        }
        p = {"Module Rating": x}
        response = HttpResponse(json.dumps(p))
        return HttpResponse(response)


# @api_view(['GET'])
def Rate(request, rate, id, moduleId):
    if request.method == 'GET':
        prof = Professor.objects.get(profId=id)
        mod = Module.objects.get(code=moduleId)
        ProfRating.objects.create(professor=prof, module=mod, rating=rate)
        p = {"output": 'successful'}
        response = HttpResponse(json.dumps(p))
        return HttpResponse(response)
