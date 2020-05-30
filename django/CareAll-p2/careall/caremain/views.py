from django.shortcuts import render
from django.views import View
from accounts.models import CareGiver,User,CareSeeker
from django.views.generic import DetailView,ListView,UpdateView
from django.http import HttpResponse
from caremain.models import CareRequests
from caremain.forms import ActivateRequestForm

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
        if self.request.user.is_elder == False:
            data['careseeker'] = CareSeeker.objects.get(user = usr)
        return data


class SendCareRequestView(View):
    def get(self,request,slug,*args,**kwargs):
        form = ActivateRequestForm
        caregiver = CareGiver.objects.get(user = request.user)
        if caregiver.get_active_care_count() < 4 :
            careseeker = User.objects.get(slug = slug)
            carerequest = CareRequests.objects.create(caregiver = request.user,careseeker = careseeker,status = 'pending')
            carerequest.save()
        else:
            return HttpResponse("you have exceeded the care taking limit")
        if CareRequests.objects.filter(caregiver = request.user,careseeker = careseeker,status = 'pending').exists():
            current_req_status = 'pending'
        careseekeruser = CareSeeker.objects.get(user = careseeker)
        context['form'] = form
        return render(request,'detailuser.html',context={'usr':careseeker,'careseeker': careseekeruser,'req_status':current_req_status,'form':form})

    

class AcceptRejectRequestView(View):  #this wiil be the view where several conditions will be checked
    def get(self,request,str,slug,*args,**kwargs):
        care_seeker = CareSeeker.objects.get(user = request.user)
        giver = User.objects.get(slug = slug)
        care_giver = CareGiver.objects.get(user = giver)
        care_request = CareRequests.objects.filter(careseeker = request.user,caregiver = giver)
        if str == 'approve':
            if CareRequests.objects.filter(careseeker = request.user,status = 'approved'):
                return HttpResponse("You have already approved one Request")
            care_seeker.set_is_available_false()
            care_giver.increment_care_count()
            care_giver.save()
            care_request.update(status = 'approved')
            care_seeker.save()
        if str == 'reject':
            care_request.update(status = 'rejected')
        active_request = CareRequests.objects.filter(careseeker = request.user).filter(status ='active')
        approved_request = CareRequests.objects.filter(careseeker = request.user).filter(status ='approved')
        req_statuses = CareRequests.objects.filter(careseeker = request.user).filter(status ='pending')
        return render(request,'dashboard.html',context={'req_statuses':req_statuses,'active':active_request,'approve':approved_request})







class StartServiceView(UpdateView):
    pass
    

class EndServiceView(View):
    pass








