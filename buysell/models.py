from django.db import models
from django.urls import reverse
# multiple select field contrib
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# tag optionality field contrib
from taggit.managers import TaggableManager

# Product category such as shoes, clothes, tablets, etc...
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Product model
class Product(models.Model):
    # types of products: buy, sell, exchange
    BUY_SELL_EXCHANGE = (
        ('buy', 'Buy'),
        ('sell', 'Sell'),
        ('exchange', 'Exchange'),
    )

    # fieldsets = (
    #     (None, {'Wants': ('tags')})
    # )

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = MultiSelectField(choices=BUY_SELL_EXCHANGE, verbose_name="Product Type")
    tags = TaggableManager(verbose_name="Wants", help_text="Enter keywords for your wants. Use a comma to separate the wants.")
    description = models.TextField(verbose_name="Enter description and contact infos")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # where to redirect after model submit
    def get_absolute_url(self):
        return reverse('buysell:index')

    def __str__(self):
        return self.name

class User_info(models.Model):
    customerID = models.CharField(max_length=255)
    customerName = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('buysell:index')

    def __str__(self):
        return self.customerName

class Recommender(models.Model):
    customerID = models.ForeignKey(User_info, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    productName = models.CharField(max_length=255)
    sales = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField
    reviewRating = models.DecimalField(max_digits=10, decimal_places=2)
    clicks = models.IntegerField
    timeSpent = models.DecimalField(max_digits=10, decimal_places=2)

