from django.urls import include, path

from . import views

app_name = 'games'
urlpatterns = [
    path('lobbies/', views.LobbyListView.as_view(), name='lobby-list'),
    path('lobby/<int:pk>/', views.LobbyDetailView.as_view(), name='lobby-detail'),
    path('lobby/new/', views.LobbyCreateView.as_view(), name='lobby-create'),
    path('lobby/<int:pk>/update/',
         views.LobbyUpdateView.as_view(), name='lobby-update'),
    path('lobby/<int:pk>/delete/',
         views.LobbyDeleteView.as_view(), name='lobby-delete'),
    path('lobby/<int:pk>/leave/', views.lobby_leave, name='lobby-leave'),
    path('lobby/<int:pk>/join/', views.lobby_join, name='lobby-join'),
    path('gamedata/<str:game>/', views.gamedata, name='gamedata'),
    path('publish_score/<int:score>/', views.publish_score, name='publish-score'),
    path('lobby/<int:pk>/scores/', views.scores, name='score-list'),
]
