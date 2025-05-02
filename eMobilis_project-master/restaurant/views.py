from django.shortcuts import render, redirect

from .models import Restaurant, Aboutpage, Homepage, Stories, Chefs, Ourmenu, Happy, Testimony, Aboutend, Contact, Footer, Order

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')

# Add all your other view functions below (about, blog, contact, menu, etc.)
# Make sure to add @login_required decorator to views that need authentication

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



from django.utils import timezone
from datetime import datetime, time as datetime_time
from .models import Table, Reservation
import logging


def insertdata(request):
    if request.method == 'POST':
        try:
            # Get and sanitize form data
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip().lower()
            phone = request.POST.get('phone', '').strip()
            date = request.POST.get('date', '').strip()
            time = request.POST.get('time', '').strip()
            person = request.POST.get('person', '0').strip()
            table_id = request.POST.get('table', '').strip()

            # Validate required fields
            if not all([name, email, phone, date, time, person, table_id]):
                messages.error(request, "All fields are required!")
                return redirect('reservation')

            # Convert and validate person count
            try:
                person = int(person)
                if person < 1:
                    raise ValueError("At least 1 person required")
            except ValueError:
                messages.error(request, "Please enter a valid number of people")
                return redirect('reservation')

            # Validate date and time
            try:
                reservation_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
                # Make the datetime timezone aware
                reservation_datetime = timezone.make_aware(reservation_datetime)

                if reservation_datetime < timezone.now():
                    messages.error(request, "Cannot book for past dates/times")
                    return redirect('reservation')

                # Validate business hours (8AM to 10PM)
                opening_time = datetime_time(8, 0)
                closing_time = datetime_time(22, 0)
                if not (opening_time <= reservation_datetime.time() <= closing_time):
                    messages.error(request, "We're only open from 8:00 AM to 10:00 PM")
                    return redirect('reservation')

            except ValueError:
                messages.error(request, "Invalid date or time format")
                return redirect('reservation')

            # Check if table exists and is available
            table = get_object_or_404(Table, id=table_id)

            if not table.available:
                messages.error(request, f"Table {table.number} is already booked")
                return redirect('reservation')

            # Check if table has enough seats
            if table.seats < person:
                messages.warning(
                    request,
                    f"Table {table.number} only has {table.seats} seats (you selected {person}). "
                    "Please choose a larger table."
                )
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

            # Success message with reservation details
            messages.success(
                request,
                f"Reservation confirmed for {reservation_datetime.strftime('%A, %B %d at %I:%M %p')} "
                f"(Table {table.number} for {person} people). Confirmation sent to {email}"
            )

            return redirect('booked')

        except Exception as e:
            messages.error(
                request,
                "An error occurred while processing your reservation. "
                "Please try again or contact us if the problem persists."
            )
            logger.error(f"Reservation error: {str(e)}", exc_info=True)
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


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import datetime, time as datetime_time
from .models import Reservation, Table
import logging


def edit_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)

    # Get available tables plus the currently reserved table
    available_tables = (Table.objects.filter(available=True) |
                        Table.objects.filter(id=reservation.table.id)).distinct().order_by('number')

    if request.method == 'POST':
        try:
            # Get and sanitize form data
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip().lower()
            phone = request.POST.get('phone', '').strip()
            date = request.POST.get('date', '').strip()
            time = request.POST.get('time', '').strip()
            person = request.POST.get('person', '0').strip()
            new_table_id = request.POST.get('table', '').strip()

            # Validate required fields
            if not all([name, email, phone, date, time, person, new_table_id]):
                messages.error(request, "All fields are required!")
                return redirect('edit_reservation', id=id)

            # Convert and validate person count
            try:
                person = int(person)
                if person < 1:
                    raise ValueError("At least 1 person required")
            except ValueError:
                messages.error(request, "Please enter a valid number of people")
                return redirect('edit_reservation', id=id)

            # Validate date and time
            try:
                reservation_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
                # Make the datetime timezone aware
                reservation_datetime = timezone.make_aware(reservation_datetime)

                if reservation_datetime < timezone.now():
                    messages.error(request, "Cannot book for past dates/times")
                    return redirect('edit_reservation', id=id)

                # Validate business hours (8AM to 10PM)
                opening_time = datetime_time(8, 0)
                closing_time = datetime_time(22, 0)
                if not (opening_time <= reservation_datetime.time() <= closing_time):
                    messages.error(request, "We're only open from 8:00 AM to 10:00 PM")
                    return redirect('edit_reservation', id=id)

            except ValueError:
                messages.error(request, "Invalid date or time format")
                return redirect('edit_reservation', id=id)

            # Get the new table
            new_table = get_object_or_404(Table, id=new_table_id)

            # Check if new table is available (unless it's the same table)
            if new_table != reservation.table and not new_table.available:
                messages.error(request, f"Table {new_table.number} is already booked")
                return redirect('edit_reservation', id=id)

            # Check if new table has enough seats
            if new_table.seats < person:
                messages.warning(
                    request,
                    f"Table {new_table.number} only has {new_table.seats} seats "
                    f"(you selected {person}). Please choose a larger table."
                )
                return redirect('edit_reservation', id=id)

            # Handle table changes
            old_table = reservation.table
            if new_table != old_table:
                # Release old table
                old_table.available = True
                old_table.save()

                # Reserve new table
                new_table.available = False
                new_table.save()

            # Update reservation
            reservation.name = name
            reservation.email = email
            reservation.phone = phone
            reservation.date = date
            reservation.time = time
            reservation.person = person
            reservation.table = new_table
            reservation.save()

            messages.success(
                request,
                f"Reservation updated successfully for {reservation_datetime.strftime('%A, %B %d at %I:%M %p')} "
                f"(Table {new_table.number} for {person} people)."
            )
            return redirect('booked')

        except Exception as e:
            messages.error(
                request,
                "An error occurred while updating your reservation. "
                "Please try again or contact us if the problem persists."
            )
            logger.error(f"Reservation update error: {str(e)}", exc_info=True)
            return redirect('edit_reservation', id=id)

    return render(request, "edit.html", {
        "reservation": reservation,
        "tables": available_tables,
        "min_date": timezone.now().strftime('%Y-%m-%d')  # For date input min attribute
    })

def dummy(request):
    chefs = Chefs.objects.all()
    # breakfasts = Ourmenu.objects.all()
    context = {"chefs": chefs}
    return render(request, 'dummy.html', context)

def footer(request):
    footer = Footer.objects.all()
    return render(request, 'common.html', {"footer":footer})


from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime, timedelta
from django.shortcuts import render


def is_admin(user):
    return user.is_superuser


@login_required
@user_passes_test(is_admin)
def reports(request):
    # Date ranges with optional custom date filtering
    today = timezone.now().date()

    # Get filter parameters from request
    start_date = request.GET.get('start_date', today.strftime('%Y-%m-%d'))
    end_date = request.GET.get('end_date', today.strftime('%Y-%m-%d'))

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except (ValueError, TypeError):
        start_date = today
        end_date = today

    # Calculate previous periods for comparison
    period_days = (end_date - start_date).days + 1
    previous_start = start_date - timedelta(days=period_days)
    previous_end = start_date - timedelta(days=1)

    # Fixed period calculations (daily, weekly, monthly)
    last_7_days = today - timedelta(days=7)
    this_month_start = today.replace(day=1)

    # Order reports for current period
    current_orders = Order.objects.filter(
        order_date__date__gte=start_date,
        order_date__date__lte=end_date
    )
    previous_orders = Order.objects.filter(
        order_date__date__gte=previous_start,
        order_date__date__lte=previous_end
    )

    # Fixed period order counts
    daily_orders = Order.objects.filter(order_date__date=today).count()
    weekly_orders = Order.objects.filter(order_date__date__gte=last_7_days).count()
    monthly_orders = Order.objects.filter(order_date__date__gte=this_month_start).count()

    # Revenue calculations
    current_revenue = current_orders.aggregate(
        total=Sum('menu_item__price')
    )['total'] or 0
    previous_revenue = previous_orders.aggregate(
        total=Sum('menu_item__price')
    )['total'] or 0

    # Fixed period revenues
    daily_revenue = Order.objects.filter(
        order_date__date=today
    ).aggregate(total=Sum('menu_item__price'))['total'] or 0

    weekly_revenue = Order.objects.filter(
        order_date__date__gte=last_7_days
    ).aggregate(total=Sum('menu_item__price'))['total'] or 0

    monthly_revenue = Order.objects.filter(
        order_date__date__gte=this_month_start
    ).aggregate(total=Sum('menu_item__price'))['total'] or 0

    # Calculate percentage changes
    revenue_change = 0
    if previous_revenue != 0:
        revenue_change = ((current_revenue - previous_revenue) / previous_revenue) * 100

    # Reservation reports
    current_reservations = Reservation.objects.filter(
        date__gte=start_date,
        date__lte=end_date
    ).count()
    previous_reservations = Reservation.objects.filter(
        date__gte=previous_start,
        date__lte=previous_end
    ).count()

    # Fixed period reservation counts
    daily_reservations = Reservation.objects.filter(date=today).count()
    weekly_reservations = Reservation.objects.filter(date__gte=last_7_days).count()
    monthly_reservations = Reservation.objects.filter(date__gte=this_month_start).count()

    # Calculate percentage change for reservations
    reservation_change = 0
    if previous_reservations != 0:
        reservation_change = ((current_reservations - previous_reservations) / previous_reservations) * 100

    # Inventory status
    low_stock_items = Ourmenu.objects.filter(stock__lte=5).order_by('stock')
    out_of_stock_items = Ourmenu.objects.filter(stock=0)

    # Popular items
    popular_items = Ourmenu.objects.annotate(
        order_count=Count('order')
    ).order_by('-order_count')[:5]

    context = {
        # Fixed period data
        'daily_orders': daily_orders,
        'weekly_orders': weekly_orders,
        'monthly_orders': monthly_orders,
        'daily_revenue': daily_revenue,
        'weekly_revenue': weekly_revenue,
        'monthly_revenue': monthly_revenue,
        'daily_reservations': daily_reservations,
        'weekly_reservations': weekly_reservations,
        'monthly_reservations': monthly_reservations,

        # Custom period data
        'current_orders_count': current_orders.count(),
        'current_reservations_count': current_reservations,
        'current_revenue': current_revenue,
        'revenue_change': revenue_change,
        'reservation_change': reservation_change,
        'period_days': period_days,

        # Inventory data
        'low_stock_items': low_stock_items,
        'out_of_stock_items': out_of_stock_items,
        'popular_items': popular_items,

        # Dates
        'today': today.strftime('%Y-%m-%d'),
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
    }

    return render(request, 'reports.html', context)