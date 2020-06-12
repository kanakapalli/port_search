import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("this script is created by kanakapalli anurag, if any issue feel free to put it on github \n ask for scripts")
print(" google the website url in google to find it's ip adders")
host = input("enter ip adders:--")
port_s= input("enter START of  port  search limit:--\n")
port_e = input("enter END of  port  search limit:--")
# 443  , 80

def port_scanner(port):
    print(port)
    if s.connect_ex((host, int(port))):
        return print(" is closed")
    else:
        return print("---- is open")

print("searching for open port")
print("this might take time ")

for i in range(int(port_s) , int(port_e)+1):
    port_scanner(i)
