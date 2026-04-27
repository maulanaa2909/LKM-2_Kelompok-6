from tkinter import W


class TiketPesawat:
    def __init__(self, jenis, harga, jumlah, tujuan):
        self.jenis = jenis
        self.harga = harga
        self.jumlah = jumlah
        self.tujuan = tujuan
        self.terjual = 0
 
    def tambah_tiket(self, jumlah):
        self.jumlah += jumlah
        print(f"    Ditambahkan {jumlah} tiket. Stok {self.jenis}: {self.jumlah} kursi")
 
    def jual_tiket(self, jumlah):
        if self.jumlah >= jumlah:
            self.jumlah -= jumlah
            self.terjual += jumlah
            total = self.harga * jumlah
            print(f"    Pembelian berhasil!")
            print(f"    Jenis    : {self.jenis.capitalize()}")
            print(f"    Jumlah   : {jumlah} tiket")
            print(f"    Total    : Rp{total:,.0f}")
            print(f"    Terjual  : {self.terjual} tiket (total)")
            print(f"    Sisa     : {self.jumlah} kursi")
        else:
            print(f"    Tiket tidak cukup!")
            print(f"    Diminta  : {jumlah} tiket")
            print(f"    Tersedia : {self.jumlah} kursi")
 
    def cek_tiket(self):
        print(f"  • {self.jenis.capitalize():<12} | Harga: Rp{self.harga:>12,.0f} | Terjual: {self.terjual:>3} | Stok: {self.jumlah:>3} kursi")
 
 
class Penerbangan:
    def __init__(self, kode, tujuan, harga_ekonomi, stok_ekonomi, harga_bisnis, stok_bisnis):
        self.kode = kode
        self.tujuan = tujuan
        self.ekonomi = TiketPesawat("ekonomi", harga_ekonomi, stok_ekonomi, tujuan)
        self.bisnis  = TiketPesawat("bisnis",  harga_bisnis,  stok_bisnis,  tujuan)
 
    def _header(self, judul):
        print(f"\n{'─'*80}")
        print(f"  {self.kode} │ {self.tujuan} │ {judul}")
        print(f"{'─'*80}")
 
    def tambah_tiket(self, jenis, jumlah):
        self._header(f"Tambah Tiket {jenis.capitalize()}")
        tiket = self.ekonomi if jenis == "ekonomi" else self.bisnis
        tiket.tambah_tiket(jumlah)
 
    def jual_tiket(self, jenis, jumlah):
        self._header(f"Pembelian Tiket {jenis.capitalize()}")
        tiket = self.ekonomi if jenis == "ekonomi" else self.bisnis
        tiket.jual_tiket(jumlah)
 
    def cek_tiket(self):
        self._header("Stok Tiket")
        self.ekonomi.cek_tiket()
        self.bisnis.cek_tiket()
 
 # capitalize() fungsinya buat bikin huruf pertama jadi besar (ini Maul bukan ai)