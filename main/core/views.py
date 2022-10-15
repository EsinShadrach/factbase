from django.shortcuts import render
from time import strftime


def index(request):
    date = strftime('%A %B %d %Y')
    time = strftime('%I:%M %p')
    context = {
        'date': date,
        'time': time,
    }
    return render(
        request,
        'core/index.html',
        context
    )
