import tkinter as tk
from tkinter import ttk

class KasirView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("KasirMini UMKM - Modern Edition")
        self.geometry("650x500")
        self.resizable(False, False)
        
        # Tema warna modern (Palette: Slate & Emerald)
        self.BG_MAIN = "#F8FAFC"       # Abu-abu sangat muda (background utama)
        self.BG_CARD = "#FFFFFF"       # Putih bersih untuk kartu login
        self.TXT_DARK = "#0F172A"      # Hitam pekat untuk teks utama
        self.TXT_MUTED = "#64748B"     # Abu-abu untuk teks sekunder/label
        self.PRIMARY = "#10B981"       # Hijau Emerald untuk tombol utama
        self.PRIMARY_HOVER = "#059669" # Hijau lebih tua saat tombol disorot
        
        self.configure(bg=self.BG_MAIN)
        
        # Container utama untuk switching halaman
        self.container = tk.Frame(self, bg=self.BG_MAIN)
        self.container.pack(fill="both", expand=True)
        
        self.init_login_frame()
        self.init_dashboard_frame()
        self.show_login()

    def init_login_frame(self):
        # Frame latar belakang halaman login
        self.login_frame = tk.Frame(self.container, bg=self.BG_MAIN)
        
        # CARD / KOTAK LOGIN UTAMA (Membuat efek melayang)
        card = tk.Frame(self.login_frame, bg=self.BG_CARD, highlightbackground="#E2E8F0", highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center", width=360, height=380)
        
        # Judul & Deskripsi Aplikasi
        tk.Label(card, text="Selamat Datang", font=("Arial", 20, "bold"), fg=self.TXT_DARK, bg=self.BG_CARD).pack(pady=(30, 2))
        tk.Label(card, text="Silakan masuk ke akun kasir Anda", font=("Arial", 10), fg=self.TXT_MUTED, bg=self.BG_CARD).pack(pady=(0, 25))
        
        # INPUT USERNAME
        lbl_user = tk.Label(card, text="USERNAME", font=("Arial", 9, "bold"), fg=self.TXT_MUTED, bg=self.BG_CARD)
        lbl_user.pack(anchor="w", padx=35, pady=(5, 2))
        
        self.ent_username = tk.Entry(card, font=("Arial", 11), bg="#F1F5F9", fg=self.TXT_DARK, 
                                     bd=0, highlightbackground="#CBD5E1", highlightthickness=1, insertbackground=self.TXT_DARK)
        self.ent_username.pack(fill="x", padx=35, ipady=8)
        
        # INPUT PASSWORD
        lbl_pass = tk.Label(card, text="PASSWORD", font=("Arial", 9, "bold"), fg=self.TXT_MUTED, bg=self.BG_CARD)
        lbl_pass.pack(anchor="w", padx=35, pady=(15, 2))
        
        self.ent_password = tk.Entry(card, show="*", font=("Arial", 11), bg="#F1F5F9", fg=self.TXT_DARK, 
                                     bd=0, highlightbackground="#CBD5E1", highlightthickness=1, insertbackground=self.TXT_DARK)
        self.ent_password.pack(fill="x", padx=35, ipady=8)
        
        # PESAN ERROR
        self.lbl_login_error = tk.Label(card, text="", fg="#EF4444", bg=self.BG_CARD, font=("Arial", 9))
        self.lbl_login_error.pack(pady=(10, 0))
        
        # TOMBOL LOGIN MODERN
        self.btn_login = tk.Button(card, text="Masuk Aplikasi", font=("Arial", 11, "bold"), 
                                   bg=self.PRIMARY, fg="white", bd=0, cursor="hand2", activebackground=self.PRIMARY_HOVER, activeforeground="white")
        self.btn_login.pack(fill="x", padx=35, pady=(15, 25), ipady=8)
        
        # Efek Hover Ringan pada Tombol Login
        self.btn_login.bind("<Enter>", lambda e: self.btn_login.config(bg=self.PRIMARY_HOVER))
        self.btn_login.bind("<Leave>", lambda e: self.btn_login.config(bg=self.PRIMARY))

    def init_dashboard_frame(self):
        self.dashboard_frame = tk.Frame(self.container, bg=self.BG_MAIN)
        
        # --- Header (Judul & Jam Digital) ---
        header_frame = tk.Frame(self.dashboard_frame, bg="#0F172A", height=55)
        header_frame.pack(fill="x", side="top")
        
        tk.Label(header_frame, text="KASIRMINI UMKM", font=("Arial", 12, "bold"), fg="white", bg="#0F172A").pack(side="left", padx=20, pady=15)
        self.lbl_jam = tk.Label(header_frame, text="00:00:00", font=("Arial", 12, "bold"), fg="#10B981", bg="#0F172A")
        self.lbl_jam.pack(side="right", padx=20, pady=15)
        
        # --- Bagian Input ---
        input_frame = tk.LabelFrame(self.dashboard_frame, text=" Input Penjualan ", padx=15, pady=10, bg=self.BG_MAIN, fg=self.TXT_DARK, font=("Arial", 9, "bold"))
        input_frame.pack(fill="x", padx=20, pady=15)
        
        tk.Label(input_frame, text="Pilih Produk:", bg=self.BG_MAIN, fg=self.TXT_DARK).grid(row=0, column=0, sticky="w", pady=5)
        self.cmb_produk = ttk.Combobox(input_frame, state="readonly", width=23)
        self.cmb_produk.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Jumlah:", bg=self.BG_MAIN, fg=self.TXT_DARK).grid(row=0, column=2, sticky="w", pady=5)
        self.ent_jumlah = tk.Entry(input_frame, width=8, bg="white", fg=self.TXT_DARK, highlightbackground="#CBD5E1", highlightthickness=1, bd=0)
        self.ent_jumlah.grid(row=0, column=3, padx=5, pady=5, ipady=3)
        self.ent_jumlah.insert(0, "1")
        
        self.btn_tambah = tk.Button(input_frame, text="Tambah", bg="#2563EB", fg="white", font=("Arial", 9, "bold"), bd=0, padx=10, cursor="hand2")
        self.btn_tambah.grid(row=0, column=4, padx=10, pady=5, ipady=3)
        
        # --- Bagian Tabel (Treeview) ---
        tabel_frame = tk.Frame(self.dashboard_frame, bg=self.BG_MAIN)
        tabel_frame.pack(fill="both", expand=True, padx=20, pady=5)
        
        # Memperbaiki visual tabel bawaan tkinter agar senada dengan tema modern
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("Arial", 9, "bold"), background="#E2E8F0", foreground=self.TXT_DARK)
        style.configure("Treeview", font=("Arial", 10), rowheight=25, fieldbackground="white")
        
        columns = ('nama', 'harga', 'jumlah', 'subtotal')
        self.tree = ttk.Treeview(tabel_frame, columns=columns, show='headings', height=6)
        self.tree.heading('nama', text='Nama Produk')
        self.tree.heading('harga', text='Harga Satuan')
        self.tree.heading('jumlah', text='Qty')
        self.tree.heading('subtotal', text='Subtotal')
        
        self.tree.column('nama', width=220)
        self.tree.column('harga', width=110, anchor="center")
        self.tree.column('jumlah', width=60, anchor="center")
        self.tree.column('subtotal', width=130, anchor="center")
        self.tree.pack(fill="both", expand=True)
        
        # --- Bagian Pembayaran ---
        bayar_frame = tk.Frame(self.dashboard_frame, pady=15, bg=self.BG_MAIN)
        bayar_frame.pack(fill="x", padx=20)
        
        self.lbl_total = tk.Label(bayar_frame, text="TOTAL: Rp 0", font=("Arial", 15, "bold"), fg="#DC2626", bg=self.BG_MAIN)
        self.lbl_total.pack(side="left")
        
        self.btn_bayar = tk.Button(bayar_frame, text="PROSES & CETAK", bg=self.PRIMARY, fg="white", font=("Arial", 10, "bold"), padx=15, bd=0, cursor="hand2")
        self.btn_bayar.pack(side="right", padx=5, ipady=5)
        
        self.ent_bayar = tk.Entry(bayar_frame, font=("Arial", 12), width=12, bg="white", fg=self.TXT_DARK, highlightbackground="#CBD5E1", highlightthickness=1, bd=0)
        self.ent_bayar.pack(side="right", padx=5, ipady=4)
        tk.Label(bayar_frame, text="Bayar (Rp):", bg=self.BG_MAIN, fg=self.TXT_DARK, font=("Arial", 10, "bold")).pack(side="right", padx=5)

    def show_login(self):
        self.dashboard_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.login_frame.pack_forget()
        self.dashboard_frame.pack(fill="both", expand=True)