
from django.urls import path

from . import views
from .views import place_order, order

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path("place_order/", place_order, name="place_order"),
    path('reservation/', views.reservation, name='reservation'),
    path('insertdata/', views.insertdata, name='insertdata'),
    path('booked/', views.booked, name='booked'),
    path("order/", order, name="order"),
    #path('delete/<int:id>/', views.delete, name='delete'),
   # path('edit/<int:id>/', views.edit, name='edit'),
    path('cancel/<int:id>/', views.cancel_reservation, name='cancel_reservation'),

]