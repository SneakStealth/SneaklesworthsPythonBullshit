#!/usr/bin/env python3
#==========================================Information.=========================================================
# Sneaklesworth Heavy Industries, 2020

#Comments for noobs.


#Python 3 only fucker. Until can import input, but people say its better to just use Python3 so, python3, fucker.

#If a python script (written on windows) fails to execute after chmod +X and ./script.py then
#The reason it fails is because of line endings or some bullshit being different on windows.
#sudo apt-get install dos2unix
#dos2unix /pathto/script.py
#you can also do unix2dos to do the reverse if you dev on unix and run on windows

##=============================================================================================================

import subprocess #Allows for interfacing with shell and running system commands.
import optparse #module to allow for parsing from command line. This will let arguments come into play like -h -i -m

#==================================FUNCTION DEFINITIONS=======================================================

def change_mac(interface, new_mac): #Defines the function to change the mac, so you can use it elsewhere easily

    print("[+] Changing MAC Address for " + interface + " to " + new_mac)  # This is a simple print just for sanity sake so you know what the address changes to as output
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])  # Uses the ip command to take the interface down
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])  # uses the IP command to assign a new address to the interface
    subprocess.call(["ip", "link", "set", "dev", interface, "up"])  # uses the ip command to bring the interface back up.

def get_arguments():
    parser = optparse.OptionParser()  # An object [parser] that can handle input using arguments via optparse
    parser.add_option("-i", "--interface", dest="interface",help="Interface that you want to change the MAC for")  # Option for interface
    parser.add_option("-m", "--mac", dest="mac",help="The Mac Address you want to change to.")  # Option for Mac Address
    (options, arguments) = parser.parse_args() #sends the arguments outside the function when the function is called
    if not options.interface: #If options.interface does not contain value then
        parser.error("[-] Please specify an interface. Use --help for more information.") #Prints the string, and exits
    elif not options.mac: #Else, if options.mac does not contain value then
        parser.error("[-] Please specify a MAC address. Use --help for more information.") #Prints the string, and exits
    return options

#=====================================STUFF===============================================================

options = get_arguments() #Calls get_arguments function
change_mac(options.interface, options.mac) #Calls the function defined above.


ip_output = subprocess.check_output(["ip", "link", "show", options.interface])
print(ip_output)




#=================================OLD GARBAGE===========================================================
# This section is commented out due to being replaced with  functions above. Functions are the best


#The 4 lines below are replaced with the get_arguments function.
# parser = optparse.OptionParser() #An object [parser] that can handle input using arguments via optparse
# parser.add_option("-i", "--interface", dest="interface", help="Interface that you want to change the MAC for") #Option for interface
# parser.add_option("-m", "--mac", dest="mac", help="The Mac Address you want to change to.") #Option for Mac Address
# (options, arguments) = parser.parse_args() #method which allows the parser object to understand what the user has input. It can return args to a variable. In this case it returns args and values




#subprocess.call("sudo ip link set dev " + interface +" down" , shell=True)
# subprocess.call("sudo ip link set dev " + interface +" address " + new_mac , shell=True)
# subprocess.call("sudo ip link set dev " + interface + " up" , shell=True)

# The above 3 commands are insecure, they lack input validation in any sense.
# If a malicious user say for the interface input did eth0;sudo rm -r -f / --no-preserve-root
# bad things would happen so don't use it like this


# print("[+] Changing MAC Address for " + interface + " to " + new_mac) #This is a simple print just for sanity sake so you know what the address changes to as output
#
# subprocess.call(["ip", "link", "set", "dev", interface, "down"]) #Uses the ip command to take the interface down
# subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac]) #uses the IP command to assign a new address to the interface
# subprocess.call(["ip", "link", "set", "dev", interface, "up"]) #uses the ip command to bring the interface back up.

#These set of commands work in a similar way, except it puts the command into a list instead of a single string
#which disallows a malicious user from injecting a different shell command. use this for subprocess


#===========================================================================================================