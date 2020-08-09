from django.contrib import admin
from django.conf.urls import url, include
from . import views 
from .views import MedicationListView, MedicationDetailView, MedicationCreateView, MedicationUpdateView


app_name = 'temp'

urlpatterns = [
    url(r'^medication/$', MedicationCreateView.as_view(), name='medication'),
    url(r'^medication/list/$', MedicationListView.as_view(), name='medication_list'),
    url(r'^medication/update/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', MedicationUpdateView.as_view(), name='medication'),
    url(r'^medication/detail/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', MedicationDetailView.as_view(), name='medication_detail'),
    url(r'^forgpassword/$', views.forgpassword, name='forgpassword'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^appointment/$', views.appointment, name='appointment'),
    url(r'^diet.html/$', views.diet, name='diet'),
    url(r'^editprofile/$', views.editprofile, name='editprofile'),
    url(r'^exercise/$', views.exercise, name='exercise'),
    url(r'^offline/$', views.offline, name='offline'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^recenttrips/$', views.recenttrips, name='recenttrips'),
    url(r'^recentvaccine/$', views.recentvaccine, name='recentvaccine'),
    ]  