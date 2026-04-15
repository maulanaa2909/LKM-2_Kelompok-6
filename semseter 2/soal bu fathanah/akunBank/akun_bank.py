class AkunBank:
    def __init__(self, nomor, pemilik, saldo_awal):
        self.nomor = nomor 
        self.pemilik = pemilik
        self.saldo = saldo_awal
        self.riwayat = []
    
    def cek_saldo(self):
        print(f"Saldo {self.pemilik}: Rp{self.saldo}")
    
    def tarik_tunai(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penarikan harus lebih besar dari 0!")
            return
            
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            pesan = f"{self.pemilik} menarik Rp{jumlah}"
            print(pesan)
            self.riwayat.append(pesan)  
        else:
            pesan = f"Saldo tidak cukup untuk penarikan Rp{jumlah} oleh {self.pemilik}"
            print("Saldo tidak cukup!")
            self.riwayat.append(pesan)  
    
    def transfer(self, tujuan, jumlah):
        if jumlah <= 0:
            print("Jumlah transfer harus lebih besar dari 0!")
            return
            
        biaya_admin = 2500
        total_biaya = jumlah + biaya_admin
        
        if self.saldo >= total_biaya:
            self.saldo -= total_biaya
            tujuan.saldo += jumlah
            pesan = f"Transfer Rp{jumlah} ke {tujuan.pemilik} Berhasil! Biaya admin Rp{biaya_admin}"
            print(pesan)
            self.riwayat.append(pesan)  
        else:
            pesan = f"Transfer Gagal: Saldo tidak cukup untuk transfer Rp{jumlah} + admin Rp{biaya_admin}"
            print("Transfer Gagal: Saldo tidak cukup.")
            self.riwayat.append(pesan)  
    
    def tampilkan_riwayat(self):
        """Method baru untuk menampilkan semua riwayat transaksi"""
        print(f"\n=== Riwayat Transaksi {self.pemilik} ===")
        if not self.riwayat:
            print("Belum ada transaksi.")
        else:
            for i, transaksi in enumerate(self.riwayat, 1):
                print(f"{i}. {transaksi}")
        print("=" * 35)