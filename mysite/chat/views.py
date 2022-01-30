from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def room(request, room_id):
    return render(request, 'chat/chatroom.html', {
        'room_id': room_id
    })
