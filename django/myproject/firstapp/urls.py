from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("form", views.myform, name="myform"),
    path("formprocess",views.process,name="process"),
    path('slist',views.studentlist.as_view(),name='s1')
]
