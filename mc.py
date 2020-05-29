#!/usr/bin/python3

import subprocess
import re

class Mac_changer:
    iface = "wlan0"
    out = subprocess.run(["sudo", "ifconfig", iface], shell=False, capture_output=True)
    res = out.stdout.decode("utf-8")
    reg = re.findall(r"ether (.*) t", res)[0]

    def __init__(self, inface):
        out = subprocess.run(["sudo", "ifconfig", inface], shell=False, capture_output=True)
        res = out.stdout.decode("utf-8")
        reg = re.findall(r"ether (.*) t", res)[0]
        self.reg = reg

    def getmac(self):
       return self.reg

    def setchmac(self,iface,mac):
        self.reg = mac
        ch =subprocess.run(["sudo", "ifconfig",iface,"down"],shell = False , capture_output=True)
        print(ch.stderr.decode("utf-8"))

        ch1 =subprocess.run(["sudo", "ifconfig",iface,"hw","ether",mac],shell = False , capture_output=True)
        print(ch1.stderr.decode("utf-8"))

        ch2 = subprocess.run(["sudo", "ifconfig",iface,"up"],shell = False , capture_output=True)
        print(ch2.stderr.decode("utf-8"))

    def getnew(self):
       return self.reg
