# Create your models here.
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Homepage(models.Model):
    heading = models.CharField(max_length=500, default='heading')
    description = models.TextField(max_length=3000, default='description')
    text1 = models.CharField(max_length=500, default='text1')
    text2 = models.CharField(max_length=500, default='text2')
    text3 = models.CharField(max_length=500, default='text3')
    btn = models.CharField(max_length=20, default='button')
    heading2 = models.CharField(max_length=500, default='heading')
    description2 = models.TextField(max_length=3000, default='description')
    text4 = models.CharField(max_length=500, default='text1')
    text5 = models.CharField(max_length=500, default='text2')
    text6 = models.CharField(max_length=500, default='text3')
    btn2 = models.CharField(max_length=20, default='button')
    background_image1 = models.ImageField(upload_to='homepage', default='homepage.jpg')
    background_image = models.ImageField(upload_to='homepage', default='homepage.jpg')
    img1 = models.ImageField(upload_to='homepage', default='homepage.jpg')
    img2 = models.ImageField(upload_to='homepage', default='homepage.jpg')
    img3 = models.ImageField(upload_to='homepage', default='homepage.jpg')

    def __str__(self):
        return self.heading

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} - {self.seats} seats ({'Available' if self.available else 'Booked'})"

class Reservation(models.Model):  # Changed from Customer to Reservation to avoid confusion
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[A-Za-z ]+$', message="Name can only contain letters and spaces.")]
    )
    email = models.EmailField()
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be exactly 10 digits.")]
    )
    date = models.DateField()
    time = models.TimeField()
    person = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f"{self.name} - {self.date} {self.time} (Table {self.table.number if self.table else 'None'})"

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=2)


class Aboutpage(models.Model):
    heading = models.CharField(max_length=500, default='hading')
    welcome = models.CharField(max_length=500, default='welcome')
    description = models.TextField(max_length=3000, default='description')
    special = models.CharField(max_length=500, default='specialmenu')
    text1 = models.CharField(max_length=500, default='text1')
    text2 = models.CharField(max_length=500, default='text2')
    text3 = models.CharField(max_length=500, default='text3')
    img1 = models.ImageField(upload_to='aboutpage', default='homepage.jpg')
    img2 = models.ImageField(upload_to='aboutpage', default='homepage.jpg')
    img3 = models.ImageField(upload_to='aboutpage', default='homepage.jpg')

    def __str__(self):
        return self.heading


class Stories(models.Model):
    name = models.CharField(max_length=500, default='text1')
    date = models.CharField(max_length=500, default='text2')
    text1 = models.TextField(max_length=500, default='text3')
    image = models.ImageField(upload_to='blog', default='blog.jpg')


    def __str__(self):
        return self.name


class Chefs(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    role = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='chefs')
    twitter = models.CharField(max_length=500, blank=False, null=False)
    facebook = models.CharField(max_length=500, blank=False, null=False)
    instagram = models.CharField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.name

from django.core.exceptions import ValidationError

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Ourmenu(models.Model):
    category_options = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('winecard', 'Winecard'),
        ('drinks', 'Drinks')
    ]

    foodname = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(max_length=50, choices=category_options, default='dinner')
    foodimage = models.ImageField(upload_to='ourmenu')
    description = models.CharField(max_length=200, blank=False, null=False)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.foodname} - Stock: {self.stock}"


#from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.db.models import Sum, Count, Avg

class Order(models.Model):
    menu_item = models.ForeignKey('Ourmenu', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    client_name = models.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[A-Za-z ]+$', "Name can only contain letters and spaces")]
    )
    client_phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', "Phone number must be 10 digits.")]
    )
    client_email = models.EmailField(
        max_length=100,
        validators=[EmailValidator()],
        help_text="We'll send your order confirmation here",
        blank=True,  # Allow blank temporarily for migration
        default="no-email@example.com"  # Temporary default for existing records
    )
    order_date = models.DateTimeField(auto_now_add=True)
    special_requests = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        help_text="Any special instructions for your order"
    )

    class Meta:
        ordering = ['-order_date']
        verbose_name = 'Customer Order'
        verbose_name_plural = 'Customer Orders'

    def clean(self):
        """Validate stock availability and order details before saving."""
        if not self.pk:  # Only validate for new orders
            if self.menu_item.stock < self.quantity:
                raise ValidationError(
                    f"Cannot place order. Only {self.menu_item.stock} {self.menu_item.foodname} available."
                )
            if self.quantity < 1:
                raise ValidationError("Quantity must be at least 1")
            if not self.client_email or self.client_email == "no-email@example.com":
                raise ValidationError("Please provide a valid email address")

    def save(self, *args, **kwargs):
        """Save order with validation and stock management."""
        self.full_clean()  # Runs clean() and all field validations

        is_new = not self.pk
        super().save(*args, **kwargs)

        if is_new:
            self.menu_item.stock -= self.quantity
            self.menu_item.save()

    def __str__(self):
        return (
            f"Order #{self.id}: {self.quantity}x {self.menu_item.foodname} "
            f"for {self.client_name} ({self.order_date.strftime('%Y-%m-%d %H:%M')})"
        )

    @property
    def total_price(self):
        """Calculate total price for the order."""
        return self.quantity * self.menu_item.price

    @classmethod
    def get_revenue_report(cls, start_date, end_date):
        """Generate revenue report between two dates."""
        return cls.objects.filter(
            order_date__date__gte=start_date,
            order_date__date__lte=end_date
        ).aggregate(
            total_orders=Count('id'),
            total_revenue=Sum(models.F('menu_item__price') * models.F('quantity')),
            average_order_value=Avg(models.F('menu_item__price') * models.F('quantity'))
        )



class Happy(models.Model):
    text1 = models.CharField(max_length=500, default='text1')
    text2 = models.CharField(max_length=500, default='text2')
    text3 = models.CharField(max_length=500, default='text3')
    text4 = models.CharField(max_length=500, default='text4')
    image = models.ImageField(upload_to='ourmenu', default='happy.jpg')

    def __str__(self):
        return self.text1

class Testimony(models.Model):
    text1 = models.TextField(max_length=500, default='text1')
    name1 = models.CharField(max_length=500, default='text2')
    position1 = models.CharField(max_length=500, default='text3')
    image1 = models.ImageField(upload_to='testimony', default='testimony.jpg')

    text2 = models.TextField(max_length=500, default='text1')
    name2 = models.CharField(max_length=500, default='text2')
    position2 = models.CharField(max_length=500, default='text3')
    image2 = models.ImageField(upload_to='testimony', default='testimony.jpg')

    text3 = models.TextField(max_length=500, default='text1')
    name3 = models.CharField(max_length=500, default='text2')
    position3 = models.CharField(max_length=500, default='text3')
    image3 = models.ImageField(upload_to='testimony', default='testimony.jpg')

    text4 = models.TextField(max_length=500, default='text1')
    name4 = models.CharField(max_length=500, default='text2')
    position4 = models.CharField(max_length=500, default='text3')
    image4 = models.ImageField(upload_to='testimony', default='testimony.jpg')

    text5 = models.TextField(max_length=500, default='text1')
    name5 = models.CharField(max_length=500, default='text2')
    position5 = models.CharField(max_length=500, default='text3')
    image5 = models.ImageField(upload_to='testimony', default='testimony.jpg')

    background = models.ImageField(upload_to='testimony', default='testimony.jpg')

    def __str__(self):
        return self.name1



class Aboutend(models.Model):
    name = models.CharField(max_length=500, default='text1')
    heading = models.CharField(max_length=500, default='text2')
    text = models.TextField(max_length=2000, default='text3')
    btn = models.CharField(max_length=20, default='button')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=500, default='text1')
    address = models.CharField(max_length=500, default='text1')
    phone = models.CharField(max_length=500, default='text1')
    email = models.CharField(max_length=500, default='text1')
    website = models.CharField(max_length=500, default='text1')

    def __str__(self):
        return self.name

class Footer(models.Model):
    heading = models.CharField(max_length=500, default='text1')
    about = models.CharField(max_length=500, default='text1')
    twitter = models.CharField(max_length=500, blank=False, null=False)
    facebook = models.CharField(max_length=500, blank=False, null=False)
    instagram = models.CharField(max_length=500, blank=False, null=False)
    open_days = models.CharField(max_length=500, default='text1')
    newsletter = models.CharField(max_length=500, default='text1')
    image1 = models.ImageField(upload_to='footer', default='testimony.jpg')
    image2 = models.ImageField(upload_to='footer', default='testimony.jpg')
    image3 = models.ImageField(upload_to='footer', default='testimony.jpg')
    image4 = models.ImageField(upload_to='footer', default='testimony.jpg')
    image5 = models.ImageField(upload_to='footer', default='testimony.jpg')
    image6 = models.ImageField(upload_to='footer', default='testimony.jpg')

    def __str__(self):
        return self.heading



