from django.urls import path
from .views import ProfileList, ProfileDetail

urlpatterns = [
    path('',ProfileList.as_view()),
    path('<int:id>',ProfileDetail.as_view())
]