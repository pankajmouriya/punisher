import optparse
import socket
import dns.resolver
import whois
import requests
import os
#-----------------------------------------------------------
G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m' # white
def banner():
    print("""%s
                    ____              _     _               
                   |  _ \ _   _ _ __ (_)___| |__   ___ _ __ 
                   | |_) | | | | '_ \| / __| '_ \ / _ \ '__|
                   |  __/| |_| | | | | \__ \ | | |  __/ |     ▄︻̷̿┻̿═━一
                   |_|    \__,_|_| |_|_|___/_| |_|\___|_|   
                                                      %s
                # Coded By Rootrwx - @rootrwx %s
    """ % (R, W, Y))
banner()
print("------------------------------------------------------------")
print("Options available in Pigscan      \n")
print("1 : For DNS Details(ip,fqdn,NS,MX)\n")
print("2 : For whois details             \n")
print("3 : For port enumeration          \n")
print("4 : Https header and Requests info\n")
print("5 : Data exfiltration\n")
print("6 : Covering Tracks\n")


print("------------------------------------------------------------")
print("Usage : python pigscan.py -t target.com -o 1 or 2 till 6 \n")
print("------------------------------------------------------------")


parser = optparse.OptionParser('hERE yOU gO')
parser.add_option('-t', dest='host_name', type='string', \
help='specify target host')
parser.add_option('-o', dest='val', type='int', \
help='specify options')
(options, args) = parser.parse_args()
host_name = options.host_name

val = options.val
if (host_name == None) | (val == None):
    print(parser.usage)
    exit(0)
if val == 1:
    print("Name                             ", host_name)
    ip = socket.gethostbyname(host_name)
    print("DNS name                         ", host_name)
    print("IP                               ", ip)
    print("Fully Qualified Domain Name      ", socket.getfqdn(ip))
    dns_value = dns.resolver.query(host_name, 'NS')

    for name_s in dns_value:
        print("NameServers                    ", name_s)
    mx_value = dns.resolver.query(host_name, 'MX')

    for m_x in mx_value:
        print("Mail Exchanger                ", m_x)
    print("-----------------------------------------------------------------")
elif val == 2:
    who_result = whois.query(host_name)
    print(who_result.name)
    print(who_result)
    print(who_result.__dict__)
    print(who_result.expiration_date)


    print("-----------------------------------------------------------------")
elif val == 3:

    i = 1
    ip = socket.gethostbyname(host_name)
    #mylist = [80, 443, 21]
    mylist = input("Enter Port to Enumerate")
    #mylist =[]
    #mylist.append(input('enter port : '))
    mylist = mylist.split(",")
    #for op in mylist:

    mylist= [int(x) for x in mylist]
    #mylist = mylist.split()
    #port = []
    #port = str(input("Enter Port number ,you want to enumerate  : "))
    #port = input("Enter Port number ,you want to enumerate  : ")

    for ports in mylist:
        try:
            con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            final_chk = con.connect_ex((ip, ports))
            if final_chk == 0:
                if i == 1:
                    print("report for {0} :".format(ip))
                    i = i - 1

                    print("Port {0} Open".format(ports))
                else:
                    print("Port {0} Close ".format(ports))

        except Exception as e:
            pass
            con.close()
    print("Connection Closed")
    print("-------------------------------------------------------------------")
elif val == 4:
    print("Http Header Result")
    status = requests.get('https://' + host_name)

    print("Http Status : ", status.status_code)
    print("Http Header : ", status.headers)
    print("Http Type   : ", status.encoding)
    print("--------------------------------------------------------------------")

elif val == 5:
    os.system("python DataExfilitrationClient.py ")

