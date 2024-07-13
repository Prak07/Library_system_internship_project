from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('get_book/',get_book,name="login") ,
    path('add_book/',Add_book,name="login") ,
    path('delete_book/<book_id>/',delete_book,name="login") ,
    path('edit_book/<book_id>/',edit_book,name="login") ,
    path('get_book/<book_id>/',look_for_book,name="login") ,
    path('search/',search,name="login") ,
    
]