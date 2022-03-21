from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Module(models.Model):
    code = models.CharField(max_length=3,
                            unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField(default=2022)
    semester = models.IntegerField()

    def __str__(self):
        return f"Module(code={self.code}, name={self.name})"


class Professor(models.Model):
    profId = models.CharField(
        max_length=3, unique=True, primary_key=True)
    name = models.CharField(max_length=30)
    modules = models.ManyToManyField(
        Module, related_name="professors", blank=True)

    def __str__(self):
        return f"Professor(code={self.profId}, name={self.name})"


class ProfRating(models.Model):
    professor = models.ForeignKey(
        Professor, related_name='ratings', on_delete=models.CASCADE)
    module = models.ForeignKey(
        Module, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return f"rating(rating={self.rating}, professor={self.professor}), module={self.module})"