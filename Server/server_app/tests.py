from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
import json
from server_app.views import intro, home, logout_user, exercise, signup, MedicationListView, MedicationCreateView, TripListView, TripCreateView, VaccineCreateView, VaccineListView, DietCreateView, DietListView, AppointCreateView, AppointCalendarListView, ProfileListView
from server_app.models import UserAppoint, UserDiet, UserMedication, UserProfile, UserTrip, UserVaccine
from django.contrib.auth.models import User


# ========================== TEST CASE TEMPLATE URLs ========================== #
class TestTempUrls(SimpleTestCase):
    def test_url_intro_is_resolved(self):
        self.intro_url = reverse('intro')
        self.assertEquals(resolve(self.intro_url).func, intro)
        print(resolve(self.intro_url))
        print('TESTE URL INDEX OK\n')

    def test_url_home_is_resolved(self):
        home_url = reverse('home')
        self.assertEquals(resolve(home_url).func, home)
        print(resolve(home_url))
        print('TESTE URL HOME OK\n')

    def test_url_logoutuser_is_resolved(self):
        self.logout_url = reverse('logout')
        self.assertEquals(resolve(self.logout_url).func, logout_user)
        print(resolve(self.logout_url))
        print('TESTE URL LOGOUT OK\n')
    
    def test_url_profilelist_is_resolved(self):
        self.profile_url = reverse('temp:profile')
        self.assertEquals(resolve(self.profile_url).func.view_class, ProfileListView)
        print(resolve(self.profile_url))
        print('TESTE URL LISTA PERFIL OK\n')

    def test_url_exercise_is_resolved(self):
        exercise_url = reverse('temp:exercise')
        print(resolve(exercise_url))
        self.assertEquals(resolve(exercise_url).func, exercise)
        print('TESTE URL EXERCICIO OK\n')

    def test_url_signup_is_resolved(self):
        self.signup_url = reverse('temp:signup')
        print(resolve(self.signup_url))
        self.assertEquals(resolve(self.signup_url).func, signup)
        print('TESTE URL ADD CONTA OK\n')

    def test_url_medcreate_is_resolved(self):
        med_url = reverse('temp:medication')
        print(resolve(med_url))
        self.assertEquals(resolve(med_url).func.view_class, MedicationCreateView)
        print('TESTE URL ADD MEDICAMENTOS OK\n')

    def test_url_tripcreate_is_resolved(self):
        trip_url = reverse('temp:recenttrips')
        print(resolve(trip_url))
        self.assertEquals(resolve(trip_url).func.view_class, TripCreateView)
        print('TESTE URL ADD VIAGENS OK\n')

    def test_url_dietcreate_is_resolved(self):
        diet_url = reverse('temp:diet')
        print(resolve(diet_url))
        self.assertEquals(resolve(diet_url).func.view_class, DietCreateView)
        print('TESTE URL ADD DIETA OK\n')

    def test_url_appointcreate_is_resolved(self):
        appoint_url = reverse('temp:appointment')
        print(resolve(appoint_url))
        self.assertEquals(resolve(appoint_url).func.view_class, AppointCreateView)
        print('TESTE URL ADD AGENDAMENTOS OK\n')

# ========================== TEST CASE AUTHENTICATION ========================== #
class TestAuth(TestCase):
    def test_user_can_login(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.assertTrue(user.is_authenticated)
        print(user.is_authenticated)
        print("TEST LOGIN OK\n")

    def test_logout(self):
        user = User.objects.create(username='testuser')
        user.set_password('test12345')
        user.save()
        self.client.logout()
        response = self.client.get('/logout/')
        user = response.context['user']
        self.assertFalse(user.is_authenticated)
        print("TEST LOGOUT OK\n")

# =============================== TEST CASE MODELS ============================== #
class TestModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            id=1,
            username='unittest3',
            first_name='Unit',
            last_name='Test',
            email='unittest@gmail.com',
            password='teste123456'
        )
        print(self.user1.username, self.user1.first_name, self.user1.last_name,self.user1.email, self.user1.password)
        print("TESTE MODEL USER OK\n") 

    def test_profile_model(self):
        self.profile1 = UserProfile.objects.create(
            user                 = self.user1,
            profile_age_prf      = 24,
            profile_loc_prf      = 'Rio de Janeiro - RJ',
            profile_weight_prf   = 74.2,
            profile_height_prf   = 178,
            profile_allergy_prf  = 'Nenhum',
            profile_blood_prf    = '-O',
            profile_desease_prf  = 'Nenhum',
            profile_diet_prf     = 'Ovolactovegetariano',
            profile_surgery_prf  = 'Nenhum',
            profile_exerc_prf    = 'Musculação',
            slug = 'profile-1'
        )
        print(self.profile1.user, self.profile1.profile_age_prf, self.profile1.profile_loc_prf,
        self.profile1.profile_weight_prf, self.profile1.profile_height_prf, self.profile1.profile_allergy_prf,
        self.profile1.profile_blood_prf, self.profile1.profile_desease_prf,self.profile1.profile_diet_prf, 
        self.profile1.profile_surgery_prf, self.profile1.profile_exerc_prf)
        print("TESTE MODEL PERFIL OK\n") 

    def test_medic_model(self):
        self.medication1 = UserMedication.objects.create(
            user                 = self.user1,
            medication_name_med  = 'Paracetamol',
            dosis_name_med       = '30 ml/l',
            init_date_med        = '2020-10-25',
            end_date_med         = '2020-10-25',
            time_med             = '07:00:00',
            slug                 = 'medication-1'
        )
        print(self.medication1.user, self.medication1.medication_name_med, self.medication1.dosis_name_med, self.medication1.init_date_med,
        self.medication1.end_date_med, self.medication1.time_med)
        print("TESTE MODEL MEDICAMENTO OK") 
 

    def test_trip_model(self):
        self.trip1 = UserTrip.objects.create(
            user             = self.user1,
            trip_country_trp = 'França',
            init_date_trp    = '2020-10-15',
            end_date_trp     = '2020-10-15',
            slug             = 'trip-1'
        )
        print(self.trip1.user, self.trip1.trip_country_trp, self.trip1.init_date_trp, self.trip1.end_date_trp) 
        print("TESTE MODEL VIAGENS OK") 


    def test_vaccine_model(self):
        self.vaccine1 = UserVaccine.objects.create(
            user             = self.user1,
            vaccine_name_vac = 'Sarampo',
            vaccine_date_vac = '2020-10-02',
            slug             = 'vaccine-1'      
        )
        print(self.vaccine1.user, self.vaccine1.vaccine_name_vac, self.vaccine1.vaccine_date_vac)
        print("TESTE MODEL VACINAS OK") 

    def test_diet_model(self):
        self.diet1 = UserDiet.objects.create(
            user            = self.user1,
            diet_include    = 'Falafel; Hummus;',
            diet_date_diet  = '2020-10-05',
            meal            = 'Almoço',
            slug            = 'diet-1'
        )
        print(self.diet1.user, self.diet1.diet_include, self.diet1.diet_date_diet, self.diet1.meal)
        print("TESTE MODEL DIETA OK") 

    def test_Appoint_model(self):
        self.appoint1 = UserAppoint.objects.create(
            user                = self.user1,
            appoint_espec_apt   = 'Dermatologista',
            appoint_date_apt    = '2020-10-05',
            appoint_time_apt    = '14:30:00',
            appoint_nmed_apt    = 'Fabiana Santina',
            appoint_credenc_apt = 'CRM 2486-SP',
            slug                = 'appoint-1'
        )
        print(self.appoint1.user, self.appoint1.appoint_espec_apt, self.appoint1.appoint_date_apt, self.appoint1.appoint_time_apt,
        self.appoint1.appoint_nmed_apt, self.appoint1.appoint_credenc_apt)
        print("TESTE MODEL AGENDAMENTO OK") 
