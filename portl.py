import socket, time, sys
import argparse

__version__="0.1"
min_port=0
#max_port=65535
max_port=10000

parser = argparse.ArgumentParser(description="a simple python port scanner",epilog="author: blackc8")
parser.add_argument("hostname",metavar="<hostname>",help="host to scan")
parser.add_argument("-dp","--ddport",help="do not display port",action="store_true")
parser.add_argument("-sF","--show_filtered",help="show filtered ports",action="store_true")
parser.add_argument("-b","--banner",help="grab the banners of ports",action="store_true")
parser.add_argument("-v","--version",help="dispaly version",action="version",version="%(prog)s ("+__version__+")")

args=parser.parse_args()

def w_log(msg):
    print(msg)

def _exit(error):
    w_log("[-] {}".format(error))
    w_log("exited")
    sys.exit()

def resolve_hostname(hostname):
    try:
        IPaddr=socket.gethostbyname(hostname)
        return IPaddr
    except socket.error:
        return 0

def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

def is_open(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    con = sock.connect_ex((host,port))
    sock.close()
    return con

def grab_banner(host,port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con  = sock.connect((host,port))
        sock.settimeout(3)
        banner = sock.recv(1024)
        banner = banner.decode().strip('\n')
        return banner
    except:
        return "<no banner>"

def scan(hostname,ddport=False,gbanner=False,show_filtered=False):
    open_ports=[]
    filtered_ports=[]
    banners=[]

    if not validIP(hostname):
        hostIP=resolve_hostname(hostname)
        if hostIP == 0:
             _exit("Unable to resolve hostname ({})")
        else: host_info="{} ({})".format(hostname,hostIP)
    else:
        hostIP=hostname
        host_info=hostname

    if not validIP(hostIP):
        _exit("Invalid IP adddress {}".format(hostIP))

    w_log("[i] Scan started at: {}".format(time.asctime()))
    start_time=time.time()

    w_log("[+] Scaning host {}".format(host_info))
    for port in range(min_port,max_port):
        port_stat=is_open(hostIP,port)
        if port_stat == 0: # open port
            open_ports.append(port)
            if not ddport:
                w_log("port: {}".format(port))
                w_log("  state: open")
                if gbanner:
                    banner=grab_banner(hostname,port)
                    banners.append([port, banner])
                    w_log("  banner: {}".format(banner))

        elif port_stat == 11: # filtered port
            filtered_ports.append(port)
            if show_filtered:
                w_log("port: {}".format(port))
                w_log("  state: filtered")

    stop_time=time.time()
    time_taken=stop_time-start_time
    w_log("[i] {} open, {} filtered ports are discovered.".format(len(open_ports),len(filtered_ports)))
    w_log("[i] Scan completed in {:.2f} seconds.".format(time_taken))
    return True,open_ports,banners,time_taken

if __name__ == "__main__":
    scan(args.hostname,args.ddport,args.banner,args.show_filtered)
