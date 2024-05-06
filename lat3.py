print("LAPORAN PENJUALAN TOKO NIKO")
print("---------------------------")

Tot_hrgbrg=0.0
Kd_Barang =input("Kode Barang =  ")
Nma_Barang =input("Nama Barang =  ")
Hrg_Sat =int(input("Harga Satuan = Rp.    "))
Jml_Barang =int(input("Jumlah Barang =   "))

print("-------------------------------")
Hrg_Beli=Hrg_Sat*Jml_Barang
Tot_hrgbrg=Hrg_Beli+Tot_hrgbrg

print("total Harga Yang Dibayar =Rp.",Tot_hrgbrg)

uang_Dibayar =int(input("uang yang dibayarkan=Rp.  "))

uang_kembalian=uang_Dibayar-Tot_hrgbrg

print("Jumlah Kembalian=Rp. ",uang_kembalian)