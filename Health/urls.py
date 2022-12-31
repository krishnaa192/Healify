from django.contrib import admin
from django.urls import path
from  Health  import views
urlpatterns = [
    path("", views.Home, name="Home"),
    path("about", views.about_us, name="about_us"),
    path("gallery", views.gallery, name="gallery"),
    path("blog", views.Blogs, name="Blogs"),
    path("contact", views.contact, name="contact"),
    path("appointment", views.appointment, name="appointment"),
    path("login", views.loginUser, name="loginUser"),
    path("registration", views.registerUser, name="registerUser"),
    path("profile", views.profile, name="profile"),
    path("confirm", views.booking_cnfrm, name="booking_cnfrm"),
    path("confirm_query", views.query_confirmations, name="query_confirmations"),
    path("subscription", views.subscription, name="subscription"),
    path("subs_cnfrm", views.subscnf, name="subscnf"),
    path("login/", views.loginUser, name="loginUser"),
    path("logout/", views.logout, name="logout"),
    

]

