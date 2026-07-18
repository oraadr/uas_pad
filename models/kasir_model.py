import datetime

class KasirModel:
    def __init__(self):
        self.daftar_produk = {
            "Kopi Susu Gula Aren": 15000,
            "Roti Bakar Cokelat": 12000,
            "Kentang Goreng": 10000,
            "Es Teh Manis": 5000
        }
        self.keranjang = []

    def get_produk_list(self):
        return list(self.daftar_produk.keys())

    def get_harga_produk(self, nama_produk):
        return self.daftar_produk.get(nama_produk, 0)

    def tambah_ke_keranjang(self, nama_produk, jumlah):
        if nama_produk in self.daftar_produk and jumlah > 0:
            harga = self.daftar_produk[nama_produk]
            subtotal = harga * jumlah
            for item in self.keranjang:
                if item['nama'] == nama_produk:
                    item['jumlah'] += jumlah
                    item['subtotal'] += subtotal
                    return self.keranjang
            self.keranjang.append({
                'nama': nama_produk, 'harga': harga, 'jumlah': jumlah, 'subtotal': subtotal
            })
        return self.keranjang

    def hitung_total(self):
        return sum(item['subtotal'] for item in self.keranjang)

    def kosongkan_keranjang(self):
        self.keranjang = []

    def simpan_struk_txt(self, bayar, kembalian):
        waktu_sekarang = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nama_file = f"Struk_{waktu_sekarang}.txt"
        with open(nama_file, "w") as f:
            f.write("=== STRUK KASIR MINI UMKM ===\n")
            f.write(f"Tanggal: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("-----------------------------\n")
            for item in self.keranjang:
                f.write(f"{item['nama']} x{item['jumlah']} : Rp {item['subtotal']}\n")
            f.write("-----------------------------\n")
            f.write(f"TOTAL      : Rp {self.hitung_total()}\n")
            f.write(f"BAYAR      : Rp {bayar}\n")
            f.write(f"KEMBALIAN  : Rp {kembalian}\n")
            f.write("=============================\n")
        return nama_file