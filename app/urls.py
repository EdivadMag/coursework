# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.List, name='list'),
    path('view/', views.View, name='view'),
    path('average/<str:id>/<str:moduleId>',
         views.Average, name='average'),
    path('rate/<int:rate>/<str:id>/<str:moduleId>',
         views.Rate, name='rate')
]
