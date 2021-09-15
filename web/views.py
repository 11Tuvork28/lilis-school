from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from .models import *
from .forms import ContactForm

def index(request):
    context = {
        "WilkommensText": WilkommensText.objects.filter(Anzeigen=True),
        "Fotos": Fotos.objects.all(),
        "blogs": Blog.objects.all().order_by('-id')[:3],
        "sponsoren":  Sponsoren.objects.all(),
        "roadmap": Roadmap.objects.all(), 
        "kontakt": Kontakt.objects.filter(Aktuell=True),
        "form": ContactForm(),

    }
    if request.method != 'GET':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['zofi@xamh.de', from_email])
            except BadHeaderError:
                pass
            redirect('index')

    return render(request=request, template_name="web/home.html", context=context)

 
def blog(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request=request, template_name="web/blog.html", context=context)