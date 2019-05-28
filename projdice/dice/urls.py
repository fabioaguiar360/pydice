from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
# Fluxo de chamadas no django
# request > urls > view > model > response