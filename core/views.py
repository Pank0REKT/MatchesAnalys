from django.shortcuts import render
from core.scripts.parsing import get_all_names


def index(request):
    return render(request, 'index.html')


def rating(request):
    top_teams = get_all_names()
    return render(request, 'rating.html', {'top_teams': top_teams})
