from django.shortcuts import render
import random

# Create your views here.

def home(request):
    number = random.randint(1,6)
    return render(request, 'dice.html', {'number': number})