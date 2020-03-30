from django.shortcuts import render


def home(request):
    data = {
        'title':'Home'
    }
    return render(request, 'main/index.html', context=data)