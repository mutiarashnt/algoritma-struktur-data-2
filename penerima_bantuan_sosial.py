print('DATA PENERIMA BANSOS APRIL 2024')
print('-' *52)
nama = str(input('Masukkan Nama Pendaftar : '))
umur = int(input('Masukkan Umur : '))
pekerjaan = str(input('Masukkan Pekerjaan : '))
penghasilan = int(input('Masukkan Penghasilan : '))
jumlah_anggota_keluarga = int(input('Masukkan Jumlah Anggota Keluarga yang Ditanggung : '))

print('=' *52)
kategori_pekerjaan = ['Buruh','Petani','Nelayan','Pedagang'] 
if (pekerjaan in kategori_pekerjaan and penghasilan <=1000000 and umur > 25 and jumlah_anggota_keluarga >= 3):
    print(nama,'memenuhi kriteria penerima bansos')
else:
    print(nama,'tidak memenuhi kriteria penerima bansos')
