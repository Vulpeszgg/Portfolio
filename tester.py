@ -0,0 +1,83 @@
import sys
import os
import time
import random

args = sys.argv[1:]
errors = []
success = []
f = list(os.popen('ls'))
files = []
for i in f:
    i = i.strip()
    files.append(i)

clear = '\x1B[0m'
color = '\x1B[0m'
answer = ''
count = 0
data = []

if len(args) == 1:
    if args[0] in files:
        success.append(clear+'\x1B[32;1m'+'[+] '+clear+'\x1B[36;3m'+'selected one file'+clear)
    else:
        errors.append(clear+'\x1B[31;1m'+'[-] '+clear+'\x1B[36;3m'+'there is no such file      '+clear)
elif len(args) > 1:
    errors.append(clear+'\x1B[31;1m'+'[-] '+clear+'\x1B[36;3m'+'selected more than one file'+clear)
else:
    errors.append(clear+'\x1B[31;1m'+'[-] '+clear+'\x1B[36;3m'+'no selected files          '+clear)

if len(errors) == 0:
    success.append(clear+'\x1B[32;1m'+'[+] '+clear+'\x1B[36;3m'+'no errors found  '+clear)
    filename = args[0].split('.')[0]
    type = args[0].split('.')[-1]
    file = args[0]
    commands = {'py': 'python3 '+file, 'js': 'rhino '+file, 'exe': 'mono '+file, 'c': 'cc '+file+' -o '+filename+' && ./'+filename, 'cpp': 'g++ -o '+filename+' '+file+' && ./'+filename}
    start = time.time()
    os.system(commands[type])
    os.system('clear')
    end = time.time() - start
    answer = str(end)[0:12]+'\x1B[34;49m'+' sec     '+clear
    color = '\x1B[32;2m'
    count = 21
    data = success
else:
    os.system('clear')
    color = '\x1B[31;2m'
    count = 31
    data = errors

# interface

cols, lines = os.get_terminal_size()

if cols % 2 == 0:
    b = '\b'
else:
    b = '\b\b'

width = cols - 6
heigth = (lines - 2 - count)//2

colors = ['\x1B[2;1m', '\x1B[31;1m', '\x1B[32;1m', '\x1B[33;1m', '\x1B[34;1m', '\x1B[35;1m', '\x1B[36;1m', '\x1B[37;1m']
c = random.choice(colors)

logo = os.popen('figlet "GEA Testing"') # width is 56

print(c, end='')
for i in logo:
    print((width-56)//2*" "+i, end='')

time.sleep(2)

print(clear+color+"  +"+(width-2)*"-"+"+  ", end="  ")
for i in range(2, heigth):
    print("  |"+width*" ", end="\b\b"+"|\n")
for i in data:
    print("  |"+(width-count)//2*" "+i+(width-count)//2*" "+color+b+"|  ")
if len(answer) > 0:
    print("  |"+(width-count)//2*" "+clear+'\x1B[1;49m'+answer+(width-count)//2*" "+color+b+"|  ")
for i in range(2, heigth):
    print("  |"+width*" ", end="\b\b"+"|\n")
print("  +"+(width-2)*"-"+"+  ")
