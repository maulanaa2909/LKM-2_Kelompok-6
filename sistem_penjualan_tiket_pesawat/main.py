from sistem_pesawat import Penerbangan

print("=" * 80)
print("                        SISTEM RESERVASI TIKET PESAWAT")
print("=" * 80)

penerbangan = Penerbangan(
    kode          = "GA-401",
    tujuan        = "Jakarta - Bali",
    harga_ekonomi = 500_000,
    stok_ekonomi  = 30,
    harga_bisnis  = 1_000_000,
    stok_bisnis   = 20,
)

penerbangan.cek_tiket()

penerbangan.tambah_tiket("ekonomi", 20)
penerbangan.tambah_tiket("bisnis", 10)

penerbangan.cek_tiket()

penerbangan.jual_tiket("bisnis", 5)
penerbangan.jual_tiket("ekonomi", 30)

penerbangan.cek_tiket()

print(f"\n{'─'*80}")
print("  Selesai.")
print(f"{'─'*80}\n")