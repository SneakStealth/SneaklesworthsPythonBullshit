#!/usr/bin/env python3
import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_brd = broadcast/arp_request
    response_list, no_response_list = scapy.srp(arp_req_brd, timeout=1)
    print(response.summary())



scan("172.16.0.0/22")


#easymode
#import scapy.all as scapy
# def scan(ip):
#     scapy.arping(ip)
#
# scan("172.16.0.0/22") #Can accept a single IP, or a range.


#Scapy notes

# scapy.ls(scapy.Ether) #Scapy.ls() will give you a list of the shit thats used in each module of scapy
# print(broadcast.summary())

# arp_request.pdst=ip   This is one way to do it, I like the above REF line 5
# arp_req_brd.show() #Show summary of the packet. All scapy items can get show method
#print(arp_req_brd.summary())
