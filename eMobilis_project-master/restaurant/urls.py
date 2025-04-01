from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import place_order, order, register_view, login_view, logout_view

urlpatterns = [
    path('', login_required(views.index), name='index'),  # Protected index view
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('menu/', views.menu, name='menu'),
    path("place_order/", place_order, name="place_order"),
    path("order/", order, name="order"),
    path('reservation/', views.reservation, name='reservation'),
    path('insertdata/', views.insertdata, name='insertdata'),
    path('booked/', views.booked, name='booked'),
    path('cancel/<int:id>/', views.cancel_reservation, name='cancel_reservation'),
    path('edit/<int:id>/', views.edit_reservation, name='edit_reservation'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]