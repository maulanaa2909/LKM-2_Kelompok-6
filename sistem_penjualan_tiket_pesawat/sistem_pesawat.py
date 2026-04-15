class TiketPesawat:
    def __init__ (self, namapenumpang,hargatiket, jumlah_tiket):
        self.namapenumpang = namapenumpang
        self.hargatiket = hargatiket
        self.jumlah_tiket = jumlah_tiket
        
    def tambah_tiket(self, jumlah):
        self.jumlah_tiket += jumlah
        print(f'Jumlah tiket yang tersedia: {self.jumlah_tiket}')
    
    
    def jual_tiket(self, jumlah):
       if self.jumlah_tiket >= jumlah:
           self.jumlah_tiket -= jumlah
           total_akhir = self.hargatiket * jumlah
           print(f"Pembelian berhasil!. harga yang harus dibayar :Rp{total_akhir:,} tiket yang tersisa {self.jumlah_tiket}")
       else:
           print("Tiket tidak cukup untuk")