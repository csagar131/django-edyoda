from django.urls import path,include
from caremainapp.views import PeopleListView,PeopleDetailView,RequestDetailView

urlpatterns = [
    path('people',PeopleListView.as_view(),name="people"),
    path('people/<int:id>',PeopleDetailView.as_view(),name='detail'),
    path('people/<int:id>/<str:username>',RequestDetailView.as_view(),name='reqdetail'),
]