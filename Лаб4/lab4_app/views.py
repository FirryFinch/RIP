from django.shortcuts import render


def btfmovies(request):
    return render(request, 'btfmovies.html', {'btfmovies': [
        {'title': 'Назад в будущее (1985)', 'id': 1},
        {'title': 'Назад в будущее 2 (1989)', 'id': 2},
        {'title': 'Назад в будущее 3 (1990)', 'id': 3}
    ]
    })


def btfmovie(request, id):
    return render(request, 'btfmovie.html', {
        'id': id
    })
