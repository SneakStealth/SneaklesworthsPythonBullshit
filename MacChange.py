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

# this runs on a unix system, if you couldn't tell. I looked it up for windows, suffice to say, go fuck yourselves.
##=============================================================================================================
import subprocess #Allows for interfacing with shell and running system commands.
import optparse #module to allow for parsing from command line. This will let arguments come into play like -h -i -m
import re #fucking regex
import sys #lol bytes-like strings
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

def current_mac(interface):
    ip_output = subprocess.check_output(["ip", "link", "show", options.interface]).decode(sys.stdout.encoding)  # I had to think about this. Thanks, mr linux.
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ip_output)
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("Could not get MAC address")

def validate_change():
    if sysmac == options.mac:
        print("[+]MAC Address successfully changed to: " + sysmac)
    else:
        print("[-]MAC Address unchanged!")
#=====================================STUFF===============================================================
options = get_arguments() #Calls get_arguments function
sysmac = current_mac(options.interface)
print("Current Mac Address: "+ sysmac)
change_mac(options.interface, options.mac) #Calls the function defined above.
sysmac = current_mac(options.interface) #is it worth turning you into a function? probably not.
validate_change()