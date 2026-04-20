class TiketPesawat:
    def __init__(self, nama_penerbangan, hargatiket, jumlah_tiket):
        self.nama_penerbangan = nama_penerbangan
        self.hargatiket = hargatiket
        self.jumlah_tiket = jumlah_tiket

    def tambah_tiket(self, jumlah):
        self.jumlah_tiket += jumlah
        print(f"Jumlah tiket yang tersedia: {self.jumlah_tiket}")

    def jual_tiket(self, jumlah):
        if self.jumlah_tiket >= jumlah:
            self.jumlah_tiket -= jumlah
            total_akhir = self.hargatiket * jumlah
            print(f"Pembelian berhasil! Harga yang harus dibayar: Rp{total_akhir:,} | Tiket tersisa: {self.jumlah_tiket}")
        else:
            print(f"Tiket tidak cukup! Diminta: {jumlah}, Tersedia: {self.jumlah_tiket}")

    def cek_tiket(self):
        print(f"Sisa tiket {self.nama_penerbangan}: {self.jumlah_tiket}")
        return self.jumlah_tiket