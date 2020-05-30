from django.urls import path,include
from caremain.views import IndexView,ListElders,CandidateDetailView,SendCareRequestView,StartServiceView


urlpatterns = [
   path('home',IndexView.as_view(),name = 'index'),
   path('candidates',ListElders.as_view(),name = 'listelders'),
   path('candidates/<slug:slug>',CandidateDetailView.as_view(),name = 'candidatedetail'),
   path('request/<slug:slug>',SendCareRequestView.as_view(),name = 'sentrequest'),
   path('request/startservice',StartServiceView.as_view(),name = 'startservice'),
]