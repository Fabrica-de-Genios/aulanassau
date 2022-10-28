from django.shortcuts import render
from .models import Postagem

def home(request):
    postagens = Postagem.objects.all().order_by('-id').values()
    return render(request, "home.html", {"dados":postagens})