from django.db import models
from django.contrib.auth.models import User
from datetime import date
import uuid # Required for unique book instances


class Category(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60)
    category = models.ManyToManyField('Category', related_name='products')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    brand = models.CharField(max_length=100)
    desc = models.TextField()
    image_url = models.CharField(max_length=2000, default='https://upload.wikimedia.org/wikipedia/commons/c/c2/Fujifilm_X-T100_8_Jun_2018b.jpg')

    def __str__(self):
        return self.name

class Chat(models.Model):
    text = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class ProductInstance(models.Model):
    """Model representing a specific product from catalog (e.g that can be SEWAA from the catalog)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular product across whole catalog')
    product = models.ForeignKey('Product', on_delete=models.RESTRICT)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Product availability',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.product.name})'

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
