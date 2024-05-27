from django.contrib import admin
from django.urls import path
from myapp import views

admin.site.site_header = "Rohan Admin"
admin.site.site_title = "Rohan Admin Portal"
admin.site.index_title = "Welcome to Rohan Khan Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact")

]
