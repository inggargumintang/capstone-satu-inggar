import os
import time

# Warna Terminal
MERAH = '\033[91m'
HIJAU = '\033[92m'
KUNING = '\033[93m'
BIRU = '\033[94m'
UNGU = '\033[95m'
BIRU_TERANG = '\033[96m'
PUTIH = '\033[97m'
RESET = '\033[0m'

# data siswa terdiri dari 10 siswa laki-laki dan 20 siswa perempuan yang terbagi menjadi 15 siswa IPA dan 15 siswa IPS, dengan rincian nilai mata pelajaran Matematika, Bahasa Indonesia, Bahasa Inggris, dan nilai peminatan
data_siswa = [
    {"nis":1001, "nama": "Dewi Lestari", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "sosiologi", "nilai_mtk": 100, "nilai_bind": 88, "nilai_bing": 78, "nilai_peminatan": 68},
    {"nis":1002, "nama": "Kadek Sari", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "biologi", "nilai_mtk": 78, "nilai_bind": 90, "nilai_bing": 82, "nilai_peminatan": 94},
    {"nis":1003, "nama": "Andi Syahputra", "jenis_kelamin": "laki-laki", "kelas": "IPS", "peminatan": "geografi", "nilai_mtk": 72, "nilai_bind": 82, "nilai_bing": 100, "nilai_peminatan": 68},
    {"nis":1004, "nama": "Bayu Pratama", "jenis_kelamin": "laki-laki", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 98, "nilai_bind": 94, "nilai_bing": 76, "nilai_peminatan": 72},
    {"nis":1005, "nama": "Candra Wijaya", "jenis_kelamin": "laki-laki", "kelas": "IPS", "peminatan": "geografi", "nilai_mtk": 76, "nilai_bind": 98, "nilai_bing": 94, "nilai_peminatan": 90},
    {"nis":1006, "nama": "Putu Ayu", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "biologi", "nilai_mtk": 78, "nilai_bind": 94, "nilai_bing": 78, "nilai_peminatan": 94},
    {"nis":1007, "nama": "Ni Luh Gading", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "biologi", "nilai_mtk": 68, "nilai_bind": 80, "nilai_bing": 98, "nilai_peminatan": 72},
    {"nis":1008, "nama": "Made Suastini", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "biologi", "nilai_mtk": 72, "nilai_bind": 98, "nilai_bing": 82, "nilai_peminatan": 100},
    {"nis":1009, "nama": "Dani Situmorang", "jenis_kelamin": "laki-laki", "kelas": "IPS", "peminatan": "ekonomi", "nilai_mtk": 72, "nilai_bind": 94, "nilai_bing": 88, "nilai_peminatan": 98},
    {"nis":1010, "nama": "Siti Nurhaliza", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "sosiologi", "nilai_mtk": 100, "nilai_bind": 68, "nilai_bing": 80, "nilai_peminatan": 90},
    {"nis":1011, "nama": "Eki Malindo", "jenis_kelamin": "laki-laki", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 94, "nilai_bind": 90, "nilai_bing": 98, "nilai_peminatan": 76},
    {"nis":1012, "nama": "Firman Saragih", "jenis_kelamin": "laki-laki", "kelas": "IPS", "peminatan": "ekonomi", "nilai_mtk": 68, "nilai_bind": 100, "nilai_bing": 76, "nilai_peminatan": 78},
    {"nis":1013, "nama": "Ratna Wulandari", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "sosiologi", "nilai_mtk": 90, "nilai_bind": 82, "nilai_bing": 90, "nilai_peminatan": 72},
    {"nis":1014, "nama": "Kartika Wijayanti", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "kimia", "nilai_mtk": 72, "nilai_bind": 78, "nilai_bing": 94, "nilai_peminatan": 80},
    {"nis":1015, "nama": "Retno Asmara", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "sosiologi", "nilai_mtk": 68, "nilai_bind": 80, "nilai_bing": 100, "nilai_peminatan": 98},
    {"nis":1016, "nama": "Guntur Wibisono", "jenis_kelamin": "laki-laki", "kelas": "IPS", "peminatan": "ekonomi", "nilai_mtk": 90, "nilai_bind": 72, "nilai_bing": 100, "nilai_peminatan": 68},
    {"nis":1017, "nama": "Hasim Pangestu", "jenis_kelamin": "laki-laki", "kelas": "IPA", "peminatan": "biologi", "nilai_mtk": 98, "nilai_bind": 72, "nilai_bing": 88, "nilai_peminatan": 80},
    {"nis":1018, "nama": "Ikhsan Anwar", "jenis_kelamin": "laki-laki", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 100, "nilai_bind": 68, "nilai_bing": 94, "nilai_peminatan": 72},
    {"nis":1019, "nama": "Larasati Rahayu", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "ekonomi", "nilai_mtk": 72, "nilai_bind": 76, "nilai_bing": 98, "nilai_peminatan": 80},
    {"nis":1020, "nama": "Liana Kusuma", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "ekonomi", "nilai_mtk": 68, "nilai_bind": 88, "nilai_bing": 72, "nilai_peminatan": 68},
    {"nis":1021, "nama": "Evelyn Tanubrata", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "geografi", "nilai_mtk": 76, "nilai_bind": 76, "nilai_bing": 82, "nilai_peminatan": 68},
    {"nis":1022, "nama": "Jefri Saputra", "jenis_kelamin": "laki-laki", "kelas": "IPS", "peminatan": "sosiologi", "nilai_mtk": 98, "nilai_bind": 100, "nilai_bing": 90, "nilai_peminatan": 98},
    {"nis":1023, "nama": "Melisa Gunawan", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 100, "nilai_bind": 80, "nilai_bing": 100, "nilai_peminatan": 76},
    {"nis":1024, "nama": "Jessica Tanjung", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "kimia", "nilai_mtk": 80, "nilai_bind": 68, "nilai_bing": 80, "nilai_peminatan": 94},
    {"nis":1025, "nama": "Olivia Sutanto", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "ekonomi", "nilai_mtk": 78, "nilai_bind": 76, "nilai_bing": 94, "nilai_peminatan": 82},
    {"nis":1026, "nama": "Yani Wenda", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 60, "nilai_bind": 52, "nilai_bing": 54, "nilai_peminatan": 50},
    {"nis":1027, "nama": "Merina Bambang", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 52, "nilai_bind": 52, "nilai_bing": 46, "nilai_peminatan": 46},
    {"nis":1028, "nama": "Naomi Hembri", "jenis_kelamin": "perempuan", "kelas": "IPS", "peminatan": "sosiologi", "nilai_mtk": 54, "nilai_bind": 52, "nilai_bing": 42, "nilai_peminatan": 60},
    {"nis":1029, "nama": "Veronika Kossay", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 52, "nilai_bind": 40, "nilai_bing": 50, "nilai_peminatan": 58},
    {"nis":1030, "nama": "Selvina Mofu", "jenis_kelamin": "perempuan", "kelas": "IPA", "peminatan": "kimia", "nilai_mtk": 46, "nilai_bind": 52, "nilai_bing": 42, "nilai_peminatan": 46},
    {"nis":1031, "nama": "Axel Pangestu", "jenis_kelamin": "laki-laki", "kelas": "IPA", "peminatan": "fisika", "nilai_mtk": 50, "nilai_bind": 42, "nilai_bing": 46, "nilai_peminatan": 46}
]
# clear screen function for windows digunakan untuk membersihkan layar terminal
def clear_screen():
    os.system('cls')

# tampilan menu utama program yang berisi 5 pilihan menu utama program yang akan ditampilkan ke layar terminal setelah program dijalankan 
def tampilan_menu():
    clear_screen()
    print(f"{BIRU_TERANG}╔══════════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Data Nilai Siswa UN Kelas XII       {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚══════════════════════════════════════════╝{RESET}")
    print(f"{HIJAU}\n1. Tampilkan Data Nilai Siswa{RESET}")
    print(f"{KUNING}2. Cari Data Nilai Siswa{RESET}")
    print(f"{HIJAU}3. Urutkan Data Nilai Siswa{RESET}")
    print(f"{BIRU}4. Perbandingan Nilai Siswa{RESET}")
    print(f"{BIRU_TERANG}5. Menambahkan Data Nilai Siswa{RESET}")
    print(f"{MERAH}6. Keluar{RESET}")

# fungsi tampilkan data digunakan untuk menampilkan seluruh data yang ada
# fungsi ini memisahkan antara kelas ipa dan ips untuk mempermudah pembacaan data
# fungsi ini juga memberikan opsi untuk mengedit dan menghapus data
def tampilkan_data(opsi=""):
    clear_screen()
    print(f"{BIRU_TERANG}╔══════════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Data Nilai Siswa UN Kelas XII       {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚══════════════════════════════════════════╝{RESET}")
    print(f"{BIRU_TERANG}╔═══════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Kelas XII IPA    {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═══════════════════════╝{RESET}")
    tampilkan_data_kelas(data_siswa,"IPA")
    print(f"{BIRU_TERANG}╔═══════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Kelas XII IPS    {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═══════════════════════╝{RESET}")
    tampilkan_data_kelas(data_siswa,"IPS")
    print(f"{HIJAU}1. Edit Data{RESET}")
    print(f"{KUNING}2. Hapus Data{RESET}")
    print(f"{HIJAU}3. Tekan Enter untuk kembali ke menu utama...{RESET}")

    if not opsi:
        opsi = input(f"{HIJAU}Masukkan Pilihan :{RESET}")
    if opsi == "1":
        print(f"\n{KUNING}Edit data siswa{RESET}")
        data = cari_data_2("1")
        edit_data(data["nis"])
    elif opsi == "2":
        print(f"\n{MERAH}Hapus data siswa{RESET}")
        data = cari_data_2("2")
        hapus_data(data["nis"])
    elif opsi == "":
        main()
    else:
        print(f"{MERAH}Pilihan tidak tersedia!{RESET}")
        time.sleep(2)
        tampilkan_data()
        

# fungsi tampilkan data kelas digunakan untuk menampilkan data siswa berdasarkan kelas yang diinputkan oleh pengguna program input kosong digunakan dalam pencarian
def tampilkan_data_kelas(data_siswa,kelas=""):
    if kelas =="":
        headers = ["NIS", "Nama", "Jenis Kelamin", "Kelas", "Minat", "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Peminatan","Rata-rata Nilai","Grade","Status"]
        head = [key for key in data_siswa[0].keys()]
        # head =["nis", "nama", "jenis_kelamin", "kelas", "peminatan", "nilai_mtk", "nilai_bind", "nilai_bing", "nilai_peminatan"]
    else:
        headers = ["NIS", "Nama", "Jenis Kelamin", "Minat", "Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Peminatan","Rata-rata Nilai","Grade","Status"]
        head = [key for key in data_siswa[0].keys() if key != 'kelas']
    column_widths = [max(len(str(siswa[heads])) for siswa in data_siswa) for heads in head]+[len("100"),len("A"),len("Tidak Lulus")]
    column_widths = [max(len(header), width) for header, width in zip(headers, column_widths)]

    # Cetak header
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
    print("|" + "|".join([" " + header.center(width) + " " for header, width in zip(headers, column_widths)]) + "|")
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")

    # Cetak data siswa
    for siswa in data_siswa:
        if siswa["kelas"] == kelas or kelas=="":
            rata_rata = (siswa["nilai_mtk"] + siswa["nilai_bind"] + siswa["nilai_bing"] + siswa["nilai_peminatan"]) / 4
            grade = ""
            if rata_rata >= 85:
                grade = "A"
            elif rata_rata >= 75:
                grade = "B"
            elif rata_rata >= 65:
                grade = "C"
            elif rata_rata >= 55:
                grade = "D"
            else:
                grade = "E"
            if siswa['nilai_mtk']>55 and siswa['nilai_bind']>55 and siswa['nilai_bing']>55 and siswa['nilai_peminatan']>55:
                status = 'Lulus'
            else:
                status = 'Tidak Lulus'
            row = [str(siswa[vals]) for vals in head]+[str(rata_rata), grade,status]
            print("|" + "|".join([" " + value.ljust(width) + " " for value, width in zip(row, column_widths)]) + "|")
    print("+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+")
    print()

# fungsi cari data 2 digunakan untuk mencari data siswa berdasarkan nama atau nis yang diinputkan oleh pengguna program
# fungsi ini digunakan dalam mengedit dan menghapus data siswa
def cari_data_2(flag):
    data = []
    pencarian = input(f"{HIJAU}Masukkan Nama atau NIS Siswa :{RESET}")
    if len(pencarian) == 0:
        print(f"{MERAH}Masukan tidak boleh kosong{RESET}")
        time.sleep(2)
        tampilkan_data(flag)
    elif bool(pencarian.isdigit()):
        for siswa in data_siswa:
            if siswa["nis"] == int(pencarian):
                data.append(siswa)
    elif bool(pencarian.replace(" ","").isalpha()):
        for siswa in data_siswa:
            if pencarian.lower() in siswa["nama"].lower():
                data.append(siswa)
    else :
        print(f"{MERAH}Masukan hanya berupa angka dan huruf{RESET}")
        time.sleep(2)
        tampilkan_data(flag)
    if len(data) == 0:
        print(f"{MERAH}Data tidak ditemukan{RESET}")
        time.sleep(2)
        tampilkan_data(flag)
    elif len(data) == 1:
        return data[0]
    else:
        for i in range(len(data)):
            print(f"{HIJAU}{i+1}. {data[i]['nama']}{RESET}")
        pilihan = input(f"{HIJAU}Masukkan pilihan: {RESET}")
        if bool(pilihan.isdigit()):
            if int(pilihan) > 0 and int(pilihan) <= len(data):
                return data[int(pilihan)-1]
            else:
                print(f"{MERAH}Pilihan tidak valid!{RESET}")
                time.sleep(2)
                tampilkan_data(flag)
    

#  fungsi edit data menggunakan nis parameter untuk mempermudah mendapatkan index data siswa yang akan diubah
def edit_data(nis_target):
    index = 0
    for i in range(len(data_siswa)):
        if int(data_siswa[i]['nis']) == int(nis_target):
            index = i
    data = data_siswa[index]
    print(f"{HIJAU}nama : {data['nama']} {RESET}")
    # "nis", "nama", "jenis_kelamin", "kelas", "peminatan", "nilai_mtk", "nilai_bind", "nilai_bing", "nilai_peminatan"
    nama_1 = input(f"{KUNING}Masukkan perubahan nama: {RESET}")
    if nama_1 == '':
        nama_1 = data["nama"]
    elif nama_1.replace(" ","").isalpha() == False:
        print(f"{MERAH}Nama harus berupa huruf{RESET}")
        time.sleep(2)
        edit_data(nis_target)
    else:
        nama_1 = nama_1.title()
    print(f"{HIJAU}kelas : {data['kelas']}{RESET}")
    kelas_1 = input(f"{KUNING}Masukkan Kelas 1) IPA 2) IPS: {RESET}")
    if kelas_1 =="":
        kelas_1 = data["kelas"]
    elif kelas_1 == '1':
        kelas_1 = 'IPA'
    elif kelas_1 == '2':
        kelas_1 = 'IPS'
    else:
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        edit_data(nis_target)
    print(f"{HIJAU}Kelas {kelas_1}{RESET}")
    print(f"{HIJAU}Peminatan {data['peminatan']}{RESET}")
    if kelas_1 == "IPA":
        peminatan_1 = input(f"{HIJAU}Masukkan Peminatan 1) biologi 2) fisika 3) kimia: {RESET}")
        if peminatan_1 == '':
            peminatan_1 = data["peminatan"]
        elif peminatan_1 == '1':
            peminatan_1 = 'biologi'
        elif peminatan_1 == '2':
            peminatan_1 = 'fisika'
        elif peminatan_1 == '3':
            peminatan_1 = 'kimia'
        else:
            print(f"{MERAH}Pilihan tidak valid!{RESET}")
            time.sleep(2)
            edit_data(nis_target)
    if kelas_1 == "IPS":
        peminatan_1 = input(f"{HIJAU}Masukkan Peminatan 1) ekonomi 2) geografi 3) sosiologi: {RESET}")
        if peminatan_1 == '':
            peminatan_1 = data["peminatan"]
        elif peminatan_1 == '1':
            peminatan_1 = 'ekonomi'
        elif peminatan_1 == '2':
            peminatan_1 = 'geografi'
        elif peminatan_1 == '3':
            peminatan_1 = 'sosiologi'
        else:
            print(f"{MERAH}Pilihan tidak valid!{RESET}")
            time.sleep(2)
            edit_data(nis_target)
    data_siswa[index].update({"nama":nama_1, "kelas":kelas_1,"peminatan":peminatan_1})
    print(data_siswa[index])
    print(f"{HIJAU}Data berhasil diubah!{RESET}")
    print(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
    if input() == '':
        tampilkan_data()

# fungsi hapus data menggunakan nis target parameter untuk mempermudah mendapatkan index data siswa yang akan dihapus
def hapus_data(nis_target):
    for i in range(len(data_siswa)):
        if int(data_siswa[i]["nis"]) == int(nis_target):
            data_siswa.pop(i)
            print(f"{HIJAU}Data berhasil dihapus!{RESET}")

            print(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            if input() == '':
                tampilkan_data()


'''
fungsi cari data digunakan untuk menampilkan menu pencarian data
fungsi ini memberikan 5 pilihan menu pencarian data
pilihan menu pencarian data: cari berdasarkan nis, cari berdasarkan nama, cari berdasarkan jenis kelamin, cari berdasarkan kelas, cari berdasarkan peminatan
pilihan menu pencarian data: kembali
'''
def cari_data():
    clear_screen()
    print(f"{BIRU_TERANG}╔════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Cari Data Siswa       {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚════════════════════════════╝{RESET}")
    print(f"{HIJAU}\n1. Cari Berdasarkan Nomer Induk{RESET}")
    print(f"{KUNING}2. Cari Berdasarkan Nama{RESET}")
    print(f"{HIJAU}3. Cari Berdasarkan Jenis Kelamin{RESET}")
    print(f"{BIRU}4. Cari Berdasarkan Kelas{RESET}")
    print(f"{BIRU}5. Cari Berdasarkan Peminatan{RESET}")
    print(f"{MERAH}6. Tekan 6 atau masukkan input kosong untuk Kembali{RESET}")
    
    pilihan = input(f"{HIJAU}Masukkan pilihan: {RESET}")
    if pilihan == '1':
        cari_berdasarkan_nis()
    elif pilihan == '2':
        cari_berdasarkan_nama()
    elif pilihan == '3':
        cari_berdasarkan_jenis_kelamin()
    elif pilihan == '4':
        cari_berdasarkan_kelas()
    elif pilihan == '5':
        cari_berdasarkan_peminatan()
    elif pilihan == '6' or pilihan == '':
        main()
    else:
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
    
# fungsi cari berdasarkan nis digunakan untuk mencari data siswa berdasarkan nis yang diinputkan oleh pengguna program
# fungsi ini hanya menerima input berupa angka
# jika data ditemukan, data tersebut akan ditampilkan ke layar terminal
# jika data tidak ditemukan, pesan data tidak ditemukan akan ditampilkan ke layar terminal
# jika input kosong, pencarian akan dibatalkan
def cari_berdasarkan_nis():
    clear_screen()
    print(f"{BIRU_TERANG}╔═══════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}     Pencarian Berdasarkan NIS     {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═══════════════════════════════════╝{RESET}")
    print(f"\n{HIJAU}Contoh: 1001{RESET}")
    print(f"{KUNING}Jika ingin membatalkan pencarian, tekan Enter tanpa input{RESET}")
    nis = input(f"\n{HIJAU}Masukkan NIS: {RESET}")
    data = []
    if len(nis) == 0:
        print(f"{KUNING}Pencarian dibatalkan!{RESET}")
        time.sleep(2)
        cari_data()
    elif bool(nis.isdigit()):
        data = [siswa for siswa in data_siswa if siswa["nis"]==int(nis)]
        if data:
            print(f"{HIJAU}Data ditemukan!{RESET}")
            tampilkan_data_kelas(data)
            input(f"\n{HIJAU}Tekan Enter untuk kembali ke menu utama{RESET}")
            main()
        else:
            print(f"{MERAH}Data tidak ditemukan!{RESET}")
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            cari_data()
    else:
        print(f"{MERAH}NIS harus berupa angka!{RESET}")
        time.sleep(2)
        cari_berdasarkan_nis()
'''
fungsi cari berdasarkan nama digunakan untuk mencari data siswa berdasarkan nama yang diinputkan oleh pengguna program
fungsi ini hanya menerima input berupa huruf
jika data ditemukan, data tersebut akan ditampilkan ke layar terminal
jika data tidak ditemukan, pesan data tidak ditemukan akan ditampilkan ke layar terminal
jika input kosong, pesan nama tidak boleh kosong akan ditampilkan ke layar terminal
'''     
def cari_berdasarkan_nama():
    clear_screen()
    print(f"{BIRU_TERANG}╔════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}     Pencarian Berdasarkan Nama     {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚════════════════════════════════════╝{RESET}")
    print(f"\n{HIJAU}Contoh: Dewi{RESET}")
    print(f"{KUNING}Jika ingin membatalkan pencarian, tekan Enter tanpa input{RESET}")
    nama = input(f"\n{HIJAU}Masukkan Nama: {RESET}")
    data = []
    if nama == '':
        print(f"{HIJAU}Kembali ke menu pencarian!{RESET}")
        time.sleep(2)
        cari_data()
    elif bool(nama.replace(" ","").isalpha()): # cek apakah input berupa huruf
        data = [siswa for siswa in data_siswa if nama.lower() in siswa["nama"].lower()]
        if data:
            print(f"{HIJAU}Data ditemukan!{RESET}")
            time.sleep(2)
            tampilkan_data_kelas(data)
            back = input(f"\n{HIJAU}Tekan Enter untuk kembali ke menu utama{RESET}")
            if not back:
                main()
        else:
            print(f"{MERAH}Data tidak ditemukan!{RESET}")
            time.sleep(2)
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            cari_data()
    else:
        print(f"{MERAH}Nama harus berupa huruf!{RESET}")
        time.sleep(2)
        cari_berdasarkan_nama()

'''
fungsi cari berdasarkan jenis kelamin digunakan untuk mencari data siswa berdasarkan jenis kelamin yang diinputkan oleh pengguna program
fungsi ini hanya menerima input berupa angka 1 atau 2
jika data ditemukan, data tersebut akan ditampilkan ke layar terminal
jika data tidak ditemukan, pesan data tidak ditemukan akan ditampilkan ke layar terminal
jika input kosong, pencarian akan dibatalkan
'''
def cari_berdasarkan_jenis_kelamin():
    clear_screen()
    print(f"{BIRU_TERANG}╔═════════════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}     Pencarian Berdasarkan Jenis Kelamin     {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═════════════════════════════════════════════╝{RESET}")
    print(f"\n{HIJAU}Contoh: 1{RESET}")
    print(f"{KUNING}Jika ingin membatalkan pencarian, tekan Enter tanpa input{RESET}")
    print(f"{HIJAU}1. Laki-laki{RESET}")
    print(f"{KUNING}2. Perempuan{RESET}")
    jenis_kelamin = input(f"{HIJAU}Masukkan Jenis Kelamin: {RESET}")
    data = []
    if jenis_kelamin == '':
        print(f"{KUNING}Pencarian dibatalkan!{RESET}")
        time.sleep(2)
        cari_data()
    elif jenis_kelamin == '1':
        data = [siswa for siswa in data_siswa if siswa['jenis_kelamin'] == 'laki-laki']
        if data:
            print(f"{HIJAU}Data ditemukan!{RESET}")
            tampilkan_data_kelas(data)
            back = input(f"\n{HIJAU}Tekan Enter untuk kembali ke menu utama{RESET}")
            if not back:
                main()
    elif jenis_kelamin == '2':
        data = [siswa for siswa in data_siswa if siswa['jenis_kelamin'] == 'perempuan']
        if data:
            print(f"{HIJAU}Data ditemukan!{RESET}")
            tampilkan_data_kelas(data)
            back = input(f"\n{HIJAU}Tekan Enter untuk kembali ke menu utama{RESET}")
            if not back:
                main()
    else:
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        cari_berdasarkan_jenis_kelamin()
'''
fungsi cari berdasarkan kelas digunakan untuk mencari data siswa berdasarkan kelas yang diinputkan oleh pengguna program
fungsi ini hanya menerima input berupa angka 1 atau 2 (1 untuk kelas IPA dan 2 untuk kelas IPS)
jika data ditemukan, data tersebut akan ditampilkan ke layar terminal
jika data tidak ditemukan, pesan data tidak ditemukan akan ditampilkan ke layar terminal
jika input kosong, pencarian akan dibatalkan
'''
def cari_berdasarkan_kelas():
    clear_screen()
    print(f"{BIRU_TERANG}╔═════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}     Pencarian Berdasarkan Kelas     {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═════════════════════════════════════╝{RESET}")
    print(f"\n{HIJAU}1. Kelas XII IPA{RESET}")
    print(f"{KUNING}2. Kelas XII IPS{RESET}")
    print(f"\n{HIJAU}Contoh: 1{RESET}")
    print(f"{HIJAU}Jika ingin membatalkan pencarian, tekan Enter tanpa input{RESET}")
    kelas = input(f"{HIJAU}Masukkan Kelas: {RESET}")
    data = []
    if kelas == '':
        print(f"{KUNING}Pencarian dibatalkan!{RESET}")
        time.sleep(2)
        cari_data()
    elif kelas == '1':
        data = [siswa for siswa in data_siswa if siswa['kelas']=="IPA"]
        if data:
            print(f"{HIJAU}Data ditemukan!{RESET}")
            tampilkan_data_kelas(data)
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            cari_data()
        else:
            print(f"{MERAH}Data tidak ditemukan!{RESET}")
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            cari_data_kelas()
    elif kelas == '2':
        data = [siswa for siswa in data_siswa if siswa['kelas']=="IPA"]
        if data:
            print(f"{HIJAU}Data ditemukan!{RESET}")
            tampilkan_data_kelas(data)
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            cari_data()
        else:
            print(f"{MERAH}Data tidak ditemukan!{RESET}")
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            cari_data_kelas()
    else:
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        cari_berdasarkan_kelas()
'''
fungsi cari berdasarkan peminatan digunakan untuk mencari data siswa berdasarkan peminatan yang diinputkan oleh pengguna program
fungsi ini hanya menerima input berupa huruf
contoh input: biologi
jika data ditemukan, data tersebut akan ditampilkan ke layar terminal
jika data tidak ditemukan, pesan data tidak ditemukan akan ditampilkan ke layar terminal
jika input kosong, pencarian akan dibatalkan
'''
def cari_berdasarkan_peminatan():
    clear_screen()
    print(f"{BIRU_TERANG}╔═════════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}     Pencarian Berdasarkan Peminatan     {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═════════════════════════════════════════╝{RESET}")
    print(f"\n{HIJAU}Contoh: biologi{RESET}")
    print(f"{KUNING}Jika ingin membatalkan pencarian, tekan Enter tanpa input{RESET}")
    peminatan = input(f"{HIJAU}Masukkan Peminatan: {RESET}")
    data = []
    if peminatan == '':
        print(f"{KUNING}Pencarian dibatalkan!{RESET}")
        time.sleep(2)
        cari_data()
    if peminatan.isalpha():
        data = [siswa for siswa in data_siswa if peminatan.lower() in siswa['peminatan'].lower()]
        if data:
            print(f"{HIJAU}Data ditemukan!{RESET}")
            tampilkan_data_kelas(data)
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            time.sleep(2)
            cari_data()
        else:
            print(f"{MERAH}Data tidak ditemukan!{RESET}")
            input(f"\n{HIJAU}Tekan Enter untuk kembali{RESET}")
            time.sleep(2)
            cari_data()
    else:
        print(f"{MERAH}Peminatan harus berupa huruf!{RESET}")
        time.sleep(2)
        cari_berdasarkan_peminatan()


'''
fungsi urut berdasarkan nama digunakan untuk mengurutkan data siswa berdasarkan nama
fungsi ini menggunakan fungsi sorted() untuk mengurutkan data siswa berdasarkan nama
fungsi ini digunakan dalam fungsi urut data
'''
def urut_berdasarkan_nama(data):
    return sorted(data, key=lambda x: x['nama'])

'''
fungsi urut berdasarkan rata-rata nilai digunakan untuk mengurutkan data siswa berdasarkan rata-rata nilai
fungsi ini menggunakan fungsi sorted() untuk mengurutkan data siswa berdasarkan rata-rata nilai
fungsi ini digunakan dalam fungsi urut data
'''
def urut_berdasarkan_rata_rata(data):
    return sorted(data, key=lambda x: sum([x['nilai_mtk'], x['nilai_bind'], x['nilai_bing'], x['nilai_peminatan']])/4, reverse=True)

'''
fungsi urut data digunakan untuk menampilkan menu pengurutan data
fungsi ini memberikan 2 pilihan menu pengurutan data berdasarkan nama atau rata-rata nilai
pilihan menu pengurutan data: urut berdasarkan nama, urut berdasarkan rata-rata nilai
pilihan menu pengurutan data: kembali
'''
def urut_data(urut_berdasarkan):
    clear_screen()
    print(f"{BIRU_TERANG}╔══════════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Data Nilai Siswa UN Kelas XII       {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚══════════════════════════════════════════╝{RESET}")
    if urut_berdasarkan == 'nama':
        data_diurutkan = urut_berdasarkan_nama(data_siswa)
    else:
        data_diurutkan = urut_berdasarkan_rata_rata(data_siswa)

    print(f"{BIRU_TERANG}╔═══════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Kelas XII IPA    {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═══════════════════════╝{RESET}")
    tampilkan_data_kelas(data_diurutkan,"IPA")
    print(f"{BIRU_TERANG}╔═══════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Kelas XII IPS    {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═══════════════════════╝{RESET}")
    tampilkan_data_kelas(data_diurutkan,"IPS")
    input(f"\n{HIJAU}Tekan Enter untuk kembali ke menu utama...{RESET}")

'''
fungsi perbandingan digunakan untuk menampilkan menu perbandingan data
fungsi ini memberikan 3 pilihan menu perbandingan data: berdasarkan jenis kelamin, berdasarkan kelas, berdasarkan peminatan
pilihan menu perbandingan data: kembali
'''
def perbandingan():
    clear_screen()
    print(f"{BIRU_TERANG}╔══════════════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Perbandingan Rata-rata Nilai Siswa      {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚══════════════════════════════════════════════╝{RESET}",end='\n')
    print(f"{BIRU_TERANG}╔═════════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Berdasarkan Jenis Kelamin      {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═════════════════════════════════════╝{RESET}",end='\n')
    hasil_perbandingan = bandingkan_data(data_siswa,1)
    for kategori, data_kategori in hasil_perbandingan.items():
        print(f"\nKategori: {kategori.capitalize()}")
        print(f"Nilai Matematika: {data_kategori['nilai_mtk']:.2f}")
        print(f"Nilai Bahasa Indonesia: {data_kategori['nilai_bind']:.2f}")
        print(f"Nilai Bahasa Inggris: {data_kategori['nilai_bing']:.2f}")
        print(f"Nilai Peminatan: {data_kategori['nilai_peminatan']:.2f}")
    print(f"{BIRU_TERANG}╔═════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Berdasarkan Kelas      {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═════════════════════════════╝{RESET}",end='\n')
    hasil_perbandingan = bandingkan_data(data_siswa,2)
    for kategori, data_kategori in hasil_perbandingan.items():
        print(f"\nKategori: {kategori.capitalize()}")
        print(f"Nilai Matematika: {data_kategori['nilai_mtk']:.2f}")
        print(f"Nilai Bahasa Indonesia: {data_kategori['nilai_bind']:.2f}")
        print(f"Nilai Bahasa Inggris: {data_kategori['nilai_bing']:.2f}")
        print(f"Nilai Peminatan: {data_kategori['nilai_peminatan']:.2f}")
    print(f"{BIRU_TERANG}╔═════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}      Berdasarkan Peminatan      {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚═════════════════════════════════╝{RESET}",end='\n')
    hasil_perbandingan = bandingkan_data(data_siswa,3)
    for kategori, data_kategori in hasil_perbandingan.items():
        print(f"\nKategori: {kategori.capitalize()}")
        print(f"Nilai Matematika: {data_kategori['nilai_mtk']:.2f}")
        print(f"Nilai Bahasa Indonesia: {data_kategori['nilai_bind']:.2f}")
        print(f"Nilai Bahasa Inggris: {data_kategori['nilai_bing']:.2f}")
    input(f"\n{HIJAU}Tekan Enter untuk kembali ke menu utama...{RESET}")

'''
fungsi bandingkan data digunakan untuk membandingkan data siswa berdasarkan jenis kelamin, kelas, atau peminatan
fungsi ini memberikan 3 pilihan menu perbandingan data: berdasarkan jenis kelamin, berdasarkan kelas, berdasarkan peminatan
pilihan menu perbandingan data: kembali
fungsi ini menggunakan fungsi bandingkan_data() untuk membandingkan data siswa berdasarkan jenis kelamin, kelas, atau peminatan
fungsi ini digunakan dalam fungsi perbandingan
'''
def bandingkan_data(data,jenis):
    hasil_perbandingan = {}
    if jenis == 1:
        for jenis_kelamin in ['laki-laki','perempuan']:
            data_jenis_kelamin = [siswa for siswa in data if siswa["jenis_kelamin"] == jenis_kelamin]
            hasil_perbandingan[jenis_kelamin] = {
            "nilai_mtk": sum(siswa["nilai_mtk"] for siswa in data_jenis_kelamin) / len(data_jenis_kelamin),
            "nilai_bind": sum(siswa["nilai_bind"] for siswa in data_jenis_kelamin) / len(data_jenis_kelamin),
            "nilai_bing": sum(siswa["nilai_bing"] for siswa in data_jenis_kelamin) / len(data_jenis_kelamin),
            "nilai_peminatan": sum(siswa["nilai_peminatan"] for siswa in data_jenis_kelamin)/len(data_jenis_kelamin)
            }
        return hasil_perbandingan
    elif jenis == 2:
        for kelas in ["IPA", "IPS"]:
            data_kelas = [siswa for siswa in data if siswa["kelas"] == kelas]
            hasil_perbandingan[kelas] = {
                "nilai_mtk": sum(siswa["nilai_mtk"] for siswa in data_kelas) / len(data_kelas),
                "nilai_bind": sum(siswa["nilai_bind"] for siswa in data_kelas) / len(data_kelas),
                "nilai_bing": sum(siswa["nilai_bing"] for siswa in data_kelas) / len(data_kelas),
                "nilai_peminatan": sum(siswa["nilai_peminatan"] for siswa in data_kelas)/len(data_kelas)
            }
        return hasil_perbandingan
    else :
        peminatan_set = set(siswa["peminatan"] for siswa in data)
        for peminatan in peminatan_set:
            data_peminatan = [siswa for siswa in data if siswa["peminatan"] == peminatan]
            hasil_perbandingan[peminatan] = {
                "nilai_mtk": sum(siswa["nilai_mtk"] for siswa in data_peminatan) / len(data_peminatan),
                "nilai_bind": sum(siswa["nilai_bind"] for siswa in data_peminatan) / len(data_peminatan),
                "nilai_bing": sum(siswa["nilai_bing"] for siswa in data_peminatan) / len(data_peminatan)
            }
        return hasil_perbandingan

'''
fungsi tambah data digunakan untuk menambahkan data siswa
fungsi ini memberikan 8 input data siswa yang harus diisi oleh pengguna program
input data siswa: nis, nama, jenis kelamin, kelas, peminatan, nilai matematika, nilai bahasa indonesia, nilai bahasa inggris, nilai peminatan
jika input data kosong, pesan input data dibatalkan kembali ke menu utama akan ditampilkan ke layar terminal
jika nis sudah ada, pesan nis sudah ada akan ditampilkan ke layar terminal
jika nis tidak berupa angka, pesan nis harus berupa angka akan ditampilkan ke layar terminal
jika nama tidak berupa huruf, pesan nama harus berupa huruf akan ditampilkan ke layar terminal
jika jenis kelamin tidak sesuai, pesan pilihan tidak valid akan ditampilkan ke layar terminal
jika kelas tidak sesuai, pesan pilihan tidak valid akan ditampilkan ke layar terminal
jika peminatan tidak sesuai, pesan pilihan tidak valid akan ditampilkan ke layar terminal
jika nilai matematika tidak berupa angka, pesan nilai harus berupa angka bulat akan ditampilkan ke layar terminal
jika nilai matematika tidak berada di antara 0 dan 100, pesan nilai harus berada di antara 0 dan 100 akan ditampilkan ke layar terminal
jika input data sudah sesuai, data siswa akan ditambahkan ke data_siswa
'''
def tambah_data(nis='',nama='',jenis_kelamin='',kelas='',peminatan='',nilai_mtk='',nilai_bind='',nilai_bing='',nilai_peminatan=''):
    clear_screen()
    print(f"{BIRU_TERANG}╔════════════════════════════════╗{RESET}")
    print(f"{BIRU_TERANG}║{UNGU}     Menambahkan Data Siswa     {BIRU_TERANG}║{RESET}")
    print(f"{BIRU_TERANG}╚════════════════════════════════╝{RESET}")
    print(f"\n{HIJAU}Jika ingin membatalkan input, tekan Enter tanpa input{RESET}")

    nis = nis or input(f"{HIJAU}Masukkan NIS: {RESET}") or batal_input()
    if nis.isdigit():
        if int(nis) in [siswa["nis"] for siswa in data_siswa]:
            print(f"{MERAH}NIS sudah ada!{RESET}")
            time.sleep(2)
            tambah_data()
        else:
            pass
    else:
        print(f"{MERAH}NIS harus berupa angka!{RESET}")
        time.sleep(2)
        tambah_data()

    nama = nama or input(f"{HIJAU}Masukkan Nama: {RESET}") or batal_input()
    if not nama.replace(" ","").isalpha(): # cek apakah input berupa huruf
        print(f"{MERAH}Nama harus berupa huruf!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis)
    jenis_kelamin = jenis_kelamin or input(f"{HIJAU}Masukkan Jenis Kelamin 1) laki-laki 2) perempuan: {RESET}") or batal_input()
    jenis_kelamin = {"1": "laki-laki", "2": "perempuan"}.get(jenis_kelamin, jenis_kelamin)
    if jenis_kelamin not in ["laki-laki", "perempuan"]:
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama)
    kelas = kelas or input(f"{HIJAU}Masukkan Kelas 1) IPA 2) IPS: {RESET}") or batal_input()
    kelas = {"1": "IPA", "2": "IPS"}.get(kelas, kelas)
    if kelas not in ["IPA", "IPS"]:
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin)
    peminatan_pilihan = {
        "IPA": {"1": "biologi", "2": "fisika", "3": "kimia"},
        "IPS": {"1": "ekonomi", "2": "geografi", "3": "sosiologi"}
    }
    for key, values in peminatan_pilihan[kelas].items():
        print(f"{HIJAU}{key}) {values}{RESET}")

    peminatan = peminatan or input(f"{HIJAU}Masukkan Peminatan : {RESET}") or batal_input()
    peminatan = peminatan_pilihan[kelas].get(peminatan, peminatan)
    if peminatan not in peminatan_pilihan[kelas].values():
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas)

    nilai_mtk = nilai_mtk or input(f"{HIJAU}Masukkan Nilai Matematika: {RESET}") or batal_input()
    if nilai_mtk.isdigit():
        nilai_mtk = int(nilai_mtk)
        if 0 <=nilai_mtk<=100:
            pass
        else:
            print(f"{MERAH}Nilai harus berada di antara 0 dan 100!{RESET}")
            time.sleep(2)
            tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan)
    else:
        print(f"{MERAH}Nilai harus berupa angka bulat!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan)

    nilai_bind = nilai_bind or input(f"{HIJAU}Masukkan Nilai Bahasa Indonesia: {RESET}") or batal_input()
    if nilai_bind.isdigit():
        nilai_bind = int(nilai_bind)
        if 0 <=nilai_bind<=100:
            pass
        else:
            print(f"{MERAH}Nilai harus berada di antara 0 dan 100!{RESET}")
            time.sleep(2)
            tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan,nilai_mtk=nilai_mtk)
    else:
        print(f"{MERAH}Nilai harus berupa angka bulat!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan,nilai_mtk=nilai_mtk)

    nilai_bing = nilai_bing or input(f"{HIJAU}Masukkan Nilai Bahasa Inggris: {RESET}") or batal_input()
    if nilai_bing.isdigit():
        nilai_bing = int(nilai_bing)
        if 0 <=nilai_bing<=100:
            pass
        else:
            print(f"{MERAH}Nilai harus berada di antara 0 dan 100!{RESET}")
            time.sleep(2)
            tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan,nilai_mtk=nilai_mtk,nilai_bind=nilai_bind)
    else:
        print(f"{MERAH}Nilai harus berupa angka bulat!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan,nilai_mtk=nilai_mtk,nilai_bind=nilai_bind)

    nilai_peminatan = nilai_peminatan or input(f"{HIJAU}Masukkan Nilai Peminatan: {RESET}") or batal_input()
    if nilai_peminatan.isdigit():
        nilai_peminatan = int(nilai_peminatan)
        if 0 <=nilai_peminatan<=100:
            pass
        else:
            print(f"{MERAH}Nilai harus berada di antara 0 dan 100!{RESET}")
            time.sleep(2)
            tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan,nilai_mtk=nilai_mtk,nilai_bind=nilai_bind,nilai_bing=nilai_bing)
    else:
        print(f"{MERAH}Nilai harus berupa angka bulat!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan,nilai_mtk=nilai_mtk,nilai_bind=nilai_bind,nilai_bing=nilai_bing)

    print(f"{HIJAU}Apakah anda yakin untuk menambahkan data?{RESET}")
    print(f"{HIJAU}1) Ya{RESET}")
    print(f"{MERAH}2) Tidak{RESET}")
    konfirmasi = input(f"\n{HIJAU}Masukkan pilihan Anda: {RESET}")
    if konfirmasi == '1':
        data_siswa.append({"nis":nis, "nama": nama, "jenis_kelamin": jenis_kelamin, "kelas": kelas, "peminatan": peminatan, "nilai_mtk": nilai_mtk, "nilai_bind": nilai_bind, "nilai_bing": nilai_bing, "nilai_peminatan": nilai_peminatan})
        print(f"{HIJAU}Data berhasil ditambahkan!{RESET}")
        input(f"\n{HIJAU}Tekan Enter untuk kembali ke menu utama...{RESET}")
        main()
    elif konfirmasi == '2':
        print(f"{MERAH}Data dibatalkan!{RESET}")
        time.sleep(2)
        tambah_data()
    else:
        print(f"{MERAH}Pilihan tidak valid!{RESET}")
        time.sleep(2)
        tambah_data(nis=nis, nama=nama, jenis_kelamin=jenis_kelamin, kelas=kelas, peminatan=peminatan, nilai_mtk=nilai_mtk, nilai_bind=nilai_bind, nilai_bing=nilai_bing, nilai_peminatan=nilai_peminatan)    

def batal_input():
    print(f"{MERAH}Input data dibatalkan kembali ke menu utama{RESET}") 
    time.sleep(2) 
    main() 


'''
fungsi main digunakan untuk menampilkan menu utama
fungsi ini memberikan 6 pilihan menu utama
pilihan menu utama: tampilkan data, cari data, urut data, perbandingan, tambah data, keluar
pilihan menu utama: tampilkan data digunakan untuk menampilkan data siswa
pilihan menu utama: cari data digunakan untuk mencari data siswa
pilihan menu utama: urut data digunakan untuk mengurutkan data siswa
pilihan menu utama: perbandingan digunakan untuk membandingkan data siswa
pilihan menu utama: tambah data digunakan untuk menambahkan data siswa
pilihan menu utama: keluar digunakan untuk keluar dari program
'''

def main():
    while True:
        tampilan_menu()
        pilihan = input(f"{KUNING}\nMasukkan pilihan Anda: {RESET}")
        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            cari_data()
        elif pilihan == '3':
            urut_berdasarkan = input(f"{KUNING}\nUrutkan berdasarkan (nama/nilai): {RESET}").lower()
            if urut_berdasarkan == 'nama' or urut_berdasarkan == 'nilai':
                urut_data(urut_berdasarkan)
            elif urut_berdasarkan == '':
                print(f"{KUNING}kembali ke menu utama{RESET}")
                time.sleep(2)
                main()
            else:
                print(f"{MERAH}Pilihan tidak valid. Silakan coba lagi.{RESET}")
                time.sleep(2)
        elif pilihan == '4':
            perbandingan()
        elif pilihan == '5':
            print(f"{HIJAU}Tambahkan Data Siswa{RESET}")
            tambah_data()

        elif pilihan == '6':
            print(f"{MERAH}Terima kasih telah menggunakan aplikasi ini.{RESET}")
            time.sleep(2)
            exit()
            break
        else:
            print(f"{MERAH}Pilihan tidak valid. Silakan coba lagi.{RESET}")
            time.sleep(2)

'''
fungsi main() digunakan untuk menjalankan program
fungsi ini akan dijalankan ketika program dijalankan
fungsi ini akan menjalankan fungsi main()
'''
if __name__ == '__main__':
    main()
