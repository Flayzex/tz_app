from django.urls import path

from .views import *


urlpatterns = [
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),

    path('item/<int:pk>/', ItemView.as_view(), name='item-detail'),
    path('buy/<int:pk>/', BuyView.as_view(), name='buy'),
]