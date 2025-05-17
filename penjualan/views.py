from django.shortcuts import render, redirect
from .models import Barang, Transaksi, DetailBarang
from django.contrib import messages
from datetime import datetime

# Inisialisasi session keranjang
def get_keranjang(request):
    return request.session.get('keranjang', [])


def keranjang(request):
    keranjang = get_keranjang(request)
    return render(request, 'keranjang.html', {
        "keranjang": keranjang
    })


def index(request):
    if request.method == 'POST':
        nama_barang = request.POST.get('nama_barang')
        quantity = int(request.POST.get('quantity'))
        tanggal = request.POST.get('tanggal')

        try:
            barang = Barang.objects.get(name__iexact=nama_barang)
        except Barang.DoesNotExist:
            messages.error(request, 'Barang tidak ditemukan di daftar barang!')
            return redirect('index')

        keranjang = request.session.get('keranjang', [])
        keranjang.append({
            'name': barang.name,
            'price': barang.price,
            'category': barang.category,
            'quantity': quantity,
            'date': tanggal
        })
        request.session['keranjang'] = keranjang
        messages.success(request, 'Barang berhasil ditambahkan ke keranjang!')
        return redirect('index')

    barang_list = Barang.objects.all()
    return render(request, 'index.html', {'barang_list': barang_list})

# Hapus item dari keranjang (berdasarkan index list)
def hapus_item_keranjang(request, index):
    keranjang = get_keranjang(request)
    try:
        keranjang.pop(index)
        request.session['keranjang'] = keranjang
        messages.success(request, "Item berhasil dihapus.")
    except IndexError:
        messages.error(request, "Gagal menghapus item.")
    return redirect('keranjang')



def edit_keranjang(request, index):
    keranjang = request.session.get('keranjang', [])

    if index < 0 or index >= len(keranjang):
        messages.error(request, 'Item tidak ditemukan!')
        return redirect('keranjang')

    item = keranjang[index]

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        date = request.POST.get('date')

        keranjang[index]['quantity'] = quantity
        keranjang[index]['date'] = date
        request.session['keranjang'] = keranjang
        messages.success(request, 'Item berhasil diubah!')
        return redirect('keranjang')

    return render(request, 'edit_keranjang.html', {'item': item, 'index': index})



# Simpan isi keranjang sebagai transaksi ke database
def simpan_transaksi(request):
    keranjang = get_keranjang(request)
    if not keranjang:
        messages.error(request, "Keranjang kosong!")
        return redirect('keranjang')

    transaksi = Transaksi.objects.create(date=datetime.today())
    for item in keranjang:
        barang = Barang.objects.get(name=item['name'])
        DetailBarang.objects.create(
            transaksi=transaksi,
            barang=barang,
            quantity=item['quantity'],
            date_transaksi=item['date']
        )

    # Kosongkan keranjang setelah transaksi
    request.session['keranjang'] = []
    messages.success(request, "Transaksi berhasil disimpan.")
    return redirect('list_transaksi')

# Menampilkan semua transaksi
def list_transaksi(request):
    transaksi = Transaksi.objects.all().order_by('-date')
    return render(request, 'transaksi.html', {
        "transaksi": transaksi
    })
