from django.urls import path
from . import views

urlpatterns = [
    path('sai/',views.Sai),
    path('pavani/',views.Ironman, name='ironman')
]