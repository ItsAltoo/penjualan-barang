from django.db import models


class Barang(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)


    def harga(self):
        return f"{self.price:,}"
    
    def __str__(self):
        return self.name


class Transaksi(models.Model):
    date = models.DateField()

    def __str__(self):
        return f"Transaksi {self.id} - {self.date}"


class DetailBarang(models.Model):
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE)
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    
    def total_harga(self):
        total = self.barang.price * self.quantity
        return f"{total:,}"

    def __str__(self):
        return f"{self.barang.name} - {self.quantity} pcs total : {self.total_harga()}"