# Panduan Penggunaan Aplikasi Penjualan Barang

Aplikasi ini memungkinkan pengguna untuk membeli barang, mengelola keranjang, serta menyimpan transaksi. Berikut adalah cara-cara menggunakan aplikasi.

## Persyaratan
1. Pastikan [Django](https://www.djangoproject.com/) telah terinstal sesuai dengan [requirements.txt](penjualan_barang/requirements.txt).
2. Pastikan Node.js dan npm telah terinstal untuk menjalankan Tailwind CSS pada [theme/static_src](penjualan_barang/theme/static_src/).

## Menjalankan Aplikasi
1. Lakukan migrasi database:
    ```sh
    python manage.py migrate
    ```
2. (Opsional) Buat akun admin untuk mengelola backend:
    ```sh
    python manage.py createsuperuser
    ```
3. Jalankan server:
    ```sh
    python manage.py runserver
    ```
4. Buka browser dan akses [http://localhost:8000](http://localhost:8000).

## Cara Menggunakan Aplikasi

### Halaman Utama (Index)
- **Form Beli Barang**:  
  Mengisi form untuk menambahkan barang ke keranjang:
  - **Nama Barang**: Pastikan barang tersebut sudah ada di database.
  - **Quantity**: Jumlah barang yang ingin dibeli.
  - **Date**: Tanggal pembelian.
  - Klik tombol **"Tambah ke Keranjang"**.
  
  Halaman ini juga menampilkan daftar barang yang tersedia.

- **Navigasi**:
  - Tautan menuju *Keranjang*: Menampilkan barang yang sudah dimasukkan ke keranjang.
  - Tautan menuju *Hasil Transaksi*: Menampilkan transaksi yang telah disimpan ke database.

### Halaman Keranjang ([templates/keranjang.html](templates/keranjang.html))
- Menampilkan daftar barang yang ada di keranjang.
- Setiap item memiliki opsi:
  - **Edit**: Ubah detail item (quantity atau tanggal) pada halaman [Edit Keranjang](templates/edit_keranjang.html).
  - **Hapus**: Menghapus item dari keranjang.
- Terdapat tombol **"Simpan Transaksi"** untuk menyimpan semua isi keranjang sebagai transaksi ke database melalui [views.simpan_transaksi](penjualan/views.py).

### Halaman Edit Keranjang ([templates/edit_keranjang.html](templates/edit_keranjang.html))
- Halaman ini digunakan untuk mengubah jumlah (quantity) dan tanggal suatu item pada keranjang.
- Setelah melakukan perubahan, klik **"Simpan Perubahan"** untuk memperbarui item tersebut di sesi.

### Halaman Transaksi ([templates/transaksi.html](templates/transaksi.html))
- Menampilkan daftar transaksi yang sudah tersimpan.
- Setiap transaksi menampilkan detail barang yang dibeli (nama, kategori, harga, quantity, dan tanggal).

## Pengaturan Tailwind CSS
1. Pindah ke direktori [theme/static_src](penjualan_barang/theme/static_src/):
    - Untuk menghasilkan file CSS yang sudah minify, jalankan:
      ```sh
      npm run build
      ```
    - Untuk pengembangan dengan watch mode:
      ```sh
      npm run dev
      ```
   CSS hasil build akan ditempatkan di theme/static/css/dist.

## Tips
- Pastikan data barang telah ditambahkan ke database agar form pembelian berjalan dengan benar.
- Sebelum melakukan transaksi, periksa kembali isi keranjang melalui halaman *Keranjang* dan lakukan edit jika diperlukan.

Ikuti panduan ini agar Anda dan pengguna lain dapat menggunakan aplikasi dengan mudah.