from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('jobsearch', views.jobsearch_home, name="jobsearch-home"),
    path('jobs', views.jobs, name="jobs"),
    path('new_job', views.new_job, name="new-job"),
    path('job/<str:job_id>', views.job, name="job"),
    path('delete_job/<job_id>', views.delete_job, name="delete-job"),
    path('clients', views.clients, name="clients"),
    path('new_client', views.new_client, name="new-client"),
    path('delete_client/<client_id>', views.delete_client, name="delete-client"),
    path('update_client/<client_id>', views.update_client, name="update-client"),
    path('client/<str:client_id>', views.client, name="client"),
    path('guests', views.guests, name="guests"),
    path('new_guest', views.new_guest, name="new-guest"),
    path('guest/<str:guest_id>', views.guest, name="guest"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit-profile"),
    path('change_password', views.change_password, name="change-password"),
] 