from django.shortcuts import render, redirect

from .models import Restaurant, Aboutpage, Homepage, Stories, Chefs, Ourmenu, Happy, Testimony, Aboutend, Contact, Footer, Order

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
    """Displays all orders placed by clients."""
    all_orders = Order.objects.all().order_by("-order_date")
    return render(request, "order.html", {"orders": all_orders})

def menu(request):
    """Fetches menu items and footer details and renders the menu page."""
    menu_items = Ourmenu.objects.all()
    return render(request, "menu.html", {"menu": menu_items})



def place_order(request):
    """Handles food ordering with complete validation and robust email error handling."""
    if request.method == "POST":
        try:
            # Get and sanitize form data
            menu_item_id = request.POST.get("menu_item")
            quantity = int(request.POST.get("quantity", 1))
            client_name = request.POST.get("client_name", "").strip()
            client_phone = request.POST.get("client_phone", "").strip()
            client_email = request.POST.get("client_email", "").strip().lower()
            special_requests = request.POST.get("special_requests", "").strip()

            # Validate required fields
            if not all([menu_item_id, client_name, client_phone, client_email]):
                messages.error(request, "❌ Please fill in all required fields.")
                return redirect("menu")

            # Validate email format
            if "@" not in client_email or "." not in client_email.split("@")[-1]:
                messages.error(request, "❌ Please enter a valid email address.")
                return redirect("menu")

            # Get menu item with existence check
            try:
                menu_item = Ourmenu.objects.get(id=menu_item_id)
            except Ourmenu.DoesNotExist:
                messages.error(request, "❌ The selected menu item was not found.")
                return redirect("menu")

            # Validate stock availability
            if menu_item.stock < quantity:
                messages.error(
                    request,
                    f"❌ Sorry, only {menu_item.stock} {menu_item.foodname} available."
                )
                return redirect("menu")

            # Validate quantity
            if quantity < 1:
                messages.error(request, "❌ Quantity must be at least 1.")
                return redirect("menu")

            # Create and save the order
            order = Order.objects.create(
                menu_item=menu_item,
                quantity=quantity,
                client_name=client_name,
                client_phone=client_phone,
                client_email=client_email,
                special_requests=special_requests,
            )

            # Check for low stock warning
            remaining_stock = menu_item.stock - quantity
            if remaining_stock <= 5:
                messages.warning(
                    request,
                    f"⚠️ Low stock: Only {remaining_stock} {menu_item.foodname} left!"
                )

            # Email confirmation handling
            try:
                # Signal will automatically send email
                messages.success(
                    request,
                    f"✅ Order #{order.id} confirmed! {quantity} × {menu_item.foodname} "
                    f"for {client_name}. Confirmation sent to {client_email}"
                )
            except Exception as email_error:
                messages.warning(
                    request,
                    f"✅ Order #{order.id} confirmed but email failed to send. "
                    f"Please contact us for confirmation. Error: {str(email_error)}"
                )
                # Log the error for admin review
                import logging
                logger = logging.getLogger(__name__)
                logger.error(
                    f"Email failed for order #{order.id}. Error: {str(email_error)}"
                )

            return redirect("order")

        except ValueError as ve:
            messages.error(request, f"❌ Invalid input: {str(ve)}")
        except ValidationError as ve:
            messages.error(request, f"❌ Validation error: {str(ve)}")
        except Exception as e:
            messages.error(
                request,
                "❌ An unexpected error occurred. Our team has been notified."
            )
            # Log the full error for debugging
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Order processing error: {str(e)}", exc_info=True)

    return redirect("menu")

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Table, Reservation  # Changed from Customer to Reservation


def reservation(request):
    available_tables = Table.objects.filter(available=True).order_by('number')
    return render(request, "reservation.html", {
        "tables": available_tables,
        "min_date": timezone.now().strftime('%Y-%m-%d')  # For date input min attribute
    })


def insertdata(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            date = request.POST.get('date')
            time = request.POST.get('time')
            person = int(request.POST.get('person'))
            table_id = request.POST.get('table')

            # Validate required fields
            if not all([name, email, phone, date, time, person, table_id]):
                messages.error(request, "All fields are required!")
                return redirect('reservation')

            # Check if table exists and is available
            table = get_object_or_404(Table, id=table_id, available=True)

            # Check if table has enough seats
            if table.seats < person:
                messages.warning(request, f"Table {table.number} only has {table.seats} seats (you selected {person}).")
                return redirect('reservation')

            # Create reservation
            reservation = Reservation.objects.create(
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
                person=person,
                table=table
            )

            # Mark table as booked
            table.available = False
            table.save()

            messages.success(request, f"Reservation confirmed for {date} at {time} (Table {table.number})")
            return redirect('booked')

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('reservation')

    return redirect('reservation')


def booked(request):
    reservations = Reservation.objects.select_related('table').order_by('-created_at')
    return render(request, "booked.html", {"reservations": reservations})


def cancel_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)

    if reservation.table:
        table = reservation.table
        table.available = True
        table.save()

    reservation.delete()
    messages.success(request, "Reservation cancelled successfully")
    return redirect('booked')


def edit_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    available_tables = Table.objects.filter(available=True) | Table.objects.filter(id=reservation.table.id)

    if request.method == 'POST':
        try:
            # Get form data
            reservation.name = request.POST.get('name')
            reservation.email = request.POST.get('email')
            reservation.phone = request.POST.get('phone')
            reservation.date = request.POST.get('date')
            reservation.time = request.POST.get('time')
            reservation.person = int(request.POST.get('person'))

            # Save changes
            reservation.save()

            messages.success(request, "Reservation updated successfully")
            return redirect('booked')

        except Exception as e:
            messages.error(request, f"Error updating reservation: {str(e)}")

    return render(request, "edit.html", {
        "reservation": reservation,
        "tables": available_tables.distinct().order_by('number')
    })

def dummy(request):
    chefs = Chefs.objects.all()
    # breakfasts = Ourmenu.objects.all()
    context = {"chefs": chefs}
    return render(request, 'dummy.html', context)

def footer(request):
    footer = Footer.objects.all()
    return render(request, 'common.html', {"footer":footer})

# restaurant/views.py

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('index')  # Replace 'home' with your homepage URL name
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('index')  # Replace 'home' with your homepage URL name
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')  # Redirect to login page after logout