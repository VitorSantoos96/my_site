from django.urls import path
from site_django.views import home, registrer, login, forget_pasword


urlpatterns = [
    path('', home), # home page / sing in
    path('registrer/', registrer), # Page of registrer
    path('login/', login), # Page of login
    path('forget_pasword/', forget_pasword), # forget pasword
]