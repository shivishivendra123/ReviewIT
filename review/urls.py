from django.urls import path
from .views import create,login,logout,homepage,add_service_form
from .views import myservice,admin_login,auth,admin_home
from .views import reject_service,accept_service

urlpatterns = [
    path('',create),
    path('login',login),
    path('homepage',homepage),
    path('logout',logout),
    path('add_service_form',add_service_form),
    path('myservice/<int:id>',myservice),
    path('admin_login',admin_login),
    path('auth',auth),
    path('admin_home', admin_home),

    path('accept_service', accept_service),
    path('reject_service', reject_service),
]
