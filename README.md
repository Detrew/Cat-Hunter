![banner](https://cdn.discordapp.com/attachments/1041614683959988235/1096448793848852491/Screenshot_2023-04-14_11-55-09.png)
<h1>Cat-Hunter</h1> 

> :warning: In development

## About
A script made in python to see suspicious reverse shell processes and SSH connections Similar to Pspy

## Requisites
Python3 (tested on: Python 3.11.2) &
psutils

### install psutils whitout pip
```
wget https://files.pythonhosted.org/packages/3d/7d/d05864a69e452f003c0d77e728e155a89a2a26b09e64860ddd70ad64fb26/psutil-5.9.4.tar.gz -O psutil.tar.gz
tar -xvf psutil.tar.gz 
mv psutil-5.9.4 psutil
cd psutil
python3 setup.py install
```

## Modes
### Passive Mode
![passive](https://cdn.discordapp.com/attachments/1041614683959988235/1096456541835644981/Screenshot_2023-04-14_12-26-44.png)
The passive mode it just Will print suspicious processes of reverse Shell and De Successful ssh connections
it will show information like PID and user who made the command

### Aggressive Mode (Dangerous)
![agressive](https://cdn.discordapp.com/attachments/1041614683959988235/1096456999908159538/Screenshot_2023-04-14_12-28-33.png)
The aggressive mode it will kill any process he finds suspicious he is not recommended as he can leave the system with no return
