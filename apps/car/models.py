from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=256)
    model = models.CharField(max_length=256)

    def __str__(self):
        return self.make


class Rating(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car")
    rating = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
