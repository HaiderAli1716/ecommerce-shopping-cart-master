from django.shortcuts import render
from django.http import HttpResponse
from affiliatestore.models import Offer, stores,Carousel,categories


# Create your views here.
def index(request):
    carousel = Carousel.objects.all()
    cardsdata=stores.objects.all()
    astores=stores.objects.filter(name__startswith='a')
    bstores=stores.objects.filter(name__startswith='b')
    cstores=stores.objects.filter(name__startswith='c')
    dstores=stores.objects.filter(name__startswith='d')
    estores=stores.objects.filter(name__startswith='e')
    fstores=stores.objects.filter(name__startswith='f')
    data={
        'carousel' : carousel,
        'cardsdata':cardsdata,
        'astores':astores,
        'bstores':bstores,
        'cstores':cstores,
        'dstores':dstores,
        'estores':estores,
        'fstores':fstores,        
    }
    return render(request, 'affiliate/affhom.html', data)

def store1(request,id):
    images=stores.objects.all()
    cardsdata=stores.objects.filter(id=id)
    products=Offer.objects.filter(storename=id)
   
    data={
        'cardsdata':cardsdata,
        'cardelement':products,
        'images':images,
        
    }
    return render(request, 'affiliate/store1.html', data)

def category(request):
    filterid=stores.objects.all()
    products=categories.objects.all()
    categoryid=request.GET.get('category')
    if categoryid:
        filterid=stores.objects.filter(category=categoryid)
    else:
        filterid=stores.objects.all()  
 
    data={
        
        'products':products,
        'filterid':filterid,
        
    }
    return render(request, 'affiliate/categories.html', data)

def about(request):
    
  return render(request, 'affiliate/about.html')