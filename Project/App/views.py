from django.shortcuts import render
from django.http import HttpResponse
from .forms import FoodFitnessForm, FoodFitnessModel


# Create your views here.
def index(request):
    return HttpResponse("Test URL")

def newUser(request):
    form = FoodFitnessModel(request.POST or None)

    context = {
        "form": form
    }
    if request.method == "POST":
        print(request.POST)
        # User.objects.create_user(request.POST["username"], ["calories"], ["date"])
    return render(request, 'App/newUser.html')
