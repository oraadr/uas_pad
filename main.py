# Import class dari sub-folder masing-masing
from models.kasir_model import KasirModel
from views.kasir_view import KasirView
from controllers.kasir_controller import KasirController

if __name__ == "__main__":
    # 1. Inisialisasi Model dari folder models
    model = KasirModel()
    
    # 2. Inisialisasi View dari folder views
    view = KasirView()
    
    # 3. Ikat hubungan di Controller dari folder controllers
    app = KasirController(model, view)
    
    # 4. Jalankan aplikasi utama
    view.mainloop()