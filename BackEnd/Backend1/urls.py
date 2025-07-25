
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/' ,views.LoginPage,name="login"),
    path('home/' ,views.HomePage,name="home"),
    path('logout/' ,views.LogoutPage,name="logout"),
    path('vote/' ,views.Voting,name="vote"),
    path('contact/' ,views.contactus,name="contact"),
]
