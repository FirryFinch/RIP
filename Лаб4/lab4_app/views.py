from django.shortcuts import render


def engines(request):
    return render(request, 'engines.html', {'engines': [
        {'title': 'Рядная', 'id': 1},
        {'title': 'V-образная', 'id': 2},
        {'title': 'Оппозитная', 'id': 3}
    ]
    })


def engine(request, id):
    return render(request, 'engine.html', {
        'id': id
    })
