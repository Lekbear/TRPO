from django.urls import path
from . import views
from django.views.generic import ListView,DetailView 
from login.models import deadlines

urlpatterns = [
    path('', views.home, name = 'home'), #создать home страничку
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('timetable/', views.timetable, name="timetable"),
    path('deadlines/', 
    ListView.as_view(queryset = deadlines.objects.all().order_by('deadlines'),
    template_name="/login/deadlines.html"), name = "deadlines"),
    path('deadlines/add', views.adddeadlines, name = 'adddeadlines'),
]
