import imp
import json
from pkgutil import ImpImporter

import requests
from django.db.models import Count
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from apps.car.api_v1.serializers import (
    CarSerializer,
    PopularSerializer,
    RatingSerializer,
)
from apps.car.helpers.car_search import carExistance
from apps.car.models import Car, Rating


# Create your views here.
class CarModelViewSet(viewsets.ModelViewSet, carExistance):
    authentication_classes = (TokenAuthentication,)
    queryset = Car.objects.all()

    def get_queryset(self):
        queryset = super(CarModelViewSet, self).get_queryset()
        return queryset

    def get_serializer_class(self):
        return CarSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        request_data = request.data
        make = request_data.get("make")
        model = request_data.get("model")

        # CHECK CAR EXISTANCE #
        is_car_exist = self.check_car_existance(make=make, model=model)

        if is_car_exist:
            # INSERT INTO DATABASE IF CAR EXIST #
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        else:
            # RETURN ERROR IF CAR DOESN'T EXIST #
            return Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data={
                    "error": f"Provided make of car {make} or model {model} doesn't exist"
                },
            )

    # FOR DELETE CAR #
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()


class RatingModelViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Rating.objects.all()

    # get ALL rating records in db
    def get_queryset(self):
        queryset = super(RatingModelViewSet, self).get_queryset()
        return queryset

    def get_serializer_class(self):
        return RatingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )
        except Exception:
            return Response(
                data={"error": "This Car is Does not exists"},
                status=status.HTTP_406_NOT_ACCEPTABLE,
            )


class PopulerModelViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Car.objects.all()

    # get ALL popular records in db
    def get_queryset(self):
        queryset = super(PopulerModelViewSet, self).get_queryset()
        queryset = queryset.annotate(rates_number=Count("car")).order_by(
            "-rates_number"
        )
        return queryset

    def get_serializer_class(self):
        return PopularSerializer
