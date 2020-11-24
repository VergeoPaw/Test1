from os import system
from colorama import init
from termcolor import colored
from models import contact

init()

def Print_Menu() :
	system("cls")
	contact.print_judul()
	print(colored("Welcome","white"), colored('username','yellow'))

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
	contact.print_judul()
	Menu = """
[A]. Tambah User
[B]. Lihat Seluruh User
[C]. Hapus User

[Q]. Kembali ke MENU
	"""
	print(Menu)

def tentang_aplikasi() :
	system("cls")
	contact.print_judul()
	print(colored(">> ","green"),colored("Version : 2.0","yellow"))
	print(colored(">> ","green"),colored("Creator : Vergeo Valentino Gunawan (9.A)","yellow"))
	contact.print_continue()