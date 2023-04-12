from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})


def test(request):
    import requests
    response = requests.get('https://djangoerni.pythonanywhere.com/courses/')
    data = response.json()
    return render(request, 'test.html', {'data':data})