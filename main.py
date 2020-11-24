from os import system

import views
from models import user,contact
from colorama import init
from termcolor import colored

init()
contact.load_contacts()
users = contact.load_users()
login = False
while not login :
	system("cls")
	contact.print_judul()
	print(colored("***** Login User *****","red"))
	username = contact.limited_print(11,input("Username\t: "))
	password = contact.limited_print(11,input("Password\t: "))

	if username in users:
		if users[username] == password :
			login = True
		else :
			print("Username atau Password tidak valid.")
			contact.print_continue()
	else :
		print("Username atau Password tidak valid.")
		contact.print_continue()
else :
	user_respond = ""
	while user_respond != "Q" :
		views.Print_Menu()
		user_respond = input("Pilih Opsi (A - G / U / O / Q) : ").upper()
		if user_respond == "O" :
			views.tentang_aplikasi()
		elif user_respond == "U" :
			RESPON = ""
			while RESPON != "Q" :
				views.Print_Menu_2()
				RESPON = input("Pilih Opsi (A-D / Q) : ")
				contact.Check_RESPON(RESPON)
		else :
			user.Check_User_Respond(user_respond)
	else :
		system("cls")
		contact.print_judul()
		print(colored(">> ","green"),colored("Thank you for using this application !","yellow"))
		print(colored(">> ","green"),colored("Good Bye !","yellow"))