from django.shortcuts import render

# Create your views here.

data = {
    'title': 'Главная страница',
    'values': ['Some', 'Hello', '123'],
    'obj': {
        'Car': 'BMW',
        'Age': 18,
        'hobby': 'Football'
    }
}


def index(request):
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
