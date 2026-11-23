hari_pertama:{"keju","tepung","garam","gula","coklat"}
hari_kedua:{"garam","gula","coklat","kecap"}
#menggabungkan kedua set
A = {"keju","tepung","garam","gula","coklat"}
B = {"garam","gula","coklat","kecap"}
C = A.union(B)
print("Hasil penggabungan kedua set:", C)
#menambahkan elemen baru ke dalam set
B = {"garam","gula","coklat","kecap"}
B.add("keju")
print("Hasil penambahan elemen baru ke dalam set B:", B)
#mencari elemen yang sama pada kedua set
A = {"keju","tepung","garam","gula","coklat"}
B = {"garam","gula","coklat","kecap"}
D = A.intersection(B)
print("Hasil pencarian elemen yang sama pada kedua set:", D)
#mencari barang yang di beli pada hari pertama tetapi tidak dibeli pada hari kedua
A = {"keju","tepung","garam","gula","coklat"}
B = {"garam","gula","coklat","kecap"}
E = A.difference(B)
print("Hasil pencarian barang yang dibeli pada hari pertama tetapi tidak dibeli pada hari kedua:", E)
#mengahapus elemen pada set
A = {"keju","tepung","garam","gula","coklat"}
F = A.remove("garam")
print("Hasil penghapusan elemen 'garam' pada set A:", A)
#mencari barang yang dibeli pada hari kedua tetapi tidak dibeli pada hari pertama
A = {"keju","tepung","garam","gula","coklat"}
B = {"garam","gula","coklat","kecap"}
G = B.difference(A)
print("Hasil pencarian barang yang dibeli pada hari kedua tetapi tidak dibeli pada hari pertama:", G)
#menampilkan semua barang yang dibeli pada hari pertama
print("Barang yang dibeli pada hari pertama:", A)
#menampilkan semua barang yang dibeli pada hari kedua
print("Barang yang dibeli pada hari kedua:", B)
