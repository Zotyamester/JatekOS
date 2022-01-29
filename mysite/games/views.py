from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import GameContent, Lobby


class LobbyListView(ListView):
    model = Lobby
    ordering = ['name', 'game']
    paginate_by = 8

    def get_queryset(self):
        queryset = Lobby.objects.all()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(game__name__icontains=q))
        return queryset


class LobbyDetailView(DetailView):
    model = Lobby


class LobbyCreateView(LoginRequiredMixin, CreateView):
    model = Lobby
    fields = ['name', 'game']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class LobbyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lobby
    fields = ['name', 'game']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        lobby = self.get_object()
        return self.request.user == lobby.owner


class LobbyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lobby

    def get_success_url(self):
        return reverse('games:lobby-list')

    def test_func(self):
        Lobby = self.get_object()
        return self.request.user == Lobby.owner or self.request.user.is_staff and not Lobby.owner.is_superuser


@login_required
def lobby_leave(request, pk):
    lobby = get_object_or_404(Lobby, pk=pk)
    request.user.profile.playing = None
    request.user.save()
    messages.success(request, 'Sikeresen elhagyta a játéklobbit.')
    return redirect('games:lobby-list')


@login_required
def lobby_join(request, pk):
    lobby = get_object_or_404(Lobby, pk=pk)
    request.user.profile.playing = lobby
    request.user.save()
    messages.success(request, 'Sikeresen csatlakozott a játéklobbihoz.')
    return redirect('games:lobby-detail', pk=lobby.id)


@login_required
def gamedata(request, game):
    data = GameContent.objects.filter(
        game__name=game).order_by('?').first().json
    return JsonResponse(data, safe=False)


@login_required
def publish_score(request, score):
    if request.method == 'POST':
        request.user.profile.score = score
        request.user.save()
        return HttpResponse(status=204)
    return HttpResponse(status=400)


@login_required
def scores(request, pk):
    lobby = get_object_or_404(Lobby, pk=pk)
    data = []
    for profile in lobby.userprofiles.all():
        data.append({'username': profile.user.username,
                    'score': profile.score})
    return JsonResponse(data, safe=False)
