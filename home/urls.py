from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("service/", views.service, name="service"),
    path("service/<str:service_type>/", views.service_detail, name="service-detail"),
    path("contact/", views.contact, name="contact"),
]
