from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from turistea.models import Contact


class IndexView(TemplateView):
    template_name = 'home.html'


def formcontact(request):
    if request.method == 'POST':
        contacto = Contact(name=request.POST['name'], email=request.POST['email'], description=request.POST['message'])
        contacto.save()
    return render(request, 'home.html')
