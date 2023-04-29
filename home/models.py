from django.db import models
from django.contrib.auth.models import User


class HomeWork(models.Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True)
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    done = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, max_length=255, upload_to='uploads/')
    lesson = models.ForeignKey('Lesson', null=True, blank=True, on_delete=models.DO_NOTHING)


class Lesson(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name