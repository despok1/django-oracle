from django.shortcuts import render


def index(request):
    return render(request, "oracle/index.html")


def info(request):
    return render(request, "oracle/info.html")
