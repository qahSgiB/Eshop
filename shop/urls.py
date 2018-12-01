from django.urls import path

from . import views



app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('product/<slug:name>/', views.product, name='product'),
    path('product/<slug:name>/<slug:style>/', views.product, name='product'),
    path('buy/<slug:name>/<slug:style>/', views.buy, name='buy'),
    path('pay/<slug:name>/<slug:style>/', views.buy, name='buy'),
]
