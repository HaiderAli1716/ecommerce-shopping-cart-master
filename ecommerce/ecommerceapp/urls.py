from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('profile',views.profile,name="profile"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),


]
