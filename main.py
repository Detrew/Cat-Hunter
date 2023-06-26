#neco arc is the best waifu <3

import psutil
import time
import os
import re

black = '\033[0;90m'
red = '\033[0;91m'
green = '\033[0;92m'
yellow = '\033[0;93m'
blue = '\033[0;94m'
purple = '\033[0;95m'
cyan = '\033[0;96m'
white = '\033[0;97m'
off = '\033[0m'
fgreen = '\033[42;97m'
fred = '\033[41;97m'

conold = []
found_pids = []
conexited = []

banner = f"""
{purple}  ▄▄█▀▀▀█▄█         ██         ▀████▀  ▀████▀▀                       ██    {off}                                [{fred}I'll get you{off}]
{purple}▄██▀     ▀█         ██           ██      ██                          ██    {off}                                  \  
{purple}██▀       ▀▄█▀██▄ ██████         ██      ██  ▀███  ▀███ ▀████████▄ ██████  ▄▄█▀██▀███▄███   {off}                  \ 
{purple}██        ██   ██   ██           ██████████    ██    ██   ██    ██   ██   ▄█▀   ██ ██▀ ▀▀   {off}                   \  ,/|         _.--´^``-...___.._.,;
{purple}█▓▄        ▄███▓█   ██    █████  ▓█      █▓    ▓█    ██   █▓    ██   ██   ▓█▀▀▀▀▀▀ █▓     {off}                      /.  \.     _-`          .--,,,--´´´
{purple}▀▓█▄     ▄▀▓   ▓█   █▓           ▓█      █▓    ▓█    █▓   █▓    ▓█   █▓   ▓█▄    ▄ █▓   {off}                       [ \    `_-''           /]
{purple}▓▓▓        ▓▓▓▓▒▓   ▓▓           ▒▓      ▓▓    ▓█    ▓▓   ▓▓    ▓▓   ▓▓   ▓▓▀▀▀▀▀▀ ▓▓  {off}   (,).-"  ".            `;;'             ;   ; ;
{purple}▒▓▓▒     ▓▀▓   ▒▓   ▓▓           ▒▓      ▒▓    ▓▓    ▓▓   ▓▓    ▓▓   ▓▓   ▒▓▓      ▓▒  {off} _/',  _ (   )_____ ._.--''     ._,,, _..'  .;.'
{purple}  ▒ ▒ ▒ ▒▓▒▓▒ ▒ ▓▒  ▒▒▒ ▒      ▒▒▒ ▒   ▒ ▒▓▒▒  ▒▒ ▓▒ ▒▓▒▒ ▒▒▒  ▒▓▒ ▒ ▒▒▒ ▒ ▒ ▒ ▒▒▒ ▒▒▒ {off} `^'"` ""´´´'`       (,_....----''      (,..--''
[{purple}https://0xc0nf1d3nt.github.io{off}]						{green}[Version: 2.0]{off}
"""

# add new blacklists to your liking
blacklist = ["discord", "brave", "chrome"]

def form(ip):
    return ip.split(":")[0]


def con():
    while True:
        newcon = []
        conns = psutil.net_connections()
        for conn in conns:
            if (
                conn.status == "ESTABLISHED" and
                conn not in conold and conn.pid is not None and
                psutil.pid_exists(conn.pid)
            ):
                proc = psutil.Process(conn.pid)
                if (
                    proc.name() == "bash" and proc.cmdline()[0] == "/bin/bash" or
                    proc.name() == "sh" and proc.cmdline()[0] == "/bin/sh"
                ):
                    newcon.append(conn)
                    username = proc.username()
        if newcon:
            for conn in newcon:
                if not any(prog in form(conn.laddr.ip) for prog in blacklist) and killer == 0:
                    print(f"{fred}RevShell Found{off} {purple}|{off} PID: {red}{conn.pid}{off} {purple}|{off} To: {red}{form(conn.laddr.ip)}{off} {purple}|{off} From: {red}{form(conn.raddr.ip)}{off} {purple}|{off} Status: {red}{conn.status}{off} {purple}|{off} Username: {red}{username}{off}")
                if not any(prog in form(conn.laddr.ip) for prog in blacklist) and killer == 1:
                    print(f"{fred}RevShell Found{off} {purple}|{off} PID: {red}{conn.pid}{off} {purple}|{off} To: {red}{form(conn.laddr.ip)}{off} {purple}|{off} From: {red}{form(conn.raddr.ip)}{off} {purple}|{off} Status: {red}{conn.status}{off} {purple}|{off} Username: {red}{username}{off} {purple}|{off} {fred} Killed {off}")
                    os.system(f"kill -9 {conn.pid}")
        conold.extend(newcon)
        processes = psutil.process_iter()
        for proc in processes:
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline', 'username', 'exe'])
                cmdline = " ".join(pinfo['cmdline'])
                if (
                    'sshd' in pinfo['name'] and
                    '-bash' not in pinfo['cmdline'] and
                    pinfo['username'] != 'sshd' and
                    pinfo['username'] != 'root'
                ):
                    if pinfo['pid'] not in found_pids:
                        found_pids.append(pinfo['pid'])
                        cmdline_str = ' '.join(pinfo['cmdline'])
                        pts_match = re.search(r'pts/\d+', cmdline_str)
                        tty = pts_match.group(0).split('/')[-1] if pts_match else None
                        if pinfo['username'] and tty and killer == 0:
                            print(f"{fred}Ssh Connect{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} TTY: {red}{tty}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off}")
                        if pinfo['username'] and tty and killer == 1:
                            os.system(f"cat kick.dat > /dev/pts/{tty}")
                            os.system(f"kill -9 {pinfo['pid']}")
                            print(f"{fred}Ssh Connect{off} {purple}|{off} User: {red}{pinfo['username']}{off} {purple}|{off} TTY: {red}{tty}{off} {purple}|{off} PID: {red}{pinfo['pid']}{off} {purple}|{off} {fred} Killed {off}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
            except KeyboardInterrupt:
                os.system('clear')
                print(f"{fgreen}Adios{off}")
                print(f"{green}[RevShells found]{off}:", len(conold))
                print(f"{green}[SSH Conections]{off}:", len(found_pids))
                exit()
os.system("clear")
print(banner)
print(f"{green}[1]{off} Agressive Mode ({red}Kill Process{off})\n{green}[2]{off} Passive Mode ({red}Only Print Process{off})\n")
op=input(f"{green}[+]{off} Select Mode: ")
try:
    if op == '2':
        os.system('clear')
        print(banner)
        print(f"{green}[+]{off} Searching Process...\n")
        killer = 0
    if op == '1':
        os.system('clear')
        print(banner)
        print(f"{green}[+]{off} Hunting Process...\n")
        killer = 1
    con()
except KeyboardInterrupt:
    os.system('clear')
    print(f"{fgreen}Adios{off}")
    print(f"{green}[Tasks found]{off}:", len(conold))
    print(f"{green}[SSH Conections]{off}:", len(found_pids))
    exit()

