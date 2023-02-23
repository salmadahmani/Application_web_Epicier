from django.contrib import admin
from .models import Clients, ClientsAdmin, Produits, ProduitsAdmin, Credits

admin.site.register(Clients, ClientsAdmin)
admin.site.register(Produits, ProduitsAdmin)
admin.site.register(Credits, )
# Register your models here.
