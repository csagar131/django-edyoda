from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from userprofile.models import User
from caremainapp.forms import ReviewForm
from django.views import View
from caremainapp.models import Reviews,CareRequest


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



class PeopleDetailView(View):
    
    def get(self,request,id,*args,**kwargs):
        form = ReviewForm()
        usr = User.objects.get(id = id)
        review = usr.ureviews.all()
        return render(request,'details.html',context={'form':form,'review':review,'usr':usr})

    
    def post(self,request,id,*args,**kwargs):
        form = ReviewForm(request.POST)
        usr = User.objects.get(id = id)
        review = usr.ureviews.all()
        if form.is_valid():
            user_review = form.cleaned_data['review']
            rev_object = Reviews.objects.create(user=usr,reviews=user_review,review_by = request.user)
            rev_object.save()
        form = ReviewForm()
        return render(request,'details.html',context={'form':form,'review':review,'usr':usr})


class RequestDetailView(View):
    def get(self,request,id,*args,**kwargs):
        form = ReviewForm()
        usr = User.objects.get(id = id)
        review = usr.ureviews.all()
        if len(CareRequest.objects.filter(request_by = request.user).filter(appr_status = True)) <= 3:
            if not CareRequest.objects.filter(request_by = request.user,request_to= usr).exists():
                req_object = CareRequest.objects.create(request_by = request.user,request_to= usr,req_status = True,appr_status = False)
                req_object.save()
        else:
            return HttpResponse("You have Exceeded the Care Limit of 4 person")
        return render(request,'reqdetails.html',context={'form':form,'review':review,'usr':usr})



class YoungerRequestView(View):
    def get(self,request,*args,**kwargs):
        req_object = CareRequest.objects.filter(request_to = request.user).filter(appr_status = False)
        return render(request,'request.html',context={'requests':req_object})


class ApproveRequestView(View):
    def get(self,request,id,*args,**kwargs):
        usr = User.objects.get(id = id)
        review = usr.ureviews.all()
        return render(request,'approvereq.html',context={'review':review,'usr':usr})


class ApproveRequestSuccessView(View):
    def get(self,request,id,*args,**kwargs):
        if len(CareRequest.objects.filter(request_to = request.user).filter(appr_status = True)) > 0:
            return HttpResponse("Sorry,You are already being taken care can't accept another request")
            
        usr = User.objects.get(id = id)
        review = usr.ureviews.all()
        req_obj = CareRequest.objects.filter(request_by = usr).filter(request_to = request.user)
        req_obj.update(request_by = usr,request_to = request.user,req_status = False,appr_status = True)
        return render(request,'approvereqsuccess.html',context={'review':review,'usr':usr})






