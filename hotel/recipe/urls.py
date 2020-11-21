from django.urls import path
from . import views

app_name = 'recipe'
urlpatterns = [
    path('',views.items_name, name='item_name'),
    path('<int:id>/', views.item_details, name='details'),
    path('add_item/', views.add_item, name='add_item')
]