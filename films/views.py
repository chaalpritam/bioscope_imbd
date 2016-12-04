from django.shortcuts import render
from django.views.generic.detail import DetailView
# Create your views here.
from django.views.generic import ListView
from .models import Film
from .forms import ContactForm

from django.conf import settings
from django.core.mail import send_mail

class FilmsDetail(DetailView):
    model = Film
    template_name = 'detail.html'
class HomeView(ListView):
    model = Film
    queryset = Film.objects.order_by('-created_date')[:9]
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context
def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        subject = "Bioscope Contact Form"
        from_email = settings.EMAIL_HOST_USER 
        to_email = [email]
        send_mail(subject, message, from_email, to_email, fail_silently=False)
        form = ContactForm()
    return render(request, "contact.html", {"title":title, "form":form})
