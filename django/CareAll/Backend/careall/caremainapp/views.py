from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from userprofile.models import User
from caremainapp.forms import ReviewForm

# Create your views here.
def indexView(request):
    if request.method == "GET":
        return render(request,'index.html')


class PeopleListView(ListView):
    template_name = 'people.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_elder == True:
            context['userlist'] = User.objects.filter(is_elder = False).exclude(username = 'admin')
        else:
            context['userlist'] = User.objects.filter(is_elder = True)
        return context


class PeopleDetailView(DetailView):
    model = User
    template_name = 'details.html'
    context_object_name = 'usr'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review'] = kwargs['object'].ureviews.all()
        return context
