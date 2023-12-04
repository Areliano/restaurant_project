
from django.urls import path

from . import views

#app_name = "rest"

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    # path('blog-single', views.blog-single, name='blog-single'),
    path('contact', views.contact, name='contact'),
    path('menu', views.menu, name='menu'),
    path('reservation', views.reservation, name='reservation'),
    path('booked', views.booked, name='booked'),
    path('dropdown', views.dropdown, name='dropdown'),
    path('delete/<id>', views.delete, name='delete'),
    path('insertdata', views.insertdata, name='insertdata'),
    path('edit/<id>', views.edit, name='edit')

]