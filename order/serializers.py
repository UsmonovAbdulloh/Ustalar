from rest_framework import serializers
from .models import OrderModel,UstaModel,ClientModel


class UstaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UstaModel
        fields = ('name','fname','phone_number','price')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('order','client_problem','price')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        field = ('client_name','client_phonenumber','client_location')