from django.urls import path
from .views import create,login,logout,homepage,add_service_form
from .views import myservice,admin_login,auth,main
urlpatterns = [
    path('',main),
    path('create',create),
    path('login',login),
    path('homepage',homepage),
    path('logout',logout),
    path('add_service_form',add_service_form),
    path('myservice/<int:id>',myservice),
    path('admin_login',admin_login),
    path('auth',auth)
]
