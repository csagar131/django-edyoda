from django.shortcuts import render
from django.views import View
from accounts.models import CareGiver,User,CareSeeker
from django.views.generic import DetailView,ListView

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')


class ListElders(View):
    def get(self,request,*agrs,**kwargs):
        if request.user.is_elder == False:
            elders = User.objects.filter(is_elder = True).exclude(username = 'admin')
            return render(request,'listcandidate.html',context = {'elders':elders})


class CandidateDetailView(DetailView):  

    model = User
    template_name = 'detailuser.html'
    context_object_name = 'usr'
    # def get(self,request,id,*args,**kwargs):
    #     usr = User.objects.get(id = id)
    #     careseeker = CareSeeker.objects.get(user = usr)
    #     return render(request,'detailuser.html',context={'usr':usr,'careseeker':careseeker})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        usr = User.objects.get(slug = self.object.slug)
        data['careseeker'] = CareSeeker.objects.get(user = usr)
        return data


    













