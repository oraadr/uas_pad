import datetime
from tkinter import messagebox

class KasirController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        self.view.btn_login.config(command=self.proses_login)
        self.view.btn_tambah.config(command=self.proses_tambah_barang)
        self.view.btn_bayar.config(command=self.proses_pembayaran)
        self.view.cmb_produk['values'] = self.model.get_produk_list()
        
        self.update_jam_digital()

    def proses_login(self):
        username = self.view.ent_username.get()
        password = self.view.ent_password.get()
        if username == "admin" and password == "kasir123":
            self.view.show_dashboard()
        else:
            self.view.lbl_login_error.config(text="Username atau Password Salah!")

    def update_jam_digital(self):
        waktu_sekarang = datetime.datetime.now().strftime("%H:%M:%S")
        self.view.lbl_jam.config(text=waktu_sekarang)
        self.view.after(1000, self.update_jam_digital)

    def proses_tambah_barang(self):
        produk_dipilih = self.view.cmb_produk.get()
        jumlah_str = self.view.ent_jumlah.get()
        if not produk_dipilih:
            messagebox.showwarning("Peringatan", "Silakan pilih produk terlebih dahulu!")
            return
        try:
            jumlah = int(jumlah_str)
            if jumlah <= 0: raise ValueError
        except ValueError:
            messagebox.showwarning("Peringatan", "Jumlah beli harus angka bulat > 0!")
            return
            
        keranjang_terbaru = self.model.tambah_ke_keranjang(produk_dipilih, jumlah)
        for row in self.view.tree.get_children():
            self.view.tree.delete(row)
        for item in keranjang_terbaru:
            self.view.tree.insert('', 'end', values=(item['nama'], f"Rp {item['harga']}", item['jumlah'], f"Rp {item['subtotal']}"))
        self.view.lbl_total.config(text=f"TOTAL: Rp {self.model.hitung_total()}")

    def proses_pembayaran(self):
        total_belanja = self.model.hitung_total()
        if total_belanja == 0:
            messagebox.showwarning("Peringatan", "Keranjang masih kosong!")
            return
        bayar_str = self.view.ent_bayar.get()
        try:
            bayar = int(bayar_str)
            if bayar < total_belanja:
                messagebox.showerror("Error", "Uang tidak cukup!")
                return
        except ValueError:
            messagebox.showwarning("Peringatan", "Input harus berupa angka!")
            return
            
        kembalian = bayar - total_belanja
        nama_file_struk = self.model.simpan_struk_txt(bayar, kembalian)
        messagebox.showinfo("Sukses", f"Kembalian: Rp {kembalian}\nStruk dicetak ke:\n{nama_file_struk}")
        
        self.model.kosongkan_keranjang()
        for row in self.view.tree.get_children():
            self.view.tree.delete(row)
        self.view.lbl_total.config(text="TOTAL: Rp 0")
        self.view.ent_bayar.delete(0, 'end')
        self.view.ent_jumlah.delete(0, 'end')
        self.view.ent_jumlah.insert(0, "1")