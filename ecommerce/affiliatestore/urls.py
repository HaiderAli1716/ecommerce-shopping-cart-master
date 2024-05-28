from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    # Home
   path("", views.index, name="Home"),
   path("store1/<id>/", views.store1, name="store"),
   path("categories/", views.category, name="Categories"),
   path("about/", views.about, name="Categories"),

]