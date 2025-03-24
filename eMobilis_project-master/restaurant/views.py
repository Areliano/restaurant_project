from django.shortcuts import render, redirect

from .models import Restaurant, Customer, Aboutpage, Homepage, Stories, Chefs, Ourmenu, Happy, Testimony, Aboutend, Contact, Footer, Order

from django.utils import timezone

from django.http import HttpResponse
from django.contrib import messages


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


def place_order(request):
    if request.method == "POST":
        menu_item_id = request.POST.get("menu_item")
        quantity = int(request.POST.get("quantity"))
        customer_name = request.POST.get("customer_name")
        customer_phone = request.POST.get("customer_phone")

        try:
            menu_item = Ourmenu.objects.get(id=menu_item_id)

            # Check if there is enough stock
            if menu_item.stock >= quantity:
                # Reduce stock
                menu_item.stock -= quantity
                menu_item.save()

                # Save the order
                Order.objects.create(
                    menu_item=menu_item,
                    quantity=quantity,
                    customer_name=customer_name,
                    customer_phone=customer_phone
                )

                # Check for low stock warning
                if menu_item.stock <= 5:  # Adjust the threshold as needed
                    messages.warning(request, f"⚠️ Warning: {menu_item.foodname} is running low on stock!")

                messages.success(request, "✅ Order placed successfully!")
            else:
                messages.error(request, "❌ Not enough stock available!")

        except Ourmenu.DoesNotExist:
            messages.error(request, "❌ Menu item not found!")

    return redirect("menu")  # Adjust to your menu URL


from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Table
from django.utils import timezone

def reservation(request):
    tables = Table.objects.filter(available=True)  # Fetch only available tables
    return render(request, "reservation.html", {"tables": tables})

def insertdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        person = int(request.POST.get('person'))

        # Find an available table that fits the group size
        table = Table.objects.filter(seats__gte=person, available=True).first()

        if table:
            # Create the reservation
            customer = Customer(name=name, email=email, phone=phone, date=date, time=time, person=person, table=table)
            customer.save()

            # Mark the table as booked
            table.available = False
            table.save()

            return redirect("/booked")
        else:
            return render(request, "reservation.html", {"error": "No available tables for the selected size."})

    return redirect("/booked")

def booked(request):
    customers = Customer.objects.all()
    return render(request, "booked.html", {"data": customers})

def cancel_reservation(request, id):
    customer = get_object_or_404(Customer, id=id)

    # Free up the table
    if customer.table:
        table = customer.table
        table.available = True
        table.save()

    customer.delete()
    return redirect("/booked")


def dummy(request):
    chefs = Chefs.objects.all()
    # breakfasts = Ourmenu.objects.all()
    context = {"chefs": chefs}
    return render(request, 'dummy.html', context)

def footer(request):
    footer = Footer.objects.all()
    return render(request, 'common.html', {"footer":footer})
