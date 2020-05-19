from django.urls import path,include
from caremainapp.views import PeopleListView,PeopleDetailView,RequestDetailView,YoungerRequestView,ApproveRequestView,ApproveRequestSuccessView

urlpatterns = [
    path('people',PeopleListView.as_view(),name="people"),
    path('people/<int:id>',PeopleDetailView.as_view(),name='detail'),
    path('people/<int:id>/<str:username>',RequestDetailView.as_view(),name='reqdetail'),
    path('people/requests',YoungerRequestView.as_view(),name = 'requests'),
    path('people/requests/<int:id>',ApproveRequestView.as_view(),name = 'approvereq'),
    path('people/requests/<int:id>/success',ApproveRequestSuccessView.as_view(),name = 'approvereqsuccess'),
]