from django.shortcuts import render

def auth(request):
    return render(request, 'auth.html')
