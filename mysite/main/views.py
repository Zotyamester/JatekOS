from django.shortcuts import render
from games.models import Game


def home(request):
    activity = Game.objects.filter(name='Activity').first()
    chess = Game.objects.filter(name='Sakk').first()
    quiz = Game.objects.filter(name='Kvíz').first()
    return render(request, 'main/home.html', context={'activity': activity, 'chess': chess, 'quiz': quiz})
