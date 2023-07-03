from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OrderModel,ClientModel,UstaModel
from rest_framework import status
# Create your views here.

class AllOrderView(APIView):
    def get(self,request,*args,**kwargs):
        all_order = OrderModel.objects.all()
        serializer = OrderModel(all_order,many=True)
        return Response(serializer.data)

class DetailOrderView(APIView):
    def get(self,request,*args,**kwargs):
        order = get_object_or_404(OrderModel,pk=kwargs['order_id'])
        serializer = OrderSerializer(order)
        return Response(serializer.data)

class CreateOrderView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteOrderView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(OrderModel,pk=kwargs['order_id'])
        instance.delete()
        return Response({'m':'success'},status=status.HTTP_204_NO_CONTENT)