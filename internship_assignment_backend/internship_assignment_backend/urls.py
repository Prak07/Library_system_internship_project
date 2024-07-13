from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",include("authentication.urls")),
    path("",include("library_management.urls")),
]