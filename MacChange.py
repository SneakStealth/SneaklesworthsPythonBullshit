#!/usr/bin/env python
#Python 3 only fucker. Until can import input
import subprocess #Allows for interfacing with shell and running system commands.
import optparse #module to allow for parsing from command line. This will let arguments come into play like -h -i -m

parser = optparse.OptionParser()


interface = input("Interface > ")
new_mac = input("Mac > ")
print("[+] Changing MAC Address for " + interface + " to " + new_mac)


# subprocess.call("sudo ip link set dev " + interface +" down" , shell=True)
# subprocess.call("sudo ip link set dev " + interface +" address " + new_mac , shell=True)
# subprocess.call("sudo ip link set dev " + interface + " up" , shell=True)
#
# The above 3 commands are insecure, they lack input validation in any sense.
# If a malicious user say for the intercface input did eth0;sudo rm -r -f / --no-preserve-root
# bad things would happen so dont use it like this

subprocess.call(["ip", "link", "set", "dev", interface, "down"])
subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
subprocess.call(["ip", "link", "set", "dev", interface, "up"])

#These set of commands work in a similar way, except it puts the command into a list instead of a single string
#which disallows a malicious user from injecting a different shell command. use this for subprocess






