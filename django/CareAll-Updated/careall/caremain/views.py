from django.shortcuts import render
from django.views import View
from accounts.models import CareGiver,User,CareSeeker
from django.views.generic import DetailView,ListView
from django.http import HttpResponse
from caremain.models import CareRequests

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
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        usr = User.objects.get(slug = self.object.slug)
        if CareRequests.objects.filter(caregiver = self.request.user,careseeker = usr,status = 'pending').exists():
            data['req_status'] = 'pending'
        data['careseeker'] = CareSeeker.objects.get(user = usr)
        return data


class SendCareRequestView(View):
    def get(self,request,slug,*args,**kwargs):
        caregiver = CareGiver.objects.get(user = request.user)
        if caregiver.get_active_care_count() < 4 :
            careseeker = User.objects.get(slug = slug)
            carerequest = CareRequests.objects.create(caregiver = request.user,careseeker = careseeker,status = 'pending')
            carerequest.save()
        if CareRequests.objects.filter(caregiver = request.user,careseeker = careseeker,status = 'pending').exists():
            current_req_status = 'pending'
        careseekeruser = CareSeeker.objects.get(user = careseeker)
        return render(request,'detailuser.html',context={'usr':careseeker,'careseeker': careseekeruser,'req_status':current_req_status})

    













