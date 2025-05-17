from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('keranjang/', views.keranjang, name='keranjang'),
    path('keranjang/hapus/<int:index>/', views.hapus_item_keranjang, name='hapus_item_keranjang'),
    path('keranjang/edit/<int:index>/', views.edit_keranjang, name='edit_keranjang'),
    path('keranjang/simpan/', views.simpan_transaksi, name='simpan_transaksi'),
    path('transaksi/', views.list_transaksi, name='list_transaksi'),
]

