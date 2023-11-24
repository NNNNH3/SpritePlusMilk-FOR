from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('logout', views.logout_user, name='logout'),
    path('cr_profile', views.create_profile, name='cr_profile'),

]
