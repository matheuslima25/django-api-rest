from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.name