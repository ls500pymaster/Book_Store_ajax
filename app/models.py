from django.db import models


class Number(models.Model):
    username = models.CharField(max_length=10, blank=False, null=True)
    number = models.PositiveIntegerField(blank=False, null=True)

    def __str__(self):
        return self.username


class Car(models.Model):
    style = models.CharField(max_length=10, blank=True, null=True)
    manufacturer = models.CharField(max_length=12, blank=True, null=True)
    model = models.TextField(max_length=20, blank=True, null=True)
    engine_cc = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.model
