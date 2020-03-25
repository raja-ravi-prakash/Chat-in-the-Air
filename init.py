import socket as soc
from colorama import init, Fore, Back, Style
import os
import time

host_name = str(soc.gethostname())
ip_address = str(soc.gethostbyname(host_name))
port = "7888"
partner_name = ""
partner_ip = ""
partner_port = ""
reset = ""

init(convert=True)
print(Fore.GREEN+"\n\ninitializing....")
time.sleep(2)


def custom():
    global port
    port = input("[*]Enter port: ")
    printDetails()


def printDetails():
    print("\n")
    print(Style.BRIGHT+Fore.GREEN+" Host Machine :")
    print(Fore.MAGENTA + Style.BRIGHT + " Machine Host - > " +
          Fore.WHITE+" "+host_name+" ")
    print(Fore.MAGENTA + " Default IP   - > " +
          Fore.WHITE+" "+ip_address+" ")
    print(Fore.MAGENTA +
          " Default Port - > " + Fore.WHITE + " "+port+" ")


def partnerDetails():
    print(Style.BRIGHT+Fore.GREEN+"\n Partner Machine :")
    print(Fore.MAGENTA + Style.BRIGHT + " Machine Host - > " +
          Fore.WHITE+" "+partner_name+" ")
    print(Fore.MAGENTA + " Default IP   - > " +
          Fore.WHITE+" "+partner_ip+" ")
    print(Fore.MAGENTA +
          " Default Port - > " + Fore.WHITE + " "+partner_port+" ")


def partner():
    global partner_ip, partner_name, partner_port
    partner_ip = input("[*]Enter Partner IP: ")
    print(Fore.RED+"Note: If you are testing this using same machine, make sure port are different.."+Fore.WHITE)
    partner_port = input("[*]Enter partner port: ")
    try:
        partner_name = str(soc.gethostbyaddr(partner_ip)[0].split(".")[0])
    except Exception as e:
        print(str(e) + " InValid IP")
        quit()

    partnerDetails()


def choice():
    global reset
    print("\n")
    while(reset != 'y' and reset != 'Y' and reset != 'n' and reset != 'N'):
        reset = input(
            "\n[*]Do you want change your port ?(y/N)")


print(Fore.RED)
print("    <ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo>")
print("    <oooooooooooooooooooooooooooooo>                                   \n\n")
print(Fore.BLUE+"      oo oo oo oo oo oo")
print("      oo             oo")
print("      oo            oo")
print("      oo           oo")
print("      oo oo oo oo oo                                   oo")
print("      oo oo             oo oo oo      oo oo oo oo             oo oo oo oo")
print("      oo  oo          oo       oo     oo       oo      oo     oo       oo")
print("      oo   oo        oo         oo    oo       oo      oo     oo       oo")
print("      oo     oo       oo       oo     oo       oo      oo     oo       oo")
print("      oo       oo      oo oo oo       oo       oo      oo     oo       oo")
print(Fore.RED+"\n\n                                   <oooooooooooooooooooooooooooooooooooooo>")
print("    <oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo>")
print(Fore.WHITE+Style.BRIGHT + "    Author: Raja Ravi Prakash")
print("    Git: https://github.com/raja-ravi-prakash/Networking")


printDetails()
choice()
time.sleep(1)
if(reset == 'y' or reset == 'Y'):
    custom()
print(Fore.BLUE+"\nEnter Partner Details: \n"+Fore.WHITE)
partner()

input("\n[*]Press any key to continue....")

os.chdir("src")

command = "java Message "+partner_ip+" "+partner_port+" "+port+" "+partner_name
os.system(command)
