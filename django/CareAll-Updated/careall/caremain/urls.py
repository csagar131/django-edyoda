from django.urls import path,include
from caremain.views import IndexView,ListElders,CandidateDetailView


urlpatterns = [
   path('home',IndexView.as_view(),name = 'index'),
   path('candidates',ListElders.as_view(),name = 'listelders'),
   path('candidates/<int:id>',CandidateDetailView.as_view(),name = 'candidatedetail'),
]