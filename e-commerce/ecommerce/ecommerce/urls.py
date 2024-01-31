from django.contrib import admin
from django.urls import path
from commerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('product/<int:id>/', views.product_list, name='product_list'),
    path('about_us/', views.about_us, name='about_us'),
    path('category/', views.category, name='category'),
]
