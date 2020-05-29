#!/usr/bin/python3
from mc import *

if __name__=="__main__":
    interface = input("interface :")
    mc = Mac_changer(interface)
    print("[*]Current Mac Address :", mc.getmac())
    chmac = input("Enter MacAddress :")
    mc.setchmac(interface,chmac)
    print("[*] New Mac Address ...",mc.getnew())
