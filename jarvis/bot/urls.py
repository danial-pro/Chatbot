from django.urls import path
from .views import home

app_name = "bot"

urlpatterns = [
    path('', home,name='home'),
]