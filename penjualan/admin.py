from django.contrib import admin
from .models import Barang, Transaksi, DetailBarang
# Register your models here.

admin.site.register(Barang)
admin.site.register(Transaksi)
admin.site.register(DetailBarang)
