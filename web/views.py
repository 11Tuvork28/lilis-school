from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import ContactForm

def index(request):
    print("test")
    if request.method == 'POST':
        print("test")
        form = ContactForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("test")
            subject = form.cleaned_data['subject']
            from_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data['message']
            email_to = form.cleaned_data['email']
            try:
                send_mail(subject, message, from_email, [email_to,from_email])
            except BadHeaderError:
                pass
            redirect('index')
    
    context = {
        "WilkommensText": WilkommensText.objects.filter(Anzeigen=True),
        "Fotos": Fotos.objects.all(),
        "blogs": Blog.objects.all().order_by('-id')[:3],
        "sponsoren":  Sponsoren.objects.all(),
        "roadmap": Roadmap.objects.all(), 
        "kontakt": Kontakt.objects.filter(Aktuell=True),
        "form": ContactForm(),

        }
    return render(request=request, template_name="web/home.html", context=context)

 
def blog(request, blog_id: int = None):
    if blog_id is None:
        context = {
            "blogs": Blog.objects.all()
        }
        return render(request=request, template_name="web/blog.html", context=context)
    else:
        context = {
            "blog": Blog.objects.filter(id=blog_id).get()
        }
        return render(request=request, template_name="web/ReadBlog.html", context=context)