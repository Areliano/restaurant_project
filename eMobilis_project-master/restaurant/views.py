from django.shortcuts import render, redirect

from .models import Restaurant, Customer, Aboutpage, Homepage, Stories, Chefs, Ourmenu, Happy, Testimony, Aboutend, Contact, Footer

from django.utils import timezone

from django.http import HttpResponse


# from restaurant.models import Homepage


# Create your views

def index(request):
    index = Homepage.objects.all()
    chefs = Chefs.objects.all()
    breakfasts = Ourmenu.objects.all()
    about = Aboutpage.objects.all()
    menu = Ourmenu.objects.all()
    happy = Happy.objects.all()
    testimony = Testimony.objects.all()
    footer = Footer.objects.all()
    context = {"index": index, "chefs": chefs, "breakfast": breakfasts, "footer":footer, "about":about, "menu":menu, "happy":happy, "testimony":testimony, "footer":footer }
    return render(request, 'index.html', context)


def stories(request):
    stories = Stories.objects.all()
    footer = Footer.objects.all()
    return render(request, 'blog.html', {"index": index, "footer":footer})


def about(request):
    about = Aboutpage.objects.all
    happy = Happy.objects.all()
    testimony = Testimony.objects.all()
    aboutend = Aboutend.objects.all()
    chefs = Chefs.objects.all()
    footer = Footer.objects.all()
    return render(request, "about.html", {"link": "about", "about": about, "footer":footer, "happy":happy, "testimony":testimony, "aboutend":aboutend, "chefs": chefs})


def blog(request):
    stories = Stories.objects.all()
    footer = Footer.objects.all()
    return render(request, "blog.html", {"stories": stories, "footer":footer})


# def blog-single(request):
#  return render(request, "blog-single.html", {"link":"blog-single"})


def contact(request):
    contact = Contact.objects.all()
    footer = Footer.objects.all()
    return render(request, "contact.html", {"contact": contact, "footer":footer})


# def index(request):
#     return render(request, "index.html", {"link":"index"})


def menu(request):
    menu = Ourmenu.objects.all()
    footer = Footer.objects.all()
    return render(request, "menu.html", {"menu": menu, "footer":footer})


def reservation(request):
    footer = Footer.objects.all()
    return render(request, "reservation.html", {"link": "reservation", "footer":footer })


def booked(request):
    customers = Customer.objects.all()
    footer = Footer.objects.all()
    return render(request, "booked.html", {"link": "booked", "data": customers, "footer":footer})


def dropdown(request):
    return render(request, "dropdown.html", {"link": "dropdown"})


def delete(request, id):
    satisfied_customer = Customer.objects.get(id=id)

    satisfied_customer.delete()
    footer = Footer.objects.all()

    return render(request, 'booked.html', {"footer":footer})


def insertdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        person = request.POST.get('person')

        Customer1 = Customer(name=name, email=email, phone=phone, date=date, time=time, person=person)
        Customer1.save()
        return redirect("/booked")

    return redirect("/booked")


def edit(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        person = request.POST.get('person')

        satisfied_customer = Customer.objects.get(id=id)

        satisfied_customer.name = name
        satisfied_customer.email = email
        satisfied_customer.phone = phone
        satisfied_customer.datetime = date
        satisfied_customer.time = time
        satisfied_customer.person = person

        satisfied_customer.save()
    satisfied_customer = Customer.objects.get(id=id)

    #   customers = Customer.objects.all()


    return render(request, 'edit.html', {'Customer': satisfied_customer})
    return redirect("/booked")


# get.request.POST['name']

#    return render(request, 'booked.html')


def dummy(request):
    chefs = Chefs.objects.all()
    # breakfasts = Ourmenu.objects.all()
    context = {"chefs": chefs}
    return render(request, 'dummy.html', context)

def footer(request):
    footer = Footer.objects.all()
    return render(request, 'common.html', {"footer":footer})
