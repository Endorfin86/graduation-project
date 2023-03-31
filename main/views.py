from django.shortcuts import render
from .models import Links
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def home(request):
    return render(request, 'main/home.html')

def aboutus(request):
    return render(request, 'main/aboutus.html')

class CreateLinks(LoginRequiredMixin, CreateView):
    model = Links
    template_name = 'main/create_link.html'
    fields = ['fulllink', 'shortlink']
        
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreateLinks, self).get_context_data(**kwards)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        ctx['link'] = Links.objects.filter(creator=user)
        return ctx

    

    
