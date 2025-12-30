
from django.contrib import admin
from django.urls import path
from Consultorio_Voluntad_De_Dios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('informacion/', views.informacion, name='informacion'),
    path("login/", views.login_view, name="login"),
]