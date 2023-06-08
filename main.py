#neco arc is the best waifu

import psutil,re,os
import time

black='\033[0;90m'
red='\033[0;91m'
green='\033[0;92m'
yellow='\033[0;93m'
blue='\033[0;94m'
purple='\033[0;95m'
cyan='\033[0;96m'
white='\033[0;97m'
off='\033[0m'
fgreen='\033[42;97m'
fred='\033[41;97m'

found_pids = []



banner=f"""
                                                                                                           
{purple}  ▄▄█▀▀▀█▄█         ██         ▀████▀  ▀████▀▀                       ██    {off}                                [{fred}I'll get you{off}]
{purple}▄██▀     ▀█         ██           ██      ██                          ██    {off}                                  \  
{purple}██▀       ▀▄█▀██▄ ██████         ██      ██  ▀███  ▀███ ▀████████▄ ██████  ▄▄█▀██▀███▄███   {off}                  \ 
{purple}██        ██   ██   ██           ██████████    ██    ██   ██    ██   ██   ▄█▀   ██ ██▀ ▀▀   {off}                   \  ,/|         _.--´^``-...___.._.,;
{purple}█▓▄        ▄███▓█   ██    █████  ▓█      █▓    ▓█    ██   █▓    ██   ██   ▓█▀▀▀▀▀▀ █▓     {off}                      /.  \.     _-`          .--,,,--´´´
{purple}▀▓█▄     ▄▀▓   ▓█   █▓           ▓█      █▓    ▓█    █▓   █▓    ▓█   █▓   ▓█▄    ▄ █▓   {off}                       [ \    `_-''           /]
{purple}▓▓▓        ▓▓▓▓▒▓   ▓▓           ▒▓      ▓▓    ▓█    ▓▓   ▓▓    ▓▓   ▓▓   ▓▓▀▀▀▀▀▀ ▓▓  {off}   (,).-"  ".            `;;'             ;   ; ;
{purple}▒▓▓▒     ▓▀▓   ▒▓   ▓▓           ▒▓      ▒▓    ▓▓    ▓▓   ▓▓    ▓▓   ▓▓   ▒▓▓      ▓▒  {off} _/',  _ (   )_____ ._.--''     ._,,, _..'  .;.'
{purple}  ▒ ▒ ▒ ▒▓▒▓▒ ▒ ▓▒  ▒▒▒ ▒      ▒▒▒ ▒   ▒ ▒▓▒▒  ▒▒ ▓▒ ▒▓▒▒ ▒▒▒  ▒▓▒ ▒ ▒▒▒ ▒ ▒ ▒ ▒▒▒ ▒▒▒ {off} `^'"` ""´´´'`       (,_....----'''     (,..--''
                                                            [{purple}https://cybercronic.rf.gd{off}]
                                                                                          
"""

def passive():
    while True:
        processes = psutil.process_iter()
        
        for proc in processes:
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline', 'username', 'exe'])
                cmdline = " ".join(pinfo['cmdline'])
                if 'bash' in cmdline and pinfo['username']:
                    if pinfo['pid'] not in found_pids:
                        found_pids.append(pinfo['pid'])
                        print(f"{fred}RevShell Found!{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} Bin: {red}{pinfo['exe']}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off}")
                cmdline = " ".join(pinfo['cmdline'])
                if 'sh' in cmdline and pinfo['username']:
                    if pinfo['pid'] not in found_pids:
                        found_pids.append(pinfo['pid'])
                        print(f"{fred}RevShell Found!{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} Bin: {red}{pinfo['exe']}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off}")
                if 'sshd' in pinfo['name'] and '-bash' not in pinfo['cmdline'] and pinfo['username'] != 'sshd' and pinfo['username'] != 'root':
                    if pinfo['pid'] not in found_pids:
                        found_pids.append(pinfo['pid'])
                        cmdline_str = ' '.join(pinfo['cmdline'])
                        pts_match = re.search(r'pts/\d+', cmdline_str)
                        tty = pts_match.group(0).split('/')[-1] if pts_match else '?' 
                        print(f"{fgreen}SSH Connection!{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} TTY: {red}{tty}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            except KeyboardInterrupt:
                os.system('clear')
                print(f"{fgreen} Adios{off}")
                exit()
def agressive():
    while True:
        processes = psutil.process_iter()
        
        for proc in processes:
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline', 'username', 'exe'])
                cmdline = " ".join(pinfo['cmdline'])
                if 'bash' in cmdline and pinfo['username']:
                    if pinfo['pid'] not in found_pids:
                        found_pids.append(pinfo['pid'])
                        print(f"{fred}RevShell Found!{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} Bin: {red}{pinfo['exe']}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off} {purple}|{off}{fred} Killed!")
                        os.system(f"kill -9 {pinfo['pid']}")
                cmdline = " ".join(pinfo['cmdline'])
                if 'sh' in cmdline and pinfo['username']:
                    if pinfo['pid'] not in found_pids:
                        found_pids.append(pinfo['pid'])
                        print(f"{fred}RevShell Found!{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} Bin: {red}{pinfo['exe']}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off} {purple}|{off}{fred} Killed!")
                        os.system(f"kill -9 {pinfo['pid']}")
                if 'sshd' in pinfo['name'] and '-bash' not in pinfo['cmdline'] and pinfo['username'] != 'sshd' and pinfo['username'] != 'root':
                    if pinfo['pid'] not in found_pids:
                        found_pids.append(pinfo['pid'])
                        cmdline_str = ' '.join(pinfo['cmdline'])
                        pts_match = re.search(r'pts/\d+', cmdline_str)
                        tty = pts_match.group(0).split('/')[-1] if pts_match else '?' 
                        print(f"{fgreen}SSH Connection!{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} TTY: {red}{tty}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off} {purple}|{off}{fred} Killed!")
                        os.system(f"cat kick.dat > /dev/pts/{tty}")
                        os.system(f"kill -9 {pinfo['pid']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            except KeyboardInterrupt:
                os.system('clear')
                print(f"{fgreen} Adios{off}")
                exit()

os.system("clear")
print(f"{banner}")
print(f"{green}[1]{off} Agressive Mode ({red}Kill Process{off})\n{green}[2]{off} Passive Mode ({red}Only Print Process{off})\n")
op=input(f"{green}[+]{off} Select Mode: ")

if op == '2':
    os.system('clear')
    print(banner)
    print(f"{green}[+]{off} Searching Process...\n")
    passive()
if op == '1':
    os.system('clear')
    print(banner)
    print(f"{green}[+]{off} Hunting Process...\n")
    agressive()
