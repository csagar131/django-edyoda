from django.urls import path,include
from caremainapp.views import PeopleListView,PeopleDetailView

urlpatterns = [
    path('people',PeopleListView.as_view(),name="people"),
    path('people/<int:pk>',PeopleDetailView.as_view(),name='detail'),
]