from django.shortcuts import render

# Create your views here.


def meow(request):
    return render(request, "base/home.html")
