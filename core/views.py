from django.shortcuts import render
from core.scripts.parsing import get_all_names, analys_match


def index(request):
    return render(request, 'index.html')


def rating(request):
    top_teams = get_all_names()
    return render(request, 'rating.html', {'top_teams': top_teams})


def description(request):
    return render(request, 'description.html')


def analys(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        ftn, ftp, ftl, stn, stp, stl = analys_match(link)
        return render(request, 'analys.html', {'first_team_name': ftn, 'first_team_percents': ftp, 'first_team_logo': ftl, 'second_team_name': stn, 'second_team_percents': stp, 'second_team_logo': stl})
    return render(request, 'analys.html')
