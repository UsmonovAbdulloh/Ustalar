from django.urls import path
from .views import AllOrderView,DeleteOrderView,DetailOrderView,CreateOrderView,ClientModel
urlpatterns = [
    path("",AllOrderView.as_view()),
    path("delete/<int:order_id>",DeleteOrderView.as_view()),
    path("create/",CreateOrderView.as_view()),
    path("detail/<int:order_id>",DetailOrderView.as_view()),
]