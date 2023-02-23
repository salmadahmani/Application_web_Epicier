from django.db import models
from django.contrib import admin

class Clients(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    list_filter = ('name',)
    search_fields = ['name', 'phone']

class Produits(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class ProduitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('name',)


class Credits(models.Model):
    STATUS = (('Pending', 'Pending'), ('Delivered', 'Delivered'))
    client = models.ForeignKey(Clients, null=True, on_delete=models.SET_NULL)
    produit = models.ForeignKey(Produits, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)




