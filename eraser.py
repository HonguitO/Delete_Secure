#!/usr/bin/env python
import sys, subprocess, os
from time import sleep
"""La herramienta de Secure-Delete es un conjunto de
programa que nos permite borrar de manera permanente archivos"""
def banner_menu():
	"""funcion banner"""
	print "+++++++++++++++++++++++++++++++++++"
	print "+       TOOLS SECURE-DELETE       +"
	print "+             By H0n6o            +"
	print "+++++++++++++++++++++++++++++++++++"

def salir():
	os.system("clear")
	banner_menu()
	key = raw_input("DESEA SALIR s/n: ")
	if key == "s":
		os.system("clear")
		exit();
	elif key == "n":
		menu_principal()
	elif key != 'break':
		salir()
		
def menu_principal():
	"""funcion menu principal"""
	opc = True
	while opc:
		os.system("clear")
		banner_menu()
		print "1).INSTALL SECURE-DELETE - DIST-UBUNTU."
		print "2).CREAR DIRECTORIO."
		print "3).BORRAR DIRECTORIO."
		print "4).BORRAR ARCHIVO."
		print "5).LIBERAR MEMORIA RAM."
		print "6).LIBERAR SWAP"
		print "7).BORRAR HDD 100%."
		print "s).SALIR."
		opc = raw_input("INGRESE UNA OPCION: ")
		if opc == "1":
			install_sd()
		elif opc == "2":
			crear_dir()			
		elif opc == "3":
			borrar_dir()
		elif opc == "4":
			borrar_arch()
		elif opc == "5":
			liberar_men()
		elif opc == "6":
			liberar_swap()
		elif opc == "7":
			borrar_hdd()
		elif opc == "s":
			salir()
		elif opc != 'break':
			menu_principal()

def install_sd():
	"""funcion para instalar la herramienta secure-delete"""
	os.system("gnome-terminal -x sh -c 'sudo apt-get install secure-delete'")
	os.system("clear")
	menu_principal()

def crear_dir():
	"""funcion para crear carpeta, que se crea en el directorio HOME"""
	os.system("clear")
	banner_menu()
	userdir = os.environ['HOME']
	direc = userdir+"/Borrar"
	if os.path.exists(direc):	##controla si el directorio ya fue creada
		print "EL DIRECTORIO YA FUE CREADO...."
		sleep(2)
		crear_dir
	else: ##en caso que no, crea un directorio
		print "CREADO DIRECTORIO...."
		sleep(2)
		os.mkdir(direc)
		if os.path.exists(direc):	##controla si se creo el directorio
			print "EL DIRECTORIO FUE CREADO....."
			sleep(2)
		else:
			print "EL DIRECTORIO NO FUE CREADO....."
			sleep(2)

def borrar_dir():
	"""funcion para borrar el directorio"""
	os.system("clear")
	banner_menu()
	userdir = os.environ['HOME']
	direc = userdir+"/Borrar"
	os.system("sudo srm -v -r %s" % direc)
	print "LOS ARCHIVOS FUERON BORRADO...."
	sleep(3)
	os.system("clear")
	menu_principal()

def borrar_arch():
	"""funcion para borrar un archivo"""
	os.system("clear")
	banner_menu()
	dirarch = raw_input("INGRESE LA RUTA DEL ARCHIVO: ")
	os.system("srm -v %s" % dirarch)
	print "EL ARCHIVO FUE BORRADO......."
	sleep(3)
	os.system("clear")
	menu_principal()

def liberar_men():
	"""funcion para liberar la memoria RAM"""
	os.system("clear")
	banner_menu()
	ejec = subprocess.Popen(["smem"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	no_install = ejec.stderr.read()
	ejec.stderr.close()
	cmd = ejec.stdout.read()
	ejec.stdout.close()
	if not no_install: ##controla si se instalo smen, si se instalo libera la memoria
		print cmd
		print "LIBERANDO MEMORIA RAM.... :D"
		sleep(3)
		os.system("clear")
		menu_principal()
	else: ##en caso contrario instala smem
		print "SMEM SE INSTALARA EN TU SISTEMA..... :D"
		sleep(3)	
		os.system("sudo apt-get install smem")
		os.system("clear")
		menu_principal()
		
def borrar_hdd():
	"""funcion para borrar disco duro"""
	os.system("clear")
	banner_menu()
	key = raw_input("OBS: TU HDD SE BORRAR POR COMPLETO. SI ESTAS SEGURO QUE DESEA REALIZAR ESTA OPERACION PRESIONE: 'S/N':")
	if key == "s":
		print "......LISTADO DE HDD......."
		os.system("sudo df -h")
		dirhdd = raw_input("INGRESE EL PATH DE LA PARTICION: ")
		os.system("sfill -v %s" % dirhdd)
		print "TU HDD SE BORRO POR COMPLETO.... :D"
		sleep(2)
		os.system("clear")
		menu_principal()
	elif key == "n":
		os.system("clear")
		menu_principal()
	elif key != 'break':
		borrar_hdd()

def liberar_swap():
	"""funcion para liberar la memoria SWAP"""
	os.system("clear")
	banner_menu()
	print "--------LISTADO DE SWAP--------"
	os.system("sudo swapon -s")
	swapdir = raw_input("INGRESE EL PATH DE LA PARTICION: ")
	os.system("sudo sswap -v %s" % swapdir)
	print "MEMORIA SWAP LIBERADA... :D"
	sleep(2)
	os.system("clear")
	menu_principal()
#####llamada al funcion menu principal.....:S	
if __name__ == '__main__':
    menu_principal()
