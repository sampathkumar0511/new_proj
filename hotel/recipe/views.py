
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

def item_details(request, id):
    #details_list = get_object_or_404(Recipe)
    details_list = get_object_or_404(Recipe,pk=id)
    #return HttpResponse(render(context,request))
    return render(request,'items/details.html', {'details_list':details_list})

def add_item(request):
    if request.method == 'POST':
        Recipe.objects.create(
            item_name = request.POST["item_name"],
            ingredients = request.POST["ingredients"],
            process = request.POST["process"],
        )
        return HttpResponseRedirect(reverse('recipe:item_name'))
    return render(request, 'items/add_item.html')
