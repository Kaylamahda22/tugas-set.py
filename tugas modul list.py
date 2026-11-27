penumpang = ["william","kate","anderson","jame","mady"]
rute = ["jakarta","ciamis","kebumen","yogyakarta"]
#membuat list baru untuk menampung keseluruhan penumpang
keseluruhan_penumpang = []
print("Daftar penumpang:", penumpang)
#menambahkan penumpang baru ke dalam list
penumpang.append("jones")
print("Daftar penumpang setelah penambahan:", penumpang)
#mengganti data penumpang pada index tertentu
penumpang[2] = "Grace"
print("Daftar penumpang setelah perubahan:", penumpang)
#mencari anggota dari list penumpang
member = "Thompson" in penumpang
print(member)
#mengurutkan list sesuai abjad
penumpang.sort()
print("Daftar penumpang setelah diurutkan:", penumpang)
#menampilkan penumpang yang sudah sampai yogyakarta menggunakan for/while
print("Daftar penumpang yang telah sampai di yogyakarta:")
for penumpang in penumpang:
    if penumpang in rute:
        print(penumpang)
        #mengosongkan list penumpang
        penumpang.clear()
        print("Daftar penumpang setelah dikosongkan:", penumpang)
