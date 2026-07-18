# KasirMini UMKM (Modern Edition)

Aplikasi desktop *Point of Sales* (Kasir) sederhana berbasis Python dan Tkinter yang dirancang untuk membantu digitalisasi pencatatan transaksi pada usaha mikro. Aplikasi ini dibangun menggunakan arsitektur **Model-View-Controller (MVC)** yang memisahkan folder data, tampilan, dan logika bisnis agar kode program menjadi rapi, modular, dan mudah dikembangkan.

## ✨ Fitur Utama
*   **Sistem Autentikasi Login:** Mengamankan aplikasi dari akses yang tidak sah sebelum masuk ke dashboard utama.
*   **Jam Digital Real-Time:** Menampilkan waktu lokal secara presisi di bagian header untuk memantau waktu operasional toko.
*   **Manajemen Keranjang Belanja:** Memilih produk lewat dropdown (Combobox), menginput jumlah barang, kalkulasi subtotal otomatis, dan menampilkan daftar belanjaan dalam tabel dinamis (Treeview).
*   **Otomatisasi Struk (.txt):** Mencetak riwayat transaksi langsung menjadi file teks eksternal sebagai bukti fisik transaksi sekaligus cadangan data agar tidak tercecer.
*   **Desain UI Modern:** Mengadopsi visual minimalis gaya flat card, entri modern, serta efek hover pada tombol utama untuk kenyamanan pengguna.

---

## 📂 Struktur Repositori (MVC Pattern)
```text
nama-lengkap-proyek-akhir/
│
├── models/
│   ├── __init__.py
│   └── kasir_model.py          # Mengolah data produk, keranjang, & cetak struk
│
├── views/
│   ├── __init__.py
│   └── kasir_view.py           # Mengatur seluruh komponen antarmuka (UI) Tkinter
│
├── controllers/
│   ├── __init__.py
│   └── kasir_controller.py     # Otak aplikasi (Menghubungkan Model dan View)
│
├── NamaLengkap_NIM_ProyekAkhir.pdf   # Dokumen Proposal Ide & Mockup Aplikasi
└── main.py                     # Entry point utama untuk menjalankan aplikasi