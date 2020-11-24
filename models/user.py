from . import contact
from colorama import init
from termcolor import colored

init()

def Check_User_Respond(Respon) :
	if Respon == "A" :
		contact.tambah_barang_baru()
	if Respon == "B" :
		contact.lihat_seluruh_barang()
	if Respon == "C" :
		contact.cari_barang()
	if Respon == "D" :
		contact.hapus_barang()
	if Respon == "E" :
		contact.edit_informasi_barang()
	if Respon == "F" :
		contact.tambah_stok_barang()
	if Respon == "G" :
		contact.kurang_stok_barang()
	if Respon == "U" :
		contact.tampilan_user()
	if Respon == "O" :
		pass
	if Respon == "Q" :
		pass
	else :
		print("Respon tidak valid !")
