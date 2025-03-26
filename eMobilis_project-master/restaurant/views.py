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


def order(request):
    """Displays all orders placed by customers."""
    all_orders = Order.objects.all().order_by("-order_date")  # Orders sorted by latest first
    return render(request, "order.html", {"orders": all_orders})

def menu(request):
    """Fetches menu items and footer details and renders the menu page."""
    menu = Ourmenu.objects.all()
    return render(request, "menu.html", {"menu": menu})

def place_order(request):
    """Handles food ordering while checking stock availability."""
    if request.method == "POST":
        menu_item_id = request.POST.get("menu_item")
        quantity = request.POST.get("quantity", 1)  # Default to 1 if not provided

        try:
            quantity = int(quantity)  # Convert quantity to integer safely
            menu_item = Ourmenu.objects.get(id=menu_item_id)  # Fetch menu item

            # ✅ Check stock availability before placing order
            if menu_item.stock < quantity:
                messages.error(request, f"❌ Sorry, {menu_item.foodname} is out of stock.")
                return redirect("menu")  # Redirect back to the menu page

            # ✅ Save the order (stock deduction is handled in Order model)
            order = Order.objects.create(
                menu_item=menu_item,
                quantity=quantity,
                customer_name=request.POST.get("customer_name"),
                customer_phone=request.POST.get("customer_phone"),
            )

            # ✅ Check for low stock warning
            if menu_item.stock <= 5:  # Adjust threshold as needed
                messages.warning(request, f"⚠️ Warning: {menu_item.foodname} is running low on stock!")

            messages.success(request, "✅ Your order has been placed successfully!")
            return redirect("order")  # Redirect to order list page

        except Ourmenu.DoesNotExist:
            messages.error(request, "❌ Menu item not found.")
        except ValueError:
            messages.error(request, "❌ Invalid quantity. Please enter a valid number.")
        except Exception as e:
            messages.error(request, f"❌ An unexpected error occurred: {str(e)}")

    return redirect("menu")  # Redirect back to the menu if something goes wrong


from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone

from django.http import JsonResponse
#from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, Table
import json

def reservation(request):
    """ Fetches only available tables and renders the reservation page. """
    tables = Table.objects.filter(available=True)
    return render(request, "reservation.html", {"tables": tables})


@csrf_exempt  # ✅ Allows testing without CSRF token (Remove in production)
def insertdata(request):
    """ Handles reservation submission while allowing existing emails to proceed with a message. """
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            time = request.POST.get('time')
            person = request.POST.get('person')

            if not all([name, email, phone, date, time, person]):
                return render(request, "reservation.html", {"error": "All fields are required!"})

            # ✅ Check if the email is already used for a reservation
            existing_customer = Customer.objects.filter(email=email).first()
            if existing_customer:
                return render(request, "reservation.html", {
                    "message": f"Your reservation is already confirmed for {existing_customer.date} at {existing_customer.time}."
                })

            # ✅ Find an available table that fits the group size
            person = int(person)  # Ensure person count is an integer
            table = Table.objects.filter(seats__gte=person, available=True).first()

            if table:
                # ✅ Create the reservation
                customer = Customer.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    date=date,
                    time=time,
                    person=person,
                    table=table
                )

                # ✅ Mark the table as booked
                table.available = False
                table.save()

                return redirect("/booked")  # ✅ Redirect to booking confirmation page
            else:
                return render(request, "reservation.html", {"error": "No available tables for the selected size."})

        except ValidationError as e:
            return render(request, "reservation.html", {"error": str(e)})
        except Exception as e:
            return render(request, "reservation.html", {"error": f"Something went wrong: {str(e)}"})

    return redirect("/booked")  # ✅ Redirect if accessed via GET


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
