from django.contrib import admin
from django.conf.urls import url, include
from . import views 
from .views import MedicationListView, MedicationDetailView, MedicationCreateView, MedicationUpdateView, MedicationDeleteView
from .views import TripCreateView, TripDetailView, TripListView, TripUpdateView, TripDeleteView
from .views import VaccineListView, VaccineDetailView, VaccineCreateView, VaccineUpdateView, VaccineDeleteView
from .views import DietCreateView, DietDetailView, DietListView, DietUpdateView, DietDeleteView

app_name = 'temp'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^medication/$', MedicationCreateView.as_view(), name='medication'),
    url(r'^medication/list/$', MedicationListView.as_view(), name='medication_list'),
    url(r'^medication/update/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', MedicationUpdateView.as_view(), name='medication'),
    url(r'^medication/detail/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', MedicationDetailView.as_view(), name='medication_detail'),
    url(r'^medication/delete/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', MedicationDeleteView.as_view(), name='medication_delete'),

    url(r'^recenttrips/$', TripCreateView.as_view(), name='recenttrips'),
    url(r'^recenttrips/list/$', TripListView.as_view(), name='trip_list'),
    url(r'^recenttrips/update/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', TripUpdateView.as_view(), name='recenttrips'),
    url(r'^recenttrips/detail/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', TripDetailView.as_view(), name='trip_detail'),
    url(r'^recenttrips/delete/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', TripDeleteView.as_view(), name='trip_delete'),

    url(r'^recentvaccine/$', VaccineCreateView.as_view(), name='recentvaccine'),
    url(r'^recentvaccine/list/$', VaccineListView.as_view(), name='vaccine_list'),
    url(r'^recentvaccine/detail/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', VaccineDetailView.as_view(), name='vaccine_detail'),
    url(r'^recentvaccine/update/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', VaccineUpdateView.as_view(), name='recentvaccine'),
    url(r'^recentvaccine/delete/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', VaccineDeleteView.as_view(), name='vaccine_delete'),

    url(r'^diet/$', DietCreateView.as_view(), name='diet'),
    url(r'^diet/list/$', DietListView.as_view(), name='diet_list'),
    url(r'^diet/detail/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', DietDetailView.as_view(), name='diet_detail'),
    url(r'^diet/update/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', DietUpdateView.as_view(), name='diet'),
    url(r'^diet/delete/(?P<pk>[0-9]+)/(?P<slug>[-\w\d]+)/$', DietDeleteView.as_view(), name='diet_delete'),

    url(r'^profile/$', views.profile, name='profile'),
    url(r'^editprofile/$', views.editprofile, name='editprofile'),

    # url(r'^forgpassword/$', views.forgpassword, name='forgpassword'),
    

    url(r'^appointment/$', views.appointment, name='appointment'),
    url(r'^exercise/$', views.exercise, name='exercise'),
    url(r'^offline/$', views.offline, name='offline'),
    ]  