from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def agenda(request):
    return render(request, 'agenda.html')