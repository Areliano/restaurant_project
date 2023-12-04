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


class Customer(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=10, default='dd/mm/yyyy')
    time = models.TimeField(max_length=50, default=timezone.now)
    person = models.IntegerField()

    def __str__(self):
        return self.name


#class Menu(models.Model):
 #   name = models.CharField(max_length=50, default='name')
  #  heading = models.CharField(max_length=50, default='heading')
    #BREAKFAST
   # text1 = models.CharField(max_length=500, default='text1')
    #text2 = models.CharField(max_length=500, default='text2')
    #text3 = models.CharField(max_length=500, default='text3')
#    text4 = models.CharField(max_length=500, default='text4')
#    text5 = models.CharField(max_length=500, default='text5')
 #   text6 = models.CharField(max_length=500, default='text6')
  #  text7 = models.CharField(max_length=500, default='text4')
   # text8 = models.CharField(max_length=500, default='text5')
    #text9 = models.CharField(max_length=500, default='text6')
#    text10 = models.CharField(max_length=500, default='text4')
 #   text11 = models.CharField(max_length=500, default='text5')
  #  text12 = models.CharField(max_length=500, default='text6')
   # text16 = models.CharField(max_length=500, default='text4')
    #text17 = models.CharField(max_length=500, default='text5')
#    text18 = models.CharField(max_length=500, default='text6')
 #   text19 = models.CharField(max_length=500, default='text4')
  #  text20 = models.CharField(max_length=500, default='text5')
   # text21 = models.CharField(max_length=500, default='text6')

  #  def __str__(self):
  #      return self.name




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


class Ourmenu(models.Model):
    category_options = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('Dessert', 'Dessert'),
        ('Winecard', 'Winecard'),
        ('Drinks', 'Drinks')
    ]

    foodname = models.CharField(max_length=50, blank=False, null=False)
    category = models.CharField(max_length=50, choices=category_options, default='Dinner')
    foodimage = models.ImageField(upload_to='ourmenu')
    description = models.CharField(max_length=200, blank=False, null=False)
    price = models.PositiveIntegerField()


    def __str__(self):
        return self.foodname

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



