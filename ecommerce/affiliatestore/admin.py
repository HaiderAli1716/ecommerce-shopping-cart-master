from django.contrib import admin
from affiliatestore.models import Carousel

# Register your models here.
from .models import Offer,stores,Carousel,categories

@admin.register(Offer)
class dealsadmin(admin.ModelAdmin):
    list_display=Offer.displayfields
    search_fields=Offer.searcfield


@admin.register(stores)
class storesAdmin(admin.ModelAdmin):
    list_display = ('id','name','category',)
    ordering =('name',)
    search_fields=('id','name',)
    
@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
    ordering =('name',)
    search_fields=('id','name',)
    
@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id','image','link',)
    ordering =('id',)
    search_fields=('id',)