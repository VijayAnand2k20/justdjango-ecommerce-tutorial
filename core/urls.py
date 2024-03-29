from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', views.checkout, name='checkout_page'),
    path('product/', views.product, name='product_page'),
]
