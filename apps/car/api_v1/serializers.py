from django.db.models import Sum
from rest_framework import serializers

from apps.car.models import Car, Rating


class CarSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()

    # calculate average rating
    def get_avg_rating(self, instance):
        car_ratings = [
            i.rating for i in Rating.objects.filter(car_id=instance.id)
        ]
        try:
            avg_rating = sum(car_ratings) / len(car_ratings)
        except ZeroDivisionError:
            avg_rating = 0

        return round(avg_rating, 2)

    class Meta:
        model = Car
        fields = ("make", "model", "avg_rating")


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("car", "rating")


class PopularSerializer(serializers.ModelSerializer):
    rates_number = serializers.IntegerField()

    class Meta:
        model = Car
        fields = ("make", "model", "rates_number")
        depth = 1
