from django.test import SimpleTestCase
from django.urls import reverse, resolve
import json
from server_app.views import intro, home, logout_user, exercise, signup, MedicationListView, MedicationCreateView, TripListView, TripCreateView, VaccineCreateView, VaccineListView, DietCreateView, DietListView, AppointCreateView, AppointCalendarListView, ProfileListView


class TestUrls(SimpleTestCase):
    def test_url_intro_is_resolved(self):
        self.intro_url = reverse('intro')
        print(resolve(self.intro_url))
        self.assertEquals(resolve(self.intro_url).func, intro)

    def test_url_home_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_url_logoutuser_is_resolved(self):
        self.logout_url = reverse('logout')
        print(resolve(self.logout_url))
        self.assertEquals(resolve(self.logout_url).func, logout_user)

    def test_url_exercise_is_resolved(self):
        url = reverse('temp:exercise')
        print(resolve(url))
        self.assertEquals(resolve(url).func, exercise)
    
    def test_url_signup_is_resolved(self):
        self.signup_url = reverse('temp:signup')
        print(resolve(self.signup_url))
        self.assertEquals(resolve(self.signup_url).func, signup)

    def test_url_medcreate_is_resolved(self):
        url = reverse('temp:medication')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, MedicationCreateView)

    def test_url_tripcreate_is_resolved(self):
        url = reverse('temp:recenttrips')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TripCreateView)

    def test_url_dietcreate_is_resolved(self):
        url = reverse('temp:diet')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, DietCreateView)

    def test_url_appointcreate_is_resolved(self):
        url = reverse('temp:appointment')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AppointCreateView)

    def test_url_profilelist_is_resolved(self):
        self.profile_url = reverse('temp:profile')
        print(resolve(self.profile_url))
        self.assertEquals(resolve(self.profile_url).func.view_class, ProfileListView)
