
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Recipe
# Create your views here.
def items_name(request):
    item_list = Recipe.objects.all()
    #template = loader.get_template('items/items_name.html')
    context = {
        'item_list': item_list
    }
    #output = ','.join([q.item_name for q in item_list])
    #return HttpResponse(template.render(context,request))
    return render(request,'items/items_name.html',context)

def item_details(request ):
    #details_list = get_object_or_404(Recipe,pk=1)
    details_list = Recipe.objects.all().values('item_name','ingredients','process')
    context = {
        'details_list': details_list,
        'detals_list' : details_list,
        'details_list': details_list

    }
    #return HttpResponse(render(context,request))
    return render(request,'items/details.html',context)

def add_item(request):
    add_item = get_object_or_404(Recipe, pk =None)
    #return HttpResponseRedirect (reverse('recipe:item_name'))
    return render(request,'items/add_item.html',add_item)
