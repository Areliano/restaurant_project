from django.db import models

from django.utils import timezone



# Create your models here.

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



class Table(models.Model):
    number = models.IntegerField(unique=True)  # Table number
    seats = models.IntegerField()  # Number of seats
    available = models.BooleanField(default=True)  # Table availability

    def __str__(self):
        return f"Table {self.number} - {'Available' if self.available else 'Booked'}"



from django.core.validators import RegexValidator
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(r'^[A-Za-z ]+$', message="Name can only contain letters and spaces.")]
    )

    email = models.EmailField(unique=True)  # ✅ Ensure each email can only have one reservation

    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be exactly 10 digits.")]
    )

    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    person = models.IntegerField()
    table = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - Table {self.table.number if self.table else 'Not Assigned'}"



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
    stock = models.PositiveIntegerField(default=10)  # ✅ Track available stock

    def __str__(self):
        return f"{self.foodname} - Stock: {self.stock}"

#from django.db import models
#from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Order(models.Model):
    menu_item = models.ForeignKey("Ourmenu", on_delete=models.CASCADE)  # Ensure "Ourmenu" is defined
    quantity = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")]
    )
    order_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """✅ Validate stock availability before saving the order."""
        if self.pk is None:  # Ensures validation runs only for new orders
            if self.menu_item.stock < self.quantity:
                raise ValidationError(f"Order cannot be placed. {self.menu_item.foodname} is out of stock.")

    def save(self, *args, **kwargs):
        """✅ Deduct stock only when order is valid and prevent accidental overwrites."""
        self.clean()  # Validate before saving

        super().save(*args, **kwargs)  # ✅ First, save order before modifying stock

        # ✅ Deduct stock only for new orders
        self.menu_item.stock -= self.quantity
        self.menu_item.save()

    def __str__(self):
        return f"Order for {self.menu_item.foodname} - {self.quantity} items"


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



