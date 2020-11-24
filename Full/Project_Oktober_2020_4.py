#============================================================================================================================================================
#============================================================================================================================================================
#============================================================================================================================================================
#
#
#   SSSSSSSSSS   TTTTTTTTTTTT   OOOOOOOOOO   KK        KK                                                                                                                      
#  SS                 TT       OO        OO  KK      KK                                                                                        
#  SS                 TT       OO        OO  KK    KK                                                                                         
#  SS                 TT       OO        OO  KK  KK                                                                                          
#   SSSSSSSSSS        TT       OO        OO  KKKK                                                                                                   
#            SS       TT       OO        OO  KK  KK                                                                                           
#            SS       TT       OO        OO  KK    KK                                                                                          
#            SS       TT       OO        OO  KK      KK                                                                                         
#   SSSSSSSSSS        TT        OOOOOOOOOO   KK        KK                                                                                                    
#                                                                                                                                 
#   SSSSSSSSSS   UU        UU   PPPPPPPPPP    EEEEEEEEEEE   RRRRRRRRRRR    MMM    MMM    AAAAAAAAAA    RRRRRRRRRRR   KK        KK   EEEEEEEEEEE  TTTTTTTTTTTT
#  SS            UU        UU  PP        PP  EE            RR         RR  MM MM  MM MM  AA        AA  RR         RR  KK      KK    EE                 TT                                    
#  SS            UU        UU  PP        PP  EE            RR         RR  MM  M  M  MM  AA        AA  RR         RR  KK    KK      EE                 TT                                 
#  SS            UU        UU  PP        PP  EE            RR         RR  MM  MMMM  MM  AA        AA  RR         RR  KK  KK        EE                 TT                              
#   SSSSSSSSSS   UU        UU  PPPPPPPPPP     EEEEEEEEEEE  RRRRRRRRRRRR   MM   MM   MM  AAAAAAAAAAAA  RRRRRRRRRRRR   KKKK           EEEEEEEEEEE       TT                                                               
#            SS  UU        UU  PP            EE            RRRR           MM        MM  AA        AA  RRRR           KK  KK        EE                 TT                 
#            SS  UU        UU  PP            EE            RR  RRR        MM        MM  AA        AA  RR  RRR        KK    KK      EE                 TT                       
#            SS  UU        UU  PP            EE            RR     RRR     MM        MM  AA        AA  RR     RRR     KK      KK    EE                 TT                               
#   SSSSSSSSSS    UUUUUUUUUU   PP             EEEEEEEEEEE  RR        RRR  MM        MM  AA        AA  RR        RRR  KK        KK   EEEEEEEEEEE       TT 
#                                                                                                                                 
#   AAAAAAAAAA    BBBBBBBBBB    CCCCCCCCCCC                                                                                                                        
#  AA        AA  BB        BB  CC                                                                                                                   
#  AA        AA  BB        BB  CC                                                                                                                   
#  AA        AA  BB        BB  CC                                                                                                                  
#  AAAAAAAAAAAA  BBBBBBBBBB    CC                                                                                                                        
#  AA        AA  BB        BB  CC                                                                                                                   
#  AA        AA  BB        BB  CC                                                                                                                  
#  AA        AA  BB        BB  CC                                                                                                                   
#  AA        AA   BBBBBBBBBB    CCCCCCCCCCC                                                                                                                          
#
#
#============================================================================================================================================================
#============================================================================================================================================================
#============================================================================================================================================================


# *******************************************************************
# -------------------------------------------------------------------
# Nama		: Vergeo Valentino Gunawan
# Kelas		: IX.A (9.A)
# MAPEL		: Python Prinit()oject - Aplikasi Pencatatan Stok Supermarket ABC)
# Tanggal	: Oktober 2020
# -------------------------------------------------------------------
# *******************************************************************
#############################################################################################################################################################
from os import system
from colorama import init
from termcolor import colored

init()

def limited_print(count, text) :
	if len(text) > count :
		return text[:count]
	elif count > 8:
		if len(text) < 4:
			return f"{text}\t"
		else:
			return text
	else:
		return text

def int_limited_print(count, text2) :
	text = str(text2)
	if len(text) > count :
		return int(text[:count])
	elif count > 8:
		if len(text) < 4:
			return int(f"{text2}\t")
		else:
			return text
	else:
		return int(text)

def integer(text) :
	run = True
	while run :
		try :
			inte = int(input(text))
		except ValueError :
			print("Invalid Input.")
		else :
			run = False
			return inte

def edit(bagian, nama, nama_baru) :
	keputusan = input(f"Apakah anda yakin ingin mengubah {bagian} barang dari {nama} menjadi {nama_baru} ? (Y/N) ")
	if keputusan.upper() == "Y" :
		daftar_barang[nama][bagian] = nama_baru
		print(f"{bagian} barang berhasil diubah menjadi {nama_baru}")
	else :
		print(f"{bagian} barang gagal diubah !")
		
def print_judul() :
	judul = """*******************************************
===== PENCATATAN STOK SUPERMARKET ABC =====
*******************************************
"""
	print(colored(judul,"green"))

def print_continue() :
	input("\nTekan ENTER untuk melanjutkan ... ")

def Print_Menu() :
	system("cls")
	print_judul()
	print(colored("Welcome","white"), colored(username,'yellow'))

	Menu = """
[A]. Tambah Barang Baru
[B]. Lihat Seluruh Barang
[C]. Cari Barang
[D]. Hapus Barang
[E]. Edit Informasi Barang
[F]. Tambah Stok Barang	
[G]. Kurang Stok Barang

[U]. Tambah, Hapus, dan Edit
     Username dan Password

[O]. Tentang Aplikasi
[Q]. Keluar Aplikasi
"""
	print(Menu)

def Print_Menu_2() :
	system("cls")
	print_judul()
	Menu = """
[A]. Tambah User
[B]. Lihat Seluruh User
[C]. Hapus User

[Q]. Kembali ke MENU
	"""
	print(Menu)

def Check_User_Respond(Respon) :
	if Respon == "A" :
		tambah_barang_baru()
	if Respon == "B" :
		lihat_seluruh_barang()
	if Respon == "C" :
		cari_barang()
	if Respon == "D" :
		hapus_barang()
	if Respon == "E" :
		edit_informasi_barang()
	if Respon == "F" :
		tambah_stok_barang()
	if Respon == "G" :
		kurang_stok_barang()
	if Respon == "U" :
		tampilan_user()
	if Respon == "O" :
		pass
	if Respon == "Q" :
		pass

def tambah_barang_baru() :
	system("cls")
	print_judul()
	print(colored("***** Tambah Barang Baru *****","red"))

	nama_barang = limited_print(10, input("Nama Barang\t: "))
	stok = integer("Stok Awal\t: ")
	stok2 = int_limited_print(3, stok)
	kode = limited_print(10, input("Kode Produk\t: "))
	kategori = limited_print(10, input("Kategori\t: "))
	modal = integer("Modal\t\t: ")
	modal2 = int_limited_print(8, modal)
	harga = integer("Harga Jual\t: ")
	harga2 = int_limited_print(8, harga)
	respon = input(f"Apakah kamu yakin ingin menyimpan {nama_barang} ? (Y/N) ")
	if respon.upper() == "Y" :
		daftar_barang[nama_barang] = {
			"Stok" : stok2,
			"Kode Produk" : kode,
			"Kategori" : kategori,
			"Modal" : f"Rp {modal2}",
			"Harga Jual" : f"Rp {harga2}"
			}
		print(f"{nama_barang} berhasil disimpan !")
	else :
		print(f"{nama_barang} gagal disimpan !")
	print_continue()

def lihat_seluruh_barang() :
	system("cls")
	print_judul()
	if len(daftar_barang) == 0 :
		print("Tidak Ada Barang yang disimpan1")
	else :
		print(colored("|Nama Barang|\t|Stok|\t|Kode Produk|\t|Kategori|\t|Modal|\t\t|Harga Jual|\n","yellow"))
		for barang in daftar_barang :
			print("|",barang,"|\t|",daftar_barang[barang]["Stok"],"|\t|",daftar_barang[barang]["Kode Produk"],"|\t|",daftar_barang[barang]["Kategori"],"|\t|",daftar_barang[barang]["Modal"],"|\t|",daftar_barang[barang]["Harga Jual"],"|")
	print_continue()

def search(barang) :
	if barang in daftar_barang :
		print(colored("Hasil : \n","yellow"))
		print(colored("Nama Barang\t: ","yellow"), colored(barang,"green"))
		print(colored("Stok\t\t: ","yellow"), colored(daftar_barang[barang]["Stok"],"green"))
		print(colored("Kode Produk\t: ","yellow"), colored(daftar_barang[barang]["Kode Produk"],"green"))
		print(colored("Kategori\t: ","yellow"), colored(daftar_barang[barang]["Kategori"],"green"))
		print(colored("Modal\t\t: ","yellow"),colored( daftar_barang[barang]["Modal"],"green"))
		print(colored("Harga Jual\t: ","yellow"), colored(daftar_barang[barang]["Harga Jual"],"green"))
		return True
	else :
		print("Data tidak ditemukan")
		return False

def cari_barang() :
	system("cls")
	print_judul()
	print(colored("***** Cari Barang *****","red"))
	nama = limited_print(10, input("Nama Barang : "))
	search(nama)
	print_continue()

def hapus_barang() :
	system("cls")
	print_judul()
	print(colored("***** Hapus Barang *****","red"))
	print("Barang didalam daftar : ")
	for barang in daftar_barang :
		print(colored(">> ","green"), colored(barang,"yellow"))
	nama = limited_print(10, input("Masukkan nama barang yang ingin dihapus : "))
	result = search(nama)
	if result :
		respon = input(f"Apakah kamu yakin ingin menghapus {nama} ? (Y/N) ")
		if respon.upper() == "Y" :
			del daftar_barang[nama]
			print(f"{nama} berhasil dihapus !")
		else :
			print("Batal menghapus !")
	print_continue()

def edit_informasi_barang() :
	system("cls")
	print_judul()
	print(colored("***** Edit Informasi Kontak *****","red"))
	nama = limited_print(10, input("Masukkan nama barang yang ingin diedit : "))
	result = search(nama)
	if result :
		print("Ingin edit apa : [1] Nama Barang, [2] Stok, [3] Kode Produk, [4] Kategori, [5] Modal, [6] Harga Jual")
		respon = input("Pilih (1-6) : ")
		if respon == "1" :
			nama_baru = limited_print(10,input("Nama barang berubah menjadi : "))
			keputusan = input(f"Apakah kamu yakin ingin mengubah nama barang {nama} menjadi {nama_baru} ? (Y/N) ")
			if keputusan.upper() == "Y" :
				daftar_barang[nama_baru] = daftar_barang[nama]
				del daftar_barang[nama]
				print(f"Nama barang berhasil diubah dari {nama} menjadi {nama_baru}")
			else :
				print("Nama barang gagal diubah !")
		elif respon == "2" :
			stok_baru = integer("Stok barang berubah menjadi : ")
			stok_baru_2 = int_limited_print(3, stok_baru)
			edit("Stok", nama, stok_baru_2)
		elif respon == "3" :
			kode_baru = limited_print(10,input("Kode Produk barang berubah menjadi : "))
			edit("Kode Produk", nama, kode_baru)
		elif respon == "4" :
			kategori_baru = limited_print(10,input("Kategori barang berubah menjadi : "))
			edit("Kategori",nama, kategori_baru)
		elif respon == "5" :
			modal_baru = integer("Modal barang diubah menjadi : ")
			modal_baru_2 = int_limited_print(8, modal_baru)
			modal_baru_3 = f"Rp {modal_baru_2}"
			edit("Modal",nama,modal_baru_3)
		elif respon == "6" :
			harga_baru = integer("Harga jual barang diubah menjadi : ")
			harga_baru_2 = int_limited_print(8,harga_baru)
			harga_baru_3 = f"Rp {harga_baru_2}"
			edit("Harga Jual", nama, harga_baru_3)
		else :
			print("Input tidak valid ...")
	print_continue()

def tambah_stok_barang() :
	system("cls")
	print_judul()
	print(colored("***** Tambah Stok Barang *****","red"))
	nama = limited_print(10, input("Masukkan nama barang yang ingin ditambah stok : "))
	result = search(nama)
	if result :
		tambah = int(input(f"Stok {nama} ingin ditambah berapa ? "))
		keputusan = input(f"Apakah anda yakin ingin menambah stok {nama} sebanyak {tambah} ? (Y/N) ")
		if keputusan.upper() == "Y" :
			dulu = daftar_barang[nama]["Stok"]
			sekarang = dulu + tambah
			daftar_barang[nama]["Stok"] = int_limited_print(3,sekarang)
			print("Penambahan Stok berhasil !")
		else :
			print("Penambahan Stok Gagal !")
	print_continue()

def kurang_stok_barang() :
	system("cls")
	print_judul()
	print(colored("***** Kurang Stok Barang *****","red"))
	nama = limited_print(10, input("Masukkan nama barang yang ingin dikurang stok : "))
	result = search(nama)
	if result :
		kurang = int(input(f"Stok {nama} ingin dikurang berapa ? "))
		if kurang >= daftar_barang[nama]["Stok"] :
			print("Pengurangan melebih stok. Gagal mengurang !")
		else :
			keputusan = input(f"Apakah anda yakin ingin mengurang stok {nama} sebanyak {kurang} ? (Y/N)")
			if keputusan.upper() == "Y" :
				dulu = daftar_barang[nama]["Stok"]
				sekarang = dulu - kurang
				daftar_barang[nama]["Stok"] = int_limited_print(3,sekarang)
			else :
				print("Pengurangan Stok Gagal !")
	print_continue()

def tampilan_user() :
	RESPON = ""
	while RESPON != "Q" :
		Print_Menu_2()
		RESPON = input("Pilih Opsi (A-D / Q) : ")
		Check_RESPO	N(RESPON)

def Check_RESPON(respon) :
	if respon == "A" :
		system("cls")
		print_judul()
		print(colored("***** Tambah User Baru *****", "red"))
		username = limited_print(11,input("Username\t: "))
		password = limited_print(11,input("Password\t: "))
		respond = input(f"Apakah kamu yakin ingin menyimpan {username} ? (Y/N)")
		if respond.upper() == "Y" :
			user[username] = password
			print(f"{username} berhasil disimpan !")
		else :
			print(f"{username} gagal disimpan !")
		print_continue()
	elif respon == "B" :
		system("cls")
		print_judul()
		print(colored("|Username|\t|Password|","yellow"))
		for use in user :
			print("|",use,"|\t|",user[use],"|")
		print_continue()
	elif respon == "C" :
		system("cls")
		print_judul()
		if len(user) == 1 :
			print("User yang tersedia tinggal 1. Tidak bisa menghapus user !")
		else :
			nama = limited_print(11,input("Masukkan username yang ingin dihapus : "))
			if nama in user :
				print(f"Username \t= {nama}")
				print(f"Password \t= {user[nama]}")
				keputusan = input(f"Apakah kamu yakin ingin menghapus {nama} ? (Y/N) ")
				if keputusan.upper() == "Y" :
					del user[nama]
					print(f"{nama} berhasil dihapus !")
				else :
					print(f"{nama} gagal dihapus !")
			else :
				print("User tidak ditemukan !")
		print_continue()


daftar_barang = {
	'Indomie' : {
		'Stok' : 10,
		'Kode Produk' : '123456',
		'Kategori' : 'Makanan',
		'Modal' : 'Rp 2000',
		'Harga Jual' : 'Rp 4000'
		},
	'Lifebuoy' : {
		'Stok' : 15,
		'Kode Produk' : '654321',
		'Kategori' : 'Alat Mandi',
		'Modal' : 'Rp 10000',
		'Harga Jual' : 'Rp 15000'
		}
}

user = {
	'Admin1' : '123456',
	'Admin2' : '654321'}

login = False
while not login :
	system("cls")
	print_judul()
	print(colored("***** Login User *****","red"))
	username = input("Username\t: ")
	password = input("Password\t: ")

	if username in user :
		if user[username] == password :
			login = True
		else :
			print("Username atau Password tidak valid.")
			print_continue()
	else :
		print("Username atau Password tidak valid.")
		print_continue()

else :
	User_Respond = ""

	while User_Respond != "Q" :
		Print_Menu()
		User_Respond = input("Pilih Opsi (A - G / U / O / Q) : ").upper()
		Check_User_Respond(User_Respond)
	else :
		system("cls")
		print_judul()
		print(colored(">> ","green"),colored("Thank you for using this application !","yellow"))
		print(colored(">> ","green"),colored("Good Bye !","yellow"))