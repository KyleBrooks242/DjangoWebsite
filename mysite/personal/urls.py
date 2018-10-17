from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^projects/', views.projects, name='project'),
    url(r'^blog/', views.blog, name='blog'),
]
