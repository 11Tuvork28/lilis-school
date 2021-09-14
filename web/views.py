from web.models import Fotos, WilkommensText
from django.shortcuts import render
from .models import *

def index(request):
    context = {
        "WilkommensText": WilkommensText.objects.filter(Anzeigen=True),
        "Fotos": Fotos.objects.all(),
        "blogs": Blog.objects.all().order_by('-id')[:3],
        "sponsoren":  Sponsoren.objects.all(),
        "roadmap": Roadmap.objects.all(), 
        "kontakt": Kontakt.objects.filter(Aktuell=True)

    }
    return render(request=request, template_name="web/home.html", context=context)

 
def blog(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request=request, template_name="web/blog.html", context=context)